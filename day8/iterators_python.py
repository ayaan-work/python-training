# The Iterator Protocol is the mechanism Python uses to loop over objects (like lists, tuples, strings, files, etc.). It is built around two functions:

# iter() → gets an iterator from an iterable.
# next() → gets the next item from the iterator.
#iterator remembers its position
#By default, iterating over a dictionary gives you its keys.
#files are iterators

numbers = [10, 20, 30]

it = iter(numbers)

print(it)
print(next(it))
print(next(it))
print(next(it))
# print(next(it))   #StopIterator error is raised

#when we use for for loop pyhton inernally does this
# it = iter(numbers)

# while True:
#     try:
#         item = next(it)
#         print(item)
#     except StopIteration:
#         break


#Creating our own iterator
import random
class Dice:

    def __init__(self,rolls):
        self.rolls=rolls
        self.count=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count<self.rolls:
            self.count+=1
            return random.randint(1,6)
        else:
            raise StopIteration

# dice=Dice(3)
# for die in dice:
#     print(die)

dice=list(Dice(3))
print(dice)

class Count:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 5:
            value = self.num
            self.num += 1
            return value
        raise StopIteration

counter = Count()

for i in counter:
    print(i)
    