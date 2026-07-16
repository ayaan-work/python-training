# tuple are immutable data structures in python which means we cannot change the values of tuple once it is created. Tuples are defined using parentheses () and can contain elements of different data types.
tuple1=(1,2,3,4,5)
print(tuple1)

tuple2=() #empty tuple
tuple3=(1,) #tuple with single element
print(tuple3)

tuple4=(1,2,3,4,5,6,7,8,9,10)
print(tuple4[0:5]) #slicing the tuple from index 0 to 4

tuple5=tuple1+tuple4 #concatenating two tuples
print(tuple5)

tuple6=tuple1*3 #repeating the tuple 3 times
print(tuple6)

tuple1.count(1) #counting the number of occurrences of an element in the tuple

tuple1.index(3) #finding the index of an element in the tuple