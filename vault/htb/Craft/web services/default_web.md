## VISIBLE CONTENT

![[Screenshot from 2024-12-01 16-34-05.png]]

The landing website seems to be a **repository** for craft brews (beer i suppose) using **REST** technology. They talk about **future mobile functionality** to interface with their **public API**, as well as a **brew submission process**. The company is named Craft - HackTheBox © All Rights Reserved.

## SITEMAP

From the landing page there appears to be little content other than static one. The initial site map we get is the following:

![[Screenshot from 2024-12-01 16-43-20.png]]

For the client part the server seems to use libraries from google's hosted libraries (the call to ajax.googleapis.com, some that are hosted locally, as well as some custom scripts (namely plugins and script)

Other than that it appears to store images in ico (icons) and some css in the /static/css folder.

Another thing to mention is that any "incorrect" request (such as non-existent content) results in a server error (code 500)

After this i decided that this website probably had not much content in it, but did a fuzz just in case it discovered something new.

