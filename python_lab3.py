def decorator_for_html_tags(f):
    def wrap(*args):
        text = f(*args)
        tags = {"paragraph": "p", "header": "h1", "hyperlink": "a", "article": "article", "body": "body", "button": "button", "column": "col", "directory list": "dir", "section": "div", "footer": "footer", "image": "img", "list item": "li", "metadata": "meta", "navigation links": "nav", "short quotation": "q", "script": "script"}
        for x in tags.keys():
            if text[0] == x:
                print("<" + tags[x] + "> " + text[1] + " </" + tags[x] + ">")
            elif text[0] == x:
                print("<" + tags[x] + "> " + text[1] + " </" + tags[x] + ">")
    return wrap


@decorator_for_html_tags
def list(*args):
    return args


m = input("Pick the html tag from (paragraph, header, hyperlink, "
          "article, body, button, "
          "column, directory list, section, "
          "footer, image, list item, metadata,"
          " navigation links, short quotation, script): ")
o = input("Enter text fot html tags: ")

list(m, o)