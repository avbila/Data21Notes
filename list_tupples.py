
#Lists:
shopping_list = ["eggs","milk","bread"]

print(shopping_list)
print(type(shopping_list))
print(shopping_list[2])
shopping_list[0] = "chocolate"
print(shopping_list)
shopping_list.append("eggs")
print(shopping_list)

#Tupples:
shopping_tup=("bread", "milk","eggs")
print(shopping_tup)

#Dictionary:
student_1={
    "name": "Andrei",
    "Age": 37,
    "Stream": "data",
    "list": ["1","2","3"]
}

print(student_1)
print(student_1["list"][1])
student_1["name"] = "bob"
print(student_1)
print(student_1.values())
print(student_1.keys())
student_1["list"].remove("2")
print(student_1)

#Sets :

car_parts={"doors","windows","wheels"}
print(car_parts)
print(type(car_parts))
car_parts.add("headlights")
print(car_parts)
car_parts.discard("doors")
print(car_parts)