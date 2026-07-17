#Strings are immutable in python. This means that once a string is created, it cannot be changed. However, you can create a new string based on the original string.

chai="Masala Chai"
print(chai)

num="0123456789"
print(num[0:5]) #prints 01234
print(num[5:]) #prints 56789
print(num[:5]) #prints 01234
print(num[0:8:2]) #prints 0246
print(num[::-1]) #prints 9876543210

st1="Hello"
str2="World"
str3=st1+str2
print(str3) #prints HelloWorld

quantity=2
name="John"
print("Hello {}. You have {} new messages.".format(name, quantity)) #prints Hello John. You have 2 new messages.
print(f"Hello {name}. You have {quantity} new messages.") #prints Hello John. You have 2 new messages.

greeting="   Hello    "
print(greeting.strip()) #prints Hello

chai1="Masala Chai"
print(chai1.replace("Masala", "Ginger")) #prints Ginger Chai

chai2="Lemon,Ginger,Masala,Mint"
print(chai2.split())
print(chai2.split(",")) #prints ['Lemon', 'Ginger', 'Masala', 'Mint']

print(chai1.find("Chai")) #prints 7

#to make strings form a list, we can use the join() method. The join() method takes all items in an iterable and joins them into one string.
chai_variety=["Masala", "Ginger", "Lemon", "Mint"]
print("".join(chai_variety)) #prints MasalaGingerLemonMint
print(" ".join(chai_variety)) #prints Masala Ginger Lemon Mint
print("-".join(chai_variety)) #prints Masala-Ginger-Lemon-Mint

path="C:\\Users\\John\\Documents\\file.txt"
print(path)

path1=r"C:\Users\John\Documents\file.txt"
print(path1) #prints C:\Users\John\Documents\file.txt
