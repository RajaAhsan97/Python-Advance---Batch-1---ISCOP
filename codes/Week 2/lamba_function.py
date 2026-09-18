# Lambda function --> Anonymous function (Es ka koi name nai hota)
#                     task to perform in one line

#lambda arugument : expression

# # Part 1
# # def square(x):
# #     return x**2

# square = lambda x : x ** 2

# print(square(5))

# # Part 2
# addition = lambda x, y : x + y

# print(addition(5,6))

# Part 3
# check if the given is EVen or odd

check_even = lambda value: "Even" if value % 2 == 0 else "Odd"

print(check_even(2))