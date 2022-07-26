import os
#create file
f=open("hello.html","w")
f.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Webpage</title>\n</head>\n<body>\n<p>Namaskara</p>\n</body>\n</html>")
f.close()
#open
os.system("start \"webpage\" hello.html")