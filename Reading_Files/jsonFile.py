import json

file_path = r"C:\Users\27ome\OneDrive\Desktop\Python\read\output2.json"
try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permision to read that file")