def dan():
    print("My name is Dan")


dan()


def add():
    num = int(input("Enter First Num:"))
    num2 = int(input(("Enter Second Number")))

    print(f"Sum of {num} and {num2} is {num + num2}")


add()


def toshiba_class(fname, lname, collage, age):
    print(f"Student first name {fname} last name: {lname},"
          f" attending {collage}, he/she is {age} years old")


toshiba_class("Dan", "Felix", "eMobilis", "29")
toshiba_class("Jayden", "Kebaso", "Kisii University", "24")
