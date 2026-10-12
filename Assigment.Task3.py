r1, c1, r2, c2 = map(int, input().split())
if abs(r1 - r2) == abs(c1 - c2):
    print("YES")
else:
    print("NO")