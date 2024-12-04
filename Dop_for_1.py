number = int(input("Введите число  "))
index = []
for number in range (0, number):
    index.append('*')
    print(*index)
