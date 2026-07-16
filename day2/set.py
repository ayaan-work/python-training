#set in python is an unordered collection of unique elements. It is mutable and can be changed after creation. Sets are defined using curly braces {} or the set() function.

set1={1,2,3,4,5}
print(set1)

set2=set() #creating an empty set

set3={1,2,3,4,5,"hello","world",26.5} #set can contain elements of different data types
print(set3,type(set3))

set1.add(6) #adding new element to the set
print(set1)

set1.remove(3) #removing an element from the set (gives error if the element is not present in the set)
print(set1) 

print(set1.union(set3)) #returning a new set which is the union of two sets
print(set1.intersection(set3)) #returning a new set which is the intersection of two sets

#Note-- we cannot update the value of an element in a set as it is unordered and does not have any index. We can only add or remove elements from a set.
