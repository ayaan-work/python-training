#dictionary in python is an unordered collection of data in a key:value pair format. It is mutable and can be changed after creation. Dictionaries are defined using curly braces {}.
#dictionary is unordered, and cannot contain duplicate keys. Each key in a dictionary must be unique, and the values can be of any data type.
dict1={"name": "Alice",
        "age": 30,
        "city": "New York"
    }
print(dict1)

for key,value in dict1.items():
    print(key,value)


print(dict1["name"]) #accessing the value of a key in the dictionary  (gives error if the key is not present in the dictionary)
print(dict1.get("age")) #accessing the value of a key in the dictionary using get() method (gives None if the key is not present in the dictionary)

dict1["age"]=31 #changing the value of a key in the dictionary
print(dict1)

dict1.update({"city": "Los Angeles"}) #updating the value of a key in the dictionary using update() method
print(dict1)

d={} #creating an empty dictionary


def add_item(item, lst=[]):
    lst.append(item)
    return lst
                            #since the default value of lst is a mutable object (list), it will retain its value between function calls. So, when we call the function again, it will use the same list and append the new item to it.
print(add_item(1))
print(add_item(2))

print("/n")

def add_item(item, lst=None):
    if lst is None:
        lst = []                  #if the default value of lst is None, it will create a new list each time the function is called. So, when we call the function again, it will use a new list and append the new item to it.

    lst.append(item)
    return lst

print(add_item(1))
print(add_item(2))

