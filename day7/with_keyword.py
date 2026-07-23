#this is an example of with keyword

f=open("day7/file.txt")
data=f.read()
print(data)
f.close()

print("\n")
#the same can be written as:


with open("day7/file.txt") as f:
    print(f.read())







    



