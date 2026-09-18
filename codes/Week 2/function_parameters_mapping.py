# def func(a, b, c):
#     print(a,b,c)

# # Positional mapping
# func(1,2,3)

# # keyword mapping
# func(c = 3, a= 1, b=2)

# # Hybrid mapping
# func(1, c =3, b=2)

def func(a, b=20, c=30):
    print(a,b,c)

func(10)

func(10, 40, 80)