try:
    age = int(input("Enter your age: "))
    print(f"your age is {age} years")
except ValueError:
    print("Age should be a number")
