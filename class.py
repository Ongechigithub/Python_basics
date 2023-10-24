class Students:
    def __init__(self, name, course, gender, age):
        self.name = name
        self.course = course
        self.gender = gender
        self.age = age

    def wanafunzi(self):
        print("Name: %s \n Course: %s \n Gender: %s \n Age: %s"
              % (self.name, self.course, self.gender, self.age))


stud1 = Students("Erick Were", "Computer Science", "Male", "25")
stud1.wanafunzi()
stud2 = Students("Ann Mungai", "Software Engineering", "Female", "20")
stud3 = Students("Felix Dan", "Education Science", "Male", "30")
stud4 = Students("Vivian Mmboga", "Doctor", "Female", "25")
stud2.wanafunzi()
stud3.wanafunzi()
stud4.wanafunzi()
