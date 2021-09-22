data = dict()
number = int(input('Сколько стран: '))

for counter in range(number):
    name = input('Название страны: ')
population = int(input('Население: '))
data[name] = population

sorted_data = sorted(data.items(), key=lambda x: x[1])
for name, population in sorted_data[::-1]:
    print(name, population)