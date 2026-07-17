from collections import Counter
#Counter is a subclass of dict that helps count hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values.

l=[1, 1, 1, 2, 2, 3, 3, 3, 3, 4]
counter=Counter(l)
print(counter) #prints Counter({3: 4, 1: 3, 2: 2, 4: 1})

l1=["apple", "banana", "orange", "apple", "banana", "apple"]
counter1=Counter(l1)
print(counter1) #prints Counter({'apple': 3, 'banana': 2, 'orange': 1})

print(counter1["apple"])

counter1["grape"]=5
print(counter1) #prints Counter({'apple': 3, 'banana': 2, 'orange': 1, 'grape': 5})
del counter1["banana"]
print(counter1) #prints Counter({'apple': 3, 'orange': 1, 'grape': 5})


c=Counter({"a":3, "b":1, "c":2})
c.update("abc")
print(c) #prints Counter({'a': 4, 'c': 3, 'b': 2})

c1=Counter(a=3, b=1, c=2, d=-2)
s=sorted(c1.elements())
print(s) #prints ['a', 'a', 'a', 'b', 'c', 'c']

lst=[1, 1, 2, 3, 3]
counter=Counter(lst)
print(counter.most_common(2)) #prints [(1, 2), (3, 2)]

#c.subtract(d) method subtracts element counts from another Counter or iterable. It can be used to remove elements from a Counter.
#c.total() method returns the total of all counts in the Counter. It can be used to get the total number of elements in a Counter.

#mathematical operations on counter
e=Counter(a=2,b=1)
f=Counter(a=1,b=2)
print(e+f)   #add two counters together 
print(e-f)   #subtract(keeping only positive counts)
print(e & f) #intersection: min(e,f)
print(e | f) #union: max(e,f)
print(e==f)  #equality
print(e<=f)  #inclusion
