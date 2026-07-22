#A custom exception makes the error more meaningful.
class InsufficientBalanceError(Exception):
    pass

balance = 1000
withdraw = 1500

try:
    if withdraw > balance:
        raise InsufficientBalanceError("Not enough balance.")

except InsufficientBalanceError as e:
    print(e)

print("\n")    

#Exception chaining
try:
    int("abc")
except ValueError as e:
    raise RuntimeError("Conversion failed.") from e