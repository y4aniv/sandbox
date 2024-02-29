sqrt = {}

for i in range(1, 31):
    sqrt[i] = round(i ** 0.5, 3)

print(sqrt)

sqrt.clear()
print("")

for i in range(1, 31):
    if i % 3 == 0:
        sqrt[i] = round(i ** 0.5, 3)
print(sqrt)