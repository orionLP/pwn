```python
import os
import uuid
import json
import requests
from flask import Flask, render_template, request, redirect, url_for

# -------------------------------
# App configuration
# -------------------------------
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "app_editorial/static/uploads/"

# -------------------------------
# Program functions
# -------------------------------
# -- Reject internal requests
def request_reject_localhost(url_bookcover):
    reject_url = ["localhost", "127.0.0.1"]
    for i in reject_url:
        if i in url_bookcover.lower():
            return True

# -- Editorial information (API)
def api_editorial_info(key):
    r = requests.get('http://127.0.0.1:5000/api')
    json_editorial_info = json.loads(r.text)

    editorial_api_version = list(json_editorial_info['version'][-1].keys())[0]

    if key == "name":
        editorial_api_value = json_editorial_info['version'][-1][editorial_api_version]['editorial']
    elif key == "contact":
        editorial_api_value = json_editorial_info['version'][-1][editorial_api_version]['contact_email']

    return editorial_api_value

# -------------------------------
# Website routes
# -------------------------------
# -- Index page
@app.route('/')
def index():
    return render_template('index.html', editorial_name=api_editorial_info('name'))

# -- Upload book to be published
# does nothing
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html', default=True, editorial_name=api_editorial_info('name'))

    elif request.method == 'POST':
        book_name = request.form['bookname']
        book_intro = request.form['bookintro']
        whyus = request.form['whyus']
        email = request.form['email']
        phone = request.form['phone']

        # To do: Connect forms and inputs
        return render_template('upload.html', default=True, editorial_name=api_editorial_info('name'), success_upload="✍️  Request Submited! 🔖")

# -- Upload cover book
@app.route('/upload-cover', methods=['GET','POST'])
def upload_cover_image():
    if request.method == 'GET':
        return redirect(url_for('upload'))

    elif request.method == 'POST':
        file_bookcover = request.files['bookfile']
        url_bookcover = request.form['bookurl']
        default_cover = "https://images.unsplash.com/photo-1630734277837-ebe62757b6e0?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80"

        uuid_filename_cover = str(uuid.uuid4()) # secure filename

        # If cover comes from an URL
        if url_bookcover:
	        # url cannot be localhost, you cannot reference yourself
            if request_reject_localhost(url_bookcover):
                return default_cover

            try: # Set default cover if exists a connection problem
                r = requests.get(url_bookcover, timeout=1)
            except:
                return default_cover

            # Save the response to the request in a file
            # file is always saved in a random file
            with open(app.config['UPLOAD_FOLDER'] + uuid_filename_cover, 'wb') as file_url_bookcover:
                file_url_bookcover.write(r.content)

        # If cover comes from a FILE
        elif file_bookcover:
	        # file is always saved in a random file
            file_bookcover.save(os.path.join(app.config['UPLOAD_FOLDER'], uuid_filename_cover))
        # Neither.
        else:
            return default_cover

		# never going to happen
        return os.path.join(app.config['UPLOAD_FOLDER'], uuid_filename_cover)

# -- About our editorial
@app.route('/about')
def about():
    return render_template('about.html', editorial_name=api_editorial_info('name'), editorial_contact=api_editorial_info('contact'))

# -- TODO: validate with team feature to send mail to new authors, message is already in api.

# -------------------------------
# Start program
# -------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0')

```


Inside the computer 

```bash
dev@editorial:/opt/apps/app_editorial/venv$ cat pyv*
home = /usr/bin
include-system-site-packages = false
version = 3.10.6
```