import os

print(dir(os))  # Prints all possible attributes and methods to perform

print(os.getcwd())  # To print current working directory
print(os.listdir())  # To print files in the directory

os.chdir("D:\PROJECTS (PRANISH)\Leaarning Path")  # To change directory

# To create New Directory - 2 different methods
os.mkdir("new_file")  # Just creates a single lvl dir
os.makedirs("new_file")  # create a multi-lvl dir (i.e, new_file/new_file1)

os.rmdir("new_file")  # To remove dir
os.removedirs("new_file")  # To remove multi-lvl dir

# ---------------------------------------------------------------

os.rename("test.txt", "demo.txt")  # To change name (test.txt is real name)

print(os.stat("demo.txt"))  # To print info of the file

# ===================================================================
# Work on environment variable

print(os.environ.get("prani"))  # It prints user environment variable

# If need to create a new file with environment variable in the specified dir
file_path = os.path.join(os.environ.get("prani"), "text.txt")

print(os.path.basename("/temp/test.txt"))  # print the specified file base name
print(os.path.dirname("/temp/test.txt"))  # Print dir name
print(
    os.path.split("/temp/test.txt")
)  # It gives both dir and base. o/p : ("/temp/", "test.txt")

print(os.path.exists("/temp/test.txt"))  # To check wether the path exits or not
print(os.path.splitext("/temp/test.txt"))  # o/p : ("/temp/test", ".txt")

print(dir(os.path))  # Prints all possible paths to work
