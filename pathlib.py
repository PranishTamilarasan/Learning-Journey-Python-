# ------------- /* PATHS */ -----------------------------
from pathlib import Path

path = Path(r"D:\Resume.docx")

print(path)         #D:\Resume.docx
print(repr(path))   #WindowsPath('D:/Resume.docx')
print(path.stem)    #Resume
print(path.suffix)  #.docx
print(path.parent)  #D:\

#Creating New Path
new_path = path.parent / (path.stem + "_newPath.docx")
print(repr(new_path))   #WindowsPath('D:/Resume_newPath.docx')

#Read All txt files in desktop
desktop = Path.home() / "Desktop"

files = list(desktop.rglob("*.txt")) #Search recursively - inside all folders in desktop

for it in files:
    print(it)

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#-------------- /* JSON */ ----------------------

import json

json_str = '''
    {
        "students" : [
            {
                "id" : 1,
                "name" : "pranish",
                "age" : 18
            },
            {
                "id" : 2,
                "name" : "Bot",
                "age" : 20
            }
        ]
    }
'''

data = json.loads(json_str) #Converts string to json
print(data)

data['Test'] = True

new_json = json.dumps(data, indent=2) #converts json to string with intendation as 2
print(new_json)

#Open and read a file
with open("File_Name.json", "r") as f:
    data = json.load(f)     #Why Not 'S' is because, we are loading a file here

print(data)

#Write to a file
with open("File_Name.json", "w") as f:
    data = json.dump(data, f)

#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
