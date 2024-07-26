## SETTING A USER

Needs:
- image
- mail
- pass
- pass confirmation

```http
------WebKitFormBoundaryzxcTyow92enyebDl
Content-Disposition: form-data; name="authenticity_token"

twA0XtnM6x7FvHCwykoofpM4meYBex9PqJZCputLc92Uj84izhoLNW5T1y4P9a7pqBtbEQXqDDTPTv50jRGIYQ
------WebKitFormBoundaryzxcTyow92enyebDl
Content-Disposition: form-data; name="user[avatar]"; filename="477.jpg"
Content-Type: image/jpeg

IMAGE HERE ENCODED

------WebKitFormBoundaryzxcTyow92enyebDl
Content-Disposition: form-data; name="user[email]"

someemail@gmail.com
------WebKitFormBoundaryzxcTyow92enyebDl
Content-Disposition: form-data; name="user[password]"

aaaaaa
------WebKitFormBoundaryzxcTyow92enyebDl
Content-Disposition: form-data; name="user[password_confirmation]"

aaaaaa
------WebKitFormBoundaryzxcTyow92enyebDl
Content-Disposition: form-data; name="commit"

Sign up
------WebKitFormBoundaryzxcTyow92enyebDl--

```

After sending this the cookie changes

```txt
_emp_man_session=06%2B%2FGvECZQjet9Ff82EkEbEJv4wQ7nKA%2Bq6PSEpLQDmNwNnOoIlLaNY0kVxqDn5S5NJsKSj0l8n8iYSzV0CkxgGfWx3s9qZGygKGnHvflzVRSKjJ4oamdG7RQJlE65wotGgfnwh7xqPg0AFcWU7LcILOeRTlVSwd2AJc%2BDnQr9UGZ4ORhnZDq1T5iI%2BPw7YJlsa1T4SRGa1GiCXznlTK65r1isvXg4%2FpTi%2B%2BtVnKYh36h8UcRiSS7E3fTupjNKIerB9BnOMhINAcqM2rgTdCos19H7rn5ibKmQCLs4CP24hmbgzQtogWnO9XBsWnPlUQYE5iVbk33aR%2BsDpmAo650byAfqeiUusNoFpLuk6VmV3Qoj%2FJjOfciRrvZXtcSsOSejUvVBvVoZahwpaKO%2BnCni5KDpklRMpEfOcILGhMEQg8Y5MZ7zhYidGChKznKyy3DKujPuOfWCikMuuC4CsPIJ4xYT%2BL%2FXM0gidjdWiJR4UMyroYvH31tpMRj2WmrtFOL4MsR2dPVSyJs9jpQ5Q%2FP9HPc%2BKvq2T2JNI3DQ%3D%3D--3WK8tyd3acuMlB5v--akPTgfUBdUKmcbcU44xRbQ%3D%3D; path=/; HttpOnly; SameSite=Lax
```

During set up there is this 

```http

You are being <a href="http://site.empman.thm/rails/active_storage/disk/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDVG9JYTJWNVNTSWhibXgzZERob01uVTNZWFkzWW1jMk9IZGxaRGt6YjNCM2JHNXpjd1k2QmtWVU9oQmthWE53YjNOcGRHbHZia2tpVVdsdWJHbHVaVHNnWm1sc1pXNWhiV1U5SW1SbFptRjFiSFJmY0hKdlptbHNaUzV3Ym1jaU95Qm1hV3hsYm1GdFpTbzlWVlJHTFRnbkoyUmxabUYxYkhSZmNISnZabWxzWlM1d2JtY0dPd1pVT2hGamIyNTBaVzUwWDNSNWNHVkpJZzVwYldGblpTOXdibWNHT3daVU9oRnpaWEoyYVdObFgyNWhiV1U2Q214dlkyRnMiLCJleHAiOiIyMDI0LTA1LTIxVDE3OjQ5OjU0Ljc3OFoiLCJwdXIiOiJibG9iX2tleSJ9fQ==--ed0cd281552bb63a2741d18f767bd1a5153b094e/default_profile.png">

```

This also happens

```http
POST /v1/leaks:lookupSingle HTTP/1.1
Host: passwordsleakcheck-pa.googleapis.com
Content-Length: 43
X-Goog-Api-Key: dummytoken
Content-Type: application/x-protobuf
Sec-Fetch-Site: none
Sec-Fetch-Mode: no-cors
Sec-Fetch-Dest: empty
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Connection: close


:§DÀ!E5¤Ã<ß£æÉýÌä*® BÖ:[·ÆTöÏIØ»R«÷
```