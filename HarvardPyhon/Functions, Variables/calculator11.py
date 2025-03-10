# Demonstrates defining a function with a return value


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    # return n * n
    # return pow(n, 2)
    return n ** 2

main()
