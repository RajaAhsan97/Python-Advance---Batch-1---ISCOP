# # Part 1
# variable = "Ahsan"     # Global variable

# def my_func():
#     #variable = 9     # Local variable
#     print(variable)

# print(variable)
# my_func()

# # Part 2
# variable = 8     # Global variable

# def my_func():
#     global variable
#     variable = 9     # Local variable
#     print(variable)

# print(variable)
# my_func()
# print(variable)


# Part 3: Nesting of function
variable = 8     # Global variable

def outer_func():
    #variable = 9     # Local variable
    def inner_function():
        #variable = 10   # Local variable
        print(variable)
    print(variable)
    inner_function()

outer_func()