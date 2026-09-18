# Loops --> Repeat code several number of time
# 1. for  ---> if I n=know number of iterations
# 2. While  ---> if we donot know number of iterations

# for loop 
# for <variable_name> in <sequence>:
#    # block of code
# print(range(10))

# for i in range(10):  #[0,1,2,3,4,5,6,7,8,9]
#     print(i)

# for i in range(0,11,3):  #[0,2,4,6,8,10]
#     print(i)

# for ch in "Ahsan":
#     print(ch)

# for i in range(10):
#     print(i)
#     if i == 8 or i == 5:
#         # body
#         print("The number found")

# for i in range(10):
#     print(i)
#     if i == 8:
#         # body
#         break

# sample program: Write a program to print even numbers from 2 to 20
# for i in range(2,21):
#     if i % 2 == 0:
#         print(i)

# for i in range(10):
#     if i == 2:
#         continue     # skip iteration 

#     print(i)

# while
# while condtion:
#     # body

i = 1
while i <= 5:
    print(i)

    i += 1

