#!/usr/bin/python3

import cgi, cgitb
import json
import os
from sys import exit

cgitb.enable() # for debugging

target_directory = "nybles-submissions"

form = cgi.FieldStorage()

response = {
    "title": form.getvalue("title"),
    "author": form.getvalue("author"),
    "categories": list( map(lambda cat : cat.strip() ,form.getvalue("categories").split(",")) ),
    "content": form.getvalue("content")
}

if ( (not response["title"]) or
     (not response["author"]) or
     (not response["categories"]) or
     (not response["content"]) ):
    print ("Content-type: text/plain")
    print ()
    print ("Incomplete submission")
    exit(0)


# everything's fine
filename = response["author"] + '-' + response["title"] + ".md"
target = os.path.join(target_directory, filename)
with open (os.path.join(os.getcwd(), target), 'w') as f:
    f.write(json.dumps(response, indent=4))


print ("Content-type: text/html")
print ()

print ("""
<html>
<body>
Response received.
Redirecting...
<script>
document.location = "https://nybles.github.io/"
</script>
</body>
</html>
""")
