

txt_data = " I like pizza!"

file_path = r"C:\Users\27ome\OneDrive\Desktop\Python\output1.txt"

try:
    with open(file_path, "a") as file:
        #"a" for append, "w" for write, "x" for create and write(cant create if its exists)
        file.write("\n" + txt_data)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exist")




