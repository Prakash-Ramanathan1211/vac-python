import json
file2 = open("data.json","r")
# print(file2.read())
data = file2.read()
name_data = json.loads(data)
print(name_data["name"])