def say_sup():
    print(f"SUP! My __name__ is {__name__}")

# when you want to prevent a block of code from running on an import
if __name__ == "__main__":
    say_sup()

# checkout the say_hi.py with and without the if statement above