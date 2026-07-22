#try-else
#else block will only run when the try block runs successfully

try:
    a=int(input("enter a number: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("this is else") 