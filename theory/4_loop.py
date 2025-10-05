years = [1994, 1972, 2008, 1993]

for year in years:
    year += 10

print('Результат:', years)

'''
Название фильма: Побег из Шоушенка
Название фильма: Крестный отец
Название фильма: Темный рыцарь
Название фильма: Список Шиндлера
Результат: [1994, 1972, 2008, 1993]
'''

# range

for i in range(10): 
    print('Сейчас выполняется шаг', i)

'''
Сейчас выполняется шаг 0
Сейчас выполняется шаг 1
Сейчас выполняется шаг 2
Сейчас выполняется шаг 3
Сейчас выполняется шаг 4
Сейчас выполняется шаг 5
Сейчас выполняется шаг 6
Сейчас выполняется шаг 7
Сейчас выполняется шаг 8
Сейчас выполняется шаг 9
'''

movies = ['Побег из Шоушенка', 'Крёстный отец', 'Тёмный рыцарь', 'Список Шиндлера']

for i in range(len(movies)): 
    print('Название фильма:', movies[i]) 

'''
Название фильма: Побег из Шоушенка
Название фильма: Крёстный отец
Название фильма: Тёмный рыцарь
Название фильма: Список Шиндлера
'''

prices = [1500, 2999, 7499, 3220]

for i in range(len(prices)):
    prices[i] -= 1000

print('Результат:', prices) # Результат: [500, 1999, 6499, 2220]

# calculating the amount

marks = [90, 85, 83, 92]
total = 0

for mark in marks:
    total += mark

print(total) # 350

# calculating the product

movies_duration = [142, 175, 152, 195, 201, 154, 178, 139, 133, 163, 136]

mult_duration = 1

for duration in movies_duration:
    mult_duration *= duration

print(mult_duration) # 1663161131763038875968000

# sum()

movies_duration = [142, 175, 152, 195, 201, 154, 178, 139, 133, 163, 136]
total_duration = sum(movies_duration)
print(total_duration) # 1768

# prod()

import math

movies_duration = [142, 175, 152, 195, 201, 154, 178, 139, 133, 163, 136]

mult_duration = math.prod(movies_duration)

print(mult_duration) # 1663161131763038875968000

# max and min with cycle and if

movies_duration = [142, 175, 152, 195, 201, 154, 178, 139, 133, 163, 136]

max_value = 0

for duration in movies_duration:
    if duration > max_value:
        max_value = duration

print(max_value) # 201

# max()

movies_duration = [142, 175, 152, 195, 201, 154, 178, 139, 133, 163, 136]
max_duration = max(movies_duration)
print (max_duration) # 201

# min()

movies_duration = [142, 175, 152, 195, 201, 154, 178, 139, 133, 163, 136]
min_duration = min(movies_duration)
print(min_duration) # 133

# square elements in the list

sides = [2, 10, 20, 3]

squares = [] 

for side in sides: 
    squares.append(side ** 2) 

print('Результат:', squares) # Результат: [4, 100, 400, 9]

# square elements in the list with range

sides = [2, 10, 20, 3]

for i in range(len(sides)): 
    sides[i] = sides[i] ** 2

print('Результат:', sides) # [4, 100, 400, 9]

# factorial 5! = 1 * 2 * 3 * 4 * 5 = 120  

number = 8 

fact = 1 

for i in range(1, number + 1): 
    fact *= i 

print(fact) # 40320 

# math.factorial()

print(math.factorial(8)) # 40320 