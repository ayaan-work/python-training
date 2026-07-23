#The os module lets Python interact with the operating system.
import os

print(os.getcwd())
# os.chdir("Documents")
print(os.listdir())
print(os.listdir("Documents"))
# os.mkdir("Projects")
# os.makedirs("A/B/C")
# os.rename("old.txt", "new.txt")
# os.remove("notes.txt")
# os.rmdir("Projects")
# os.removedirs("A/B/C")
print(os.path.exists("notes.txt"))
# os.path.join("folder", "file.txt")
# print(os.path.abspath("notes.txt"))