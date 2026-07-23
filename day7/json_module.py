# JSON is one of the most commonly used data formats for APIs, configuration files, and data exchange. In Python, you work with JSON using the built-in json module
import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data)
print(type(data))

print("\n")

#writing to a json file
student = {
    "name": "Ayaan",
    "age": 22,
    "city": "Delhi"
}

with open("day7/student1.json", "w") as file:
    json.dump(student, file, indent=4)

print("\n")

#load string->loads
text = '{"name":"Ayaan","age":22}'
data = json.loads(text)
print(data)
print(type(data))

print("\n")

#writing a string json->string
text = json.dumps(student)
print(text)
print(type(text))