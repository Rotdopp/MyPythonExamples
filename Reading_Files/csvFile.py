import csv

file_path = r"C:\Users\27ome\OneDrive\Desktop\Python\read\output3.csv"
try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permision to read that file")