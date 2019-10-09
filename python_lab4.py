from functools import wraps

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


if __name__ == '__main__':
    main()
