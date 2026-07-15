# enumerate() adds an index to each item while iterating.

fruits = ["Apple", "Banana", "Orange"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

print("\n")

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

print("\n")    

# zip() combines multiple iterables element by element.
# zip() stops when the shortest iterable ends.

names = ["A", "B", "C"]
ages = [20, 21, 22]
cities = ["Delhi", "Mumbai", "Pune"]

for name, age, city in zip(names, ages, cities):
    print(name, age, city)

print("\n")

# map() applies a function to every element in an iterable.

def square(x):
    return x * x

numbers = [1, 2, 3, 4]        #without lambda function
result = map(square, numbers)
print(list(result))

print("\n")

numbers = [1, 2, 3, 4]     #with lambda function
result = map(lambda x: x * 2, numbers)
print(list(result))

# filter() keeps only the elements that satisfy a condition.

def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
result = filter(is_even, numbers)
print(list(result))

print("\n")

numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))

print("\n")

#  sorted() returns a new sorted list from the elements of any iterable.
# .sort() sorts the list in place and returns None.