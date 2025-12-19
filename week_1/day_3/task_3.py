n = 10

print("Counting from 1 to n (skip 5)")
for i in range(1, n + 1):
    if i == 5:
        continue

    print(i)
