# T = ("apple", "Cherry", "banana")
# # Unpacking
# green, red, yellow = T

# print(green)
# print(red)
# print(yellow)

T = ("apple", "Cherry", "banana", "mango")
# Unpacking
green, red, *yellow = T

print(green)
print(red)
print(yellow)