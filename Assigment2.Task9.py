a = int(input())
b = int(input())
c = int(input())
d = int(input())

# Если числитель равен нулю тождественно
if a == 0 and b == 0:
    print("INF")
elif a == 0:
    # Числитель — константа (b != 0), дробь равна 0 быть не может
    print("NO")
elif -b % a != 0:
    # Корень не является целым числом
    print("NO")
else:
    x = -b // a
    # Проверяем, чтобы знаменатель не обратная в ноль точка
    if c * x + d == 0:
        print("NO")
    else:
        print(x)