# Decision making structure

# if <condition>  ---> True
#    # Block code   1line or multiple lines
# else:
#     # Block of code    1 line or multiple lines

# part 1
# marks = int(input("Enter marks"))

# if marks >= 50:
#     print("Passed")
# else:
#     print("Failed")

# part 3
marks = 85

if marks >= 90 and marks <= 100:   # --> True       # 90 - 100 ----> A grade
    print("Ap pass hain")
    print("A Grade")
elif marks >= 80 and marks < 90:
    print("Ap pass hain")
    print("B Grade")
else:
    print("AP fail hain")
    print("C grade")

# a>b>c