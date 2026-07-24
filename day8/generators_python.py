# Generators are one of Python's most powerful features. They let you produce values one at a time, instead of creating and storing all values in memory at once. This is called lazy evaluation.
#A generator is a special kind of function that uses the yield keyword instead of return.
#Instead of returning all values at once, it pauses after producing each value and resumes from where it left off when asked for the next one.

def numbers():
    return [1, 2, 3]
nums = numbers()
print(nums)
#The entire list is created in memory before it is returned.

def numbers():
    yield 1
    yield 2
    yield 3

gen = numbers()

print(next(gen))
print(next(gen))
print(next(gen))
#Every call to next() continues execution until the next yield.
#yield pauses execution instead of ending the function.
print("\n")

#The for loop automatically calls next() until StopIteration is raised.
for num in numbers():
    print(num)

#Generators can produce values forever.
#Without generators, an infinite list would be impossible because it would never finish creating.
def infinite():
    num = 1

    while True:
        yield num
        num += 1

g = infinite()
print(next(g))
print(next(g))
print(next(g))

#generator expressions (use paranthesis instead of square bracket)
nums = (x * x for x in range(5))
print(nums)
for n in nums:
    print(n)

# Use generators when:

# Processing very large files.
# Working with large datasets.
# Streaming data from APIs or sensors.
# Creating infinite sequences.
# Chaining data-processing pipelines.
# You only need to iterate once.

# Use lists when:

# You need random access (nums[5]).
# You need to iterate multiple times over the same data.
# The dataset is small enough to fit comfortably in memory.