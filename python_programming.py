import urllib.request

page = urllib.request.urlopen("https://www.netflix.com/login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse")

text = page.read().decode("utf8")
    
where = text.find("title>")
where1 = text.find("</title")

start_of_title = where + 6
end_of_title = where1

title = text[start_of_title : end_of_title]

print(title)
