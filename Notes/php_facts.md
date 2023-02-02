## PHP FACTS 

php wrappers: sometimes you may be allowed to use this to retrieve raw php or other types of files. using this shinanigan
parameter=php://fiter/convert.base64-encode/resource=file.php  <---- insted of including the file php and executing it, it will
transform it into base64 and give it back (neat trick, i have to look deeper into this).

Some directories are allowed to execute php and some are not, if you can find which ones you may be able to take leverage of a lfi 
into rce.

