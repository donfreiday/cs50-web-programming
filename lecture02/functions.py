def square(x):
    return x*x

# wrap functionality in main() so square() can be imported without executing the test code
def main():
    for i in range(10):
        print("{} squared is {}".format(i, square(i)))

    # Equivalent, Python 3.6+ version
    for i in range(10):
        print(f"{i} squared is {square(i)}")

# if this is the file being executed
if __name__ == "__main__":
    main()