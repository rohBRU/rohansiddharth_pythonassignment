numbers = [10, 23, 45, 12, 55, 30, 8]

for num in numbers:
    if num > 50:
        break
    if num % 5 == 0:
        continue
    print(num)
