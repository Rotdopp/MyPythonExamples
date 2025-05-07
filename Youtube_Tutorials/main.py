
x = 2
for i in range(0,4):
    print(x)
                # i is our counter range(0,4) initiate i from 0 to 4 and for loop increase i automaticly every single loop
print()
number = 0
while number <= 10:
    print(number)
    number += 1

List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

Dictionary = {"Germany": "Berlin",
              "Canada": "Toronto",
              "England": "London"}
print(Dictionary)
print(Dictionary["Germany"])




import time

def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1/2)
    print("DONE!!")

count(10)

def reverseCount(end=0, start=10):
    for x in range(start, end-1, -1):
        print(x)
        time.sleep(1/2)
    print("Done!!!")

reverseCount()