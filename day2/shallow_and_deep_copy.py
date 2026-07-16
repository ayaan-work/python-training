lst1=[1,2,3,4,5]
lst2=lst1
print(lst1)
print(lst2)
lst2[0]=100
print(lst1)
print(lst2)

print("\n")

#shallow copy

lst3=[1,2,3,4,5]
lst4=lst3.copy() #shallow copy of lst3
print(lst3)
print(lst4)
lst4[0]=100
print(lst3)
print(lst4) 

lst5=[[1,2,3],[4,5,6]]
lst6=lst5.copy() #shallow copy of lst5
print(lst5)
print(lst6)
lst6[0][0]=100
print(lst5)
print(lst6)

lst5.append([7,8,9])
print(lst5)

print("\n")

#deep copy
import copy
lst7=[[1,2,3],[4,5,6]]
lst8=copy.deepcopy(lst7) #deep copy of lst7
print(lst7)
print(lst8)
lst8[0][0]=100
print(lst7)
print(lst8)
