#A Command-Line Interface (CLI) lets users pass information when running a program.
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("number1",help="number1")  #parser.add_argument("--number1",help="number1")
parser.add_argument("number2",help="number2")  # for optional argument we use -- in front of the argument
parser.add_argument("operation",help="operation",choices=["add","subtract","multiply"]) 
args = parser.parse_args()
# print(args.number1)
# print(args.number2)             #python argparse_python.py --number1 10 --number2 20 --operation multiply
# print(args.operation)           #if we use optional argument then we run our code like this
n1=int(args.number1)
n2=int(args.number2)
result=None
if args.operation=="add":
    result=n1+n2
elif args.operation=="subtract":
    result=n1-n2
elif args.operation=="multiply":
    result=n1*n2


print(f"Result: {result}")

