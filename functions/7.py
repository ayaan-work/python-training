#Else on loops
# The else block runs only if the loop finishes normally (i.e., it is not terminated by break).

for i in range(5):
    print(i)
else:
    print("Loop completed")

print("\n")

count = 1

while count <= 3:
    print(count)
    count += 1
else:
    print("Finished")

print("\n")

#match statement
#similar to switch case in other languages, match statement is used to match a value against multiple cases.

day = 2

match day:
    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case _:
        print("Invalid")