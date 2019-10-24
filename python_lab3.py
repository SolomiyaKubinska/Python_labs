def decorator_for_html_tags(tags=""):
    def decorator(func):
        def wrap(str0):
            print("<" + tags + "> " + func(str0) + " </" + tags + ">")
        return wrap
    return decorator

@decorator_for_html_tags("div")
def line(str):
    return str

def main():
    a = input("Enter text for html tags: ")
    return line(a)

if __name__ == '__main__':
    main()