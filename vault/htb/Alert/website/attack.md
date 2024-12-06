A basic request that we can do is:

```http
------WebKitFormBoundaryuBle3WAwY9lxiCu3
Content-Disposition: form-data; name="file"; filename="epic.md"
Content-Type: text/markdown

<?= echo "hello"; ?> 
------WebKitFormBoundaryuBle3WAwY9lxiCu3--
```

**Notice**:

- There is no validation for the content
- The resulting file is uploaded into /uploads with a random name and md extension (don't know yet if it is always the case)

**Attempting to bypass the extension filter**

