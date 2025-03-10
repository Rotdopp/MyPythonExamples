my_list = [1, 2, "Hello", 4, 5] # Ordered, mutable, allows duplicates

my_tuple = (1, 2, "Hello", 4, 7) # Ordered, immutable, allows duplicates

my_set = {1, 2, "Hello", 4, 5} # Unordered, mutable, unique elements

my_dict = {'a': "Hello", 'b': 2, 'c': 3} # Key-value pairs, mutable

print(my_list)
print(my_tuple)
print(my_set)
print(my_dict)
print("--------my_list---------")

print(my_list[2])
print(my_list[3])
my_list.append("Hello World")
print(my_list)
my_list.pop()
print(my_list)
print("------my_tuple-----------")

print(my_tuple[1])
print(my_tuple[2])
# can't change anything once you declare it
print("---------my_set--------")

my_set.add("Welcome")
print(my_set.pop())
print(my_set.union(my_tuple))  # perform union with set and tuple
print(my_set)
print("-------my_dict----------")

print(my_dict.get('a'))
print(my_dict.get('b'))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.fromkeys())
