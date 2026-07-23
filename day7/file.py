#File I/O

f=open("day7/file.txt")   #the default mode is read "r"
data=f.read()
print(data)
f.close()