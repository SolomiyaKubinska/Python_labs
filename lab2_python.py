def decorator(html_tags_remover):
    def wrap(string):
        a = []
        dict_of_tags = {"<": "&lt;", ">": "&gt;", "&": "&amp;", "\"": "&quot;"}
        for x in html_tags_remover(string):
            if x in dict_of_tags.keys():
                a.append(dict_of_tags[x])
            else:
                a.append(x)
        return print("".join(a))
    return wrap

@decorator
def line(string):
    return string

def main():
    a = input("Enter text for escaping html tags: ")
    line(a)

if __name__ == '__main__':
    main()
