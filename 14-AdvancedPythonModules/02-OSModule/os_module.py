f = open('practice.txt', 'w+')
f.write("This is a test string")
f.close()

import os
print(os.getcwd())
print("-----------------")
print(os.listdir())
print("-----------------")
print(os.listdir("C:\\Users"))
print("-----------------")

import shutil

 shutil.move('.\\14-AdvancedPythonModules\\02-OSModule', 'C:\\Users\\jamescox')

import send2trash

send2trash.send2trash('practice.txt')

file_path = os.getcwd() + "\\Example_Top_Level"

for (folder, sub_folders, files) in os.walk(file_path):
    print(f"Currently looking at {folder}")
    print("\n")
    
    print("The subfolders are :")
    for sub_folder in sub_folders:
        print(f"\tSubfolder:{sub_folder}")

    print("\n")
    print("The files are: ")
    for f in files:
        print(f"\tFile: {f}")
    print("\n")