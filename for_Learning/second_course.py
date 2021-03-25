#1.2 Модель данных: объекты

objects = [1, 2, 1, 2, 3]
ans = 0
total = []
for obj in objects: # доступная переменная objects
    if obj not in total:
        total.append(obj)
        ans += 1
print(ans)