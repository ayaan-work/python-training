# A defaultdict is like a normal dictionary, but if a key doesn't exist, it automatically creates it with a default value instead of raising a KeyError.
from collections import defaultdict 

d = defaultdict(list)
d["python"].append(1)
d["python"].append(2)
print(d)


words = ["apple", "banana", "apple"]
count = defaultdict(int)
for word in words:
    count[word] += 1
print(count)


students = [
    ("CS", "Alice"),
    ("IT", "Bob"),
    ("CS", "Charlie"),
]
groups = defaultdict(list)
for dept, name in students:
    groups[dept].append(name)
print(groups)