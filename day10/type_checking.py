# mypy is a type checking module in python which checks that all the type-hints in our code are correct. 
def add(a: int, b: int) -> int:
    return a+b

print(add(5,5))

def average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)

scores = [80, 90, 100]

print(average(scores))