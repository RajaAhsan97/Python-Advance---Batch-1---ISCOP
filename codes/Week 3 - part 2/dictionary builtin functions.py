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

# # delete
# del record["Location"]

# print(record)

# # pop  --->   nikalna
# print(record.pop("Course"))

# print(record)

# # popitem
# print(record.popitem())

# print(record)

# # values
# print(record.values())

# # keys
# print(record.keys())

# # items
# print(record.items())

# get  ---> access value (safe)
#print(record["Status"])
#print(record.get("Name",  "key not present"))

meta_data = {"Status": "ongoing", "Contact": "+92-3xx-xxxxxxx"}

#record["mata_data"] = meta_data

# update
record.update(meta_data)

print(record)