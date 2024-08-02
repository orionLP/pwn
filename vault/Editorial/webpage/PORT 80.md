## FUZZES

**Trying to get more endpoints** 

```bash
┌──(root㉿kali)-[~]
└─# ffuf -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-big.txt -u http://editorial.htb/FUZZ 

about                   [Status: 200, Size: 2939, Words: 492, Lines: 72, Duration: 92ms]
upload                  [Status: 200, Size: 7140, Words: 1952, Lines: 210, Duration: 58ms]


┌──(root㉿kali)-[~]
└─# ffuf -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-big.txt -u http://editorial.htb/static/FUZZ 

Nothing, although i know this is not the case, the website marks as not found anything it does not want you to see, so i can't tell good from bad'

┌──(root㉿kali)-[~]
└─# ffuf -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-big.txt -u http://editorial.htb/static/css/FUZZ

Nothing
```

**Trying to discover subdomains**

```bash
┌──(root㉿kali)-[~]
└─# ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -u http://FUZZ.editorial.htb/

2600 done , none found 
```

## SITEMAP

**There are parts not listed here, as burp creates a map itself**

- /: Also the home endpoint, contains links to other parts and a subscription button (non functional). The links below get you to the top of the page. The search functionality at the top also does nothing.
- /upload: contains a book upload functionality (that actually works to submit anything). Can be used given an url or an uploaded file. The button also has a custom script added to it that posts data to **/upload-cover**. There is also another form to send contact info about books
- /about: Information about the website, plus a contact email submissions@tiempoarriba.htb. 

Actually, one thing that seems common is to blacklist all pages you do not want seen in not found :( 
## CODE REVIEW

- /
The original code uses urls for images relative to the current path, but cannot find those images in any other place that is not the site
- /about: nothing interesting
- /static/css/bootstrap.min.css: simply css
- /static/css/bootstrap.min.css.map: contains references to other parts of the site (which seems like i can't access to weridly though) such as "../../scss/_popover.scss"
- /static/images: [[images]]: contains images used for the web page
- /upload: nothing out of the ordinary that has not been commented already
- /static/uploads: seems uploaded images go here, they seem to be deleted shortly after, they 
## /upload-cover

**GET**
Redirect to the /upload page

## /upload 

**POST first form**
Uploads are done from /upload, the related code is 

```html
<form id="form-cover" method="post" enctype="multipart/form-data">
          <div class="row g-3">

            <div class="col-6">
              <div style="float:left; width:10%;">
                <img style="width: 70%; border-radius: 3px;" id="bookcover" src="/static/images/unsplash_photo_1630734277837_ebe62757b6e0.jpeg">
              </div>

              <div style="float:right; width:90%;">
                <input type="text" class="form-control" name="bookurl" id="bookurl" placeholder="Cover URL related to your book or">
              </div>
            </div>

            <div class="col-5">
              <input type="file" class="form-control" name="bookfile" id="bookfile">
            </div>

            <div class="col-1">
              <button type="submit" class="form-control" id="button-cover">Preview</button>
            </div>

          </div>
        </form>
```

```javascript 
         document.getElementById('button-cover').addEventListener('click', function(e) {
            e.preventDefault();
            var formData = new FormData(document.getElementById('form-cover'));
            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/upload-cover');
            xhr.onload = function() {
              if (xhr.status === 200) {
                var imgUrl = xhr.responseText;
                console.log(imgUrl);
                document.getElementById('bookcover').src = imgUrl;

                document.getElementById('bookfile').value = '';
                document.getElementById('bookurl').value = '';
              }
            };
            xhr.send(formData);
          });
```


Let us play with these parameters, specifically, for the [[images]] uploaded. And also trying to upload [[documents]].

**Actually i had to look this up**: i did think of using the url functionality to send requests to the own server (ssrf), however, as i was always given the same image i quickly gave it up. I did not think of testing other ports, which i should have done.

If we actually input http://127.0.0.1:5000 we see that an image was created, let us try to fetch it, we get the following content

So let us continue in [[PORT 5000]]
