def decorator(html_tags_remover):
    def wrap(string):
        a = []
        dict_of_tags = {"<": "&lt;", ">": "&gt;", "&": "&amp;", "\"": "&quot;"}
        for x in html_tags_remover(string):
            if x in dict_of_tags.keys():
                x = dict_of_tags[x]
                a.append(x)
            else:
                a.append(x)
        return print("".join(a))
    return wrap

@decorator
def printline1(string):
    return string

def main():
    return printline1(input("Enter text for escaping html tags: "))

if __name__ == '__main__':
    main()
