import random
print("Enter range: ")
x = int(input())
m = list(random.randint(0, 100) for i in range(x))
print(m)
s = sum(m)
print(s)
l = s/len(m)
print(l)
