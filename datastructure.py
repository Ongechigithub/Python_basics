# list mutable
fruits = ["Mangoes", "Oranges", "Bananas", "Watermelon"]
fruits.sort()
num = [11, 3, 7, 8, 14, -3, 2]
num.sort()
num[3] = 9
rep = num * 2
print(len(num))

print(fruits)
fruits[1] = "Apples"
print(f"I love eating fruits {fruits[1]}")
print(num)
print(rep)

# tuples immutable ordered
cars = ("Toyota", "Mercedes", "Nissan")
# cars[0]="vw"
print(cars[0])
tup = cars * 3
print(tup)
print(tup.count("Nissan"))

# sets unordered
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print(days)

# dictionaries

staff_details={"Name":"Erick", "Age":30,"Company" "eMobilis" "Gender": "Male"}
print(staff_details)
print(f"Name %s" %staff_details["Name"])
