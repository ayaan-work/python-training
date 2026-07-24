#context manager with class
class Demo:

    def __enter__(self):
        print("Entering")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")

with Demo():
    print("I am Demo Class")

print("\n")
#craeting a custom context manager

class Database:

    def __enter__(self):
        print("Connecting")
        return self

    def query(self):
        print("Running Query")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing Connection")

with Database as db:
    db.query()

#context manager with function
#Python provides the contextlib.contextmanager decorator to create context managers using a generator.
from contextlib import contextmanager

@contextmanager
def my_context():

    print("Enter")

    yield

    print("Exit")

with my_context():
    print("Inside")

# How yield Works Here
# Everything before yield acts like __enter__().
# Everything after yield acts like __exit__().