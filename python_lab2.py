def decorator(func):
    def wrap():
        s = func()
        a =[]
        for x in s:
            if x == "<":
                x = "&lt;"
                a.append(x)
            elif x == ">":
                x = "%gt;"
                a.append(x)
            elif x == "&":
                x = "&amp;"
                a.append(x)
            elif x == "\"":
                x = "%quot;"
                a.append(x)
            else:
                a.append(x)
        return print(a)
    return wrap


@decorator
def printline1():
    m = "<ul> <li>WELCOME</li> <hr width=\"1\" size=\"10\"> <li>ABOUT US</li> <hr width=\"1\" size=\"10\"> </ul>"
    return m


printline1()

