k = int(input())

possible = False
# Проверяем все возможные количества пачек по 5 шариков
for y in range(k // 5 + 1):
    remainder = k - y * 5
    if remainder >= 0 and remainder % 3 == 0:
        possible = True
        break

if possible:
    print("YES")
else:
    print("NO")