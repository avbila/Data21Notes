x = [1,2,3,4,5,6,7,8,9,10,11,12,12,12]
y = [2,3,4,5,5,6,6,6,7,8,8,9,12]
z = [3,4,5,15,13,14]
a = [25,26]

x = set(x)
y = set(y)

x=x.intersection(y)
print(x)
x=x.intersection(z)
print(x)
x=x.intersection(a)
print(len(x))

x = int("-4")
y = int("+5")

print(x)
print(y)

