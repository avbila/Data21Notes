def addition(num1, num2):  # normal function
    return num1 + num2


#  lambda expression:
add = lambda num1, num2: num1 + num2

print(add(2, 3))
print(add(2, 3))

#----

savings = [234, 555, 674, 78]

def bonus(list):  #normal way of doing it
    bonus =[]
    for x in list:
        bonus.append(x*1.1)
    return bonus

print(bonus(savings))

#labda way of doing it:
bonus_lambda = list(map(lambda x: x*1.1, savings))  # you need to add the list or something else to get the result in the format u wanted

print(bonus_lambda)

