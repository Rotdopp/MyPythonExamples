import json

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}


file_path = r"C:\Users\27ome\OneDrive\Desktop\Python\output2.json"

try:
    with open(file_path, "w") as file:
        json.dump(employee, file, indent=4)
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("That file already exist")