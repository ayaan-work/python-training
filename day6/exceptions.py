try:
    a=int(input("enter a number: "))
    print(a)

except Exception as e:
    print(e)


print("Thank You!")

print("\n")

a=int(input("enter a number"))
b=int(input("enter another number"))
if(b==0):          # we can raise our own error to let others know that they are doing a mistake
    raise ZeroDivisionError("you cannot divide by zero")
else:
    print(f"The division of a/b is {a/b}")

print("\n")

   


