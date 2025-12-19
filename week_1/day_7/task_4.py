try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise ValueError("No negative number")

    print(num)
except ValueError as e:
    print(f"Error: {e}")
