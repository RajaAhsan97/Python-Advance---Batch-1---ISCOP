L = ["apple", "mango", 1,2,3,4]

# append
L.append("orange")

print(L)

# extend
L.extend([5,6,'cherry'])

print(L)

# insert element to specific position
L.insert(2, "blueberry")

print(L)

# remove an element from list  pop()
pop_element = L.pop()

print(pop_element)
print(L)

pop_element = L.pop(1)

print(pop_element)
print(L)

# delete and element from list
del L[0]

print(L)

# del L

# print(L)

# clear()
L.clear()

print(L)