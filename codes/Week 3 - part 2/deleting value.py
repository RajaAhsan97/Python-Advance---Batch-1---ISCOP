record = {"Name": "Ahsan", "Course": "Python advance", "Batch": 1}

# accessing data
# print(record["Name"])
# print(record["Course"])

# Adding data to dictionary
record["institute"] = "ISCOP"
record["Location"] = "Gulshan"

print(record)

record["Location"] = "Newtown"

print(record)

del record["Location"]

print(record)