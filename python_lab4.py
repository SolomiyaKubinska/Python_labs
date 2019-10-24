def wraps(func):
    def wrap_decorator(func0):
        def html_wrap(string2):
            return 0
        html_wrap.__name__ = func.__name__
        html_wrap.__doc__ = func.__doc__
        return html_wrap
    return wrap_decorator

def html_decorator(func):
    @wraps(func)
    def text_decorator(string1):
        print("<html>\n<head>\n\n</head>\n<body>\n\t<div> " + str(func(string1)) + " </div>\n</body>\n</html>")
    return text_decorator

@html_decorator
def html_text(string):
    """HTML text"""
    return string

def main():
    html_text(input("Enter text for html file: "))
    print(html_text.__name__)
    print(html_text.__doc__)
    print(help(html_text))

if __name__ == '__main__':
    main()
