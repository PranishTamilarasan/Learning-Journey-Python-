import subprocess
from sys import stdout

p1 = subprocess.run(
    "dir", shell=True, capture_output=True
)  # Print current directory List

print(p1)  # CompletedProcess(args='dir', returncode=0)
print(
    p1.stdout
)  # stdout is to print captured output. To capture we use capture_output. It stores in bytes
print(p1.stdout.decode())  # To convert bytes to strings or use 'text = True' in line 4
print(p1.args)  # prints the argument we used. i,e in this case "dir"
print(p1.returncode)  # Return error count
print(
    p1.stderr
)  # To display the error, In default python don't throw error if external cmd fails.


# To avoid error
p1 = subprocess.run("dir", stderr=subprocess.DEVNULL)


# To redirect output in a file
with open("output.txt", "w") as f:
    p1 = subprocess.run("dir", stdout=f, text=True)
