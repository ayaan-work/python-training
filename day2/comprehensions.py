# new_collection = [expression for item in iterable]
# new_collection = [expression for item in iterable if condition]

#list comprehension is a concise way to create lists in python. It consists of an expression followed by a for loop inside square brackets. We can also add an optional condition to filter the elements.
squares = [i * i for i in range(1, 6)]
print(squares)

evens = [i for i in range(1, 11) if i % 2 == 0]
print(evens)

names = ["alice", "bob", "charlie"]
upper = [name.upper() for name in names]
print(upper)

numbers = [1, 2, 3, 4, 5]
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print(labels)

print("\n")

#dictionary comprehension
squares = {i: i * i for i in range(1, 6)}
print(squares)


student = {
    "name": "Ayaan",
    "city": "Delhi"
}
reverse = {value: key for key, value in student.items()}
print(reverse)

print("\n")

#set comprehension
numbers = [1, 2, 2, 3, 3, 4]
unique = {x for x in numbers}
print(unique)

print("\n")


#multiple list comprehension
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]
flat = [num for row in matrix for num in row]
print(flat)

print("\n")

#multiple conditions in list comprehension
numbers = [i for i in range(1, 31) if i % 2 == 0 if i % 3 == 0]
print(numbers)