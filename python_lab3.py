def decorator_for_html_tags(tags=""):
    def decorator(func):
        def wrap(string):
            print("<" + tags + "> " + str(func(string)) + " </" + tags + ">")
        return wrap
    return decorator

@decorator_for_html_tags("div")
def list(string):
    return string

def main():
    return list(input("Enter text for html tags: "))

if __name__ == '__main__':
    main()