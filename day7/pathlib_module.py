#These modules are used almost everywhere in Python projects because hardcoding file paths and configuration values is a bad practice.Nowadays, pathlib is the recommended approach because it's cleaner and more readable.
from pathlib import Path

path = Path("day7") / "file1.txt"
print(path)
print(Path.cwd())  #This tells where your Python program is currently running.
print(Path.home())
print(path.exists())
print(path.is_file())
print(path.name)
print(path.suffix)
print(path.stem)
# Path("day7/Projects").mkdir()
# Path("day7/A/B/C").mkdir(parents=True, exist_ok=True)


# with open(path,"w") as f:
#     f.write("using Pthlib module")

#reading a file
path=Path("day7")/"notes.txt"
text = path.read_text()
print(text)

#writing to a file
path=Path("day7")/"new_file.txt"
path.write_text("Hello Python")
