n = 10

nums = list(range(1, n + 1))
even_squares = [num**2 for num in nums if num % 2 == 0]

print(even_squares)
