This is a simple page that given a **valid username**, sends a reset request. Random and invalid usernames trigger different responses, so we can derive usernames with brute force. A basic one is **admin**.

One very interesting thing is that by giving random characters we were able to trigger an sql error to pop up, as shown in the following image.

![[Screenshot from 2024-09-10 20-19-13.png]]

So we can probably ex-filtrate data from this webpage such as passwords using [[error based sql injection]]. 