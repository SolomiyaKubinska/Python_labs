import random

def lst(n, a, b):
    lst0 = []
    for i in range(n):
        lst0.append(random.randint(a, b))
    return lst0

def main():
    n = int(input("Enter number: "))
    a = int(input("Enter the beginning: "))
    b = int(input("Enter the ending: "))
    l = lst(n, a, b)
    print("List - " + str(l))
    print("Sum of the list - " + str(sum(l)))
    print("Average of the list - " + str(sum(l)/n))

if __name__ == '__main__':
    main()