import random

def lst(n, a, b):
    lst0 = []
    for i in range(n):
        lst0.append(random.randint(a, b))
    return lst0

def input_data():
    n = int(input("Enter number: "))
    a = int(input("Enter the beginning: "))
    b = int(input("Enter the ending: "))
    return n, a, b

def main():
    n, a, b = input_data()
    l = lst(n, a, b)
    print("List - " + str(l))
    print("Sum of the list - " + str(sum(l)))
    print("Average of the list - " + str(sum(l)/n))

if __name__ == '__main__':
    main()