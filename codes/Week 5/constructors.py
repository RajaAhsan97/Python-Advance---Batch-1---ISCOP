# constructor ----> humari class ki jitny bi attribtes un my default value initialize krwata h

class mobilePhone:

    # initializers
    def __init__(self, camera, ram, storage, model, price):
        # Instance attributes
        self.camera = camera
        self.ram = ram
        self.storage = storage
        self.model = model
        self.price = price

    # Instance methods
    # self --> special variable --> jo object ko point out krta h
    def taking_photo(self):
        print(f"I can take pictures from {self.camera} camera")

    def call(self):
        print(f"I can call my {self.model} camera")

# objec t bnaty hein
m1 = mobilePhone("28Mp", "16GB", "128GB", "iphone", "200000")
m2 = mobilePhone(camera="16MP", storage="256GB", ram="8gb", model="infinix", price="70000")

print(m2.camera)
print(m2.model)
print(m2.price)

print(m2.taking_photo())
print(m2.call())