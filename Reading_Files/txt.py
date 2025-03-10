
file_path = r"C:\Users\27ome\OneDrive\Desktop\Python\read\read1txt.txt"
try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permision to read that file")