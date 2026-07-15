def solve(a,b,c):    #function definition
    if a>b and a>c:
        print(a, "is the largest number")
    elif b>a and b>c:
        print(b, "is the largest number")
    else:
        print(c, "is the largest number")   


solve(10, 20, 30)          #function call  