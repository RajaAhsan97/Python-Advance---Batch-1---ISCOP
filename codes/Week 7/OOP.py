# Programming Paradigms: (Style)
# 1. Sequential programming    --> line by line
# 2. Procedural programming    --> functions bnaty hein
# 3. Object Oriented Programming (OOP)  --> Object

# Real - life scenarios

# Object --> any thing under consideration
#   1.  characteristics/properties
#   2.  Behaiviours

# CLass --> template/design/blueprint of object

class StudentRecords():
    # constructor
    def __init__(self, name, roll_no, email, gender):
        # instance attributes
        self.name = name
        self.roll_no = roll_no
        self.email = email
        self.gender = gender

    # instance methods
    def attend_class(self):
        print(f"{self.name} can attend class")

    def appear_exam(self):
        print(f"{self.name} bearing roll_no: {self.roll_no} appears in exam")

    def result(self):
        print(f"{self.name} pass in examp")


std1 = StudentRecords("Ahsan", "AI-9030", "xyz@gmail.com", "Male") 
std2 = StudentRecords("Ehsan", "AI-9031", "XYZ@gmail.com", "Male")

std2.name = "Saad"


print(std2.name)
print(std2.email)
print(std2.roll_no)
print(std2.gender)

print(std2.appear_exam())
print(std1.appear_exam())


# Pillars of OOP:
#   1. Encapsulation
#   2. Inheritance
#   3. Polymorphism
#   4. Abstraction