# Programming Paradigm: Programming ka style
#     1.  Sequential programming:  line by line
#     2.  Procedural Programming: functions banty hein   ---> Debugging asaan horhi h
#     3.  Object oriented programming (OOPs): Objects   
#                Hum kisi bi real world scenario ki assani sy programm kr sakty hein


# What is Object?
#    Anything user observation 
#      
# Object must have:
#   - characteristics/properties
#   - Behaviour/actions
# Object is an instance of class

# sab sy pehly hum Object ka design bnaengy


# Class:
#    - Design of Object
#    Technical definition
#    - Class is a blueprint or template of Object


# class and Objects
# class ka jo bi name hoga --> wo camel case

# blueprint
class mobilePhone:
    # characteristice / properites /attributes / varibles
    # hard coded
    camera = "28MP"
    ram = "16GB"
    storage = "128GB"
    model = "iphone"
    price = 200000

    # behaviours / Instance methods
    # self --> special variable --> jo object ko point out krta h
    def taking_photo(self):
        print(f"I can take pictures from {self.camera} camera")

    def call(self):
        print(f"I can call my {self.model} camera")

# class ka object bnana paryga
m1 = mobilePhone()
m2 = mobilePhone()

print(m1)
print(m2)

print(m1.price)
print(m1.camera)

print(m2.camera)


print(mobilePhone.taking_photo(m1))

# or

print(m1.taking_photo())

#print(m2.taking_photo())