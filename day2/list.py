#list are mutable in python which means we can change the values of list after creating it
arr=["hello",1,36.7,True]
print(arr)

arr[1]=60
print(arr)

print(arr[0:3]) #slicing the list from index 0 to 2

arr.append("apple") #adding new element to the list
print(arr)

l1=[1,2,3,4,5]
l1.sort() #sorting the list in ascending order
arr2=sorted(l1) #sorting the list in ascending order and returning a new list
print(arr2)

print(arr.pop(3)) #removing the element at index 3 from the list and returning it
print(arr)

arr.insert(1,"banana") #inserting new element at index 1
print(arr)

l=input("Enter the list elements separated by space: ").split() #taking input from user and converting it into list (but the element inside the list will be of string type)
print(l)
print(type(l[1]))

arr2=list(map(int,input("enter numbers: ").split()))
print(arr2)