import os

file_path = r"C:\Users\27ome\OneDrive\Desktop\Yeni Yılda Yapılcaklar"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")

    elif os.path.isdir(file_path):
        print("That is a directory")

else:
    print(f"The location '{file_path}' does not exist")
