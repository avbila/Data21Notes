

#If statements:
age = 13

if age > 18:
    print("You are older than  18.")
elif age >12:
    print("You are 12 to 18")
else:
    print("Younger than 12")

#For loops:
list_data = [1,2,3,4,6,8,5]

for i in list_data:
    print(i)

#while loops:
x = 0
while x<10:
    print(x)
    x+=1
    if x == 3:
        break

while True:
    age = input("What is your age?   ")
    if age.isdigit():
        break
    else:
        print("Please provide age")