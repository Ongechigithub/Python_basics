class fruits:
    def __init__(self, type, price, color):
        self.type = type
        self.price = price
        self.color = color

    def onyesha(self):
        print(f"I like eating {self.type} and it costs {self.price}, color being {self.color}")


# creating an object

myobj = fruits("banana", "Ksh 20", "yellow")
myobj1 = fruits("Orange", "Ksh 50", "Orange")
myobj2 = fruits("Mangoes", "Ksh 40", "Red")

myobj.onyesha()
myobj1.onyesha()
myobj2.onyesha()
