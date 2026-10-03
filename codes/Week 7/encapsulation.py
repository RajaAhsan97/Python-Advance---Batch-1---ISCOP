# 1. Encapsulation: bundling attributes and methods into a single unit called class, while restricting direct access to internal details 

# Access modifiers
# a. Public
# b. Private ---> (__)
# c. Protected

class StudentRecords():
    # constructor
    def __init__(self, name, roll_no, email, gender):
        # instance attributes
        self.__name = name      # Private
        self.roll_no = roll_no  # Public
        self.email = email      # Public    
        self.gender = gender    # Public

    # instance methods
    def attend_class(self):
        print(f"{self.__name} can attend class")

    def appear_exam(self):
        print(f"{self.__name} bearing roll_no: {self.roll_no} appears in exam")

    def result(self):
        print(f"{self.__name} pass in examp")

    # setter method --> data py validaions laga sakty hein
    def set_name(self, new_name):
        blacklisted_name = ["rafiq", "rahul"]

        if new_name.lower() in blacklisted_name:
            print(f"{new_name} is blacklisted")
        else:
            self.__name = new_name

    # getter method --> private data ko access krta h
    def get_name(self):
        return self.__name

std1 = StudentRecords("Ahsan", "AI-9030", "xyz@gmail.com", "Male") 

std1.__name = "Saad"
std1.roll_no = "AI-9033"

print(std1.appear_exam())

std1.set_name("waqar")
print(std1.get_name())
print(std1.appear_exam())