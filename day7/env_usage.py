import os

print(os.getenv("USERNAME"))
print(os.getenv("USERNAME", "Guest"))

# os.environ["CITY"] = "Delhi"
# print(os.environ["CITY"])

#this uses the global environment that is set up for this machine if we want to use our own specific .env file then we have to install the python-dotenv module by running pip install python-dotenv and then use the same module for using our own specific .env file