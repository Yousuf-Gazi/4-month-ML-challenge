x = 20

try:
    num = int(input("Enter a number: "))
    print(num / x)
except ZeroDivisionError:
    print("cant divide a number by zero")
except ValueError:
    print("must be an integer number")
finally:
    print("Execution Complete")
