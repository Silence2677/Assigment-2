k = int(input())
m = int(input())
n = int(input())

if n <= k:
    print(2 * m)
else:
    total_sides = 2 * n
    batches = (total_sides + k - 1) // k
    print(batches * m)