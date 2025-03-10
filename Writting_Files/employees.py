txt_data = " I like pizza!"

employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

file_path = r"C:\Users\27ome\OneDrive\Desktop\Python\output1.txt"

try:
    with open(file_path, "w") as file:
        for employee in employees:
            file.write(employee + "\n")
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exist")