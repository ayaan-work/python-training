def main():
    try:
        a=int(input("enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("this is finally block")

main()         

#real use finally block comes in functions, finally will run even if the statement return is present in both try and except block, finally overwrites that and will run
# if we remove finally from function then the program will exit from the return statement of try or except. 