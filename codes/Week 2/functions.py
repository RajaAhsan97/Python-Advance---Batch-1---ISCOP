# functions
# Modularity

# function definition
# def <Function_name>(input parameter):
#    # DOc string
#    # block of code

# 1. function name should be in snake case  --->  my_function
# 2. function can have parameter
# 3. function can return result

# PART 1:
# function definition
# function with no input parameters
# def my_func():
#     """
#         This is my test function, it can take no input and it 
#         does not return a value.

#         It can only prints a value
#     """   
#     print("Hello I am in function")

# # function calling
# my_func()

# print(my_func.__doc__)


# PART 2:

# # function definition
# def my_func(fname, lname):
#     """
#         This function takes first and last name, and combine them into a full name

#         Parameters:
#             fname: first name
#             lname: last name

#         Return:
#             return full name
#     """

#     full_name = fname + ' ' + lname    # contatination

#     return full_name

# # access function doc string
# #print(my_func.__doc__)

# # function calling
# name = my_func("Raja", "Ahsan")

# print(name)


# PART 3:

# function definition
# def my_func(fname="Raja", lname="Ahsan"):
#     """
#         This function takes first and last name, and combine them into a full name

#         Parameters:
#             fname: first name
#             lname: last name

#         Return:
#             return full name
#     """

#     full_name = fname + ' ' + lname    # contatination

#     return full_name

# # access function doc string
# #print(my_func.__doc__)

# # function calling 1
# name = my_func()

# print(name)

# # function calling 2
# name = my_func("areeba", "Khan")

# print(name)


# # Task: create a calculate_func (+,*,-,/)
# #        1. x
# #        2. y
# #        3 operator  (-)


# PART 4:
# function can return single or multiple value
def circle(r):
    """
        Compute are and circumference of a circle

        Parameters:
            r: radius

        Return
            area and circumferense
    """
    area = 3.14 * r ** 2
    circumference = 2 * 3.14 * r

    return area, circumference

#result = circle(5)
#print(result)

circle_area, circle_circumference = circle(5)

print("Area: ", circle_area)
print("Circumference: ", circle_circumference)