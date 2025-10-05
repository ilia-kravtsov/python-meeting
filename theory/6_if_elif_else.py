# bool

print(10 != 10) # False
print(777 > 7) # True
print('ac' > 'ab') # True
print(120.5 >= 20.7) # True
print('hellO'.islower()) # False
print('777i'.isdigit()) # False
print('здесьестпробелызнакипрепинания'.isalpha()) # True

# conditional operator

weather = 'дождь'

if weather == 'дождь':
    print('взять зонт')

# conditional branching

weather = 'солнце'

if weather == 'дождь':
    print('взять зонт')
else:
    print('помыть машину')

# task

movie_rating = 8.73 

if movie_rating >= 8.5:
    print('Высокий рейтинг')
else:
    print('Обычный рейтинг')

# task

movie_info = ['Бойцовский клуб', 'США', 1999, 'триллер, драма, криминал', 139, 8.644]

if movie_info[2] > 2000:
    print('Да')
else:
    print('Нет')

# task

time = 'день'

if time == 'утро':
    print('завтрак')
elif time == 'день':
    print('обед')
elif time == 'вечер':
    print('ужин')

# task

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1979, 1985]

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1979, 1985]

for year in years:
    if 1960 <= year <= 1969:
        print('Фильм вышел в шестидесятые.')
    elif 1970 <= year <= 1979:
        print('Фильм вышел в семидесятые.')
    elif 1980 <= year <= 1989:
        print('Фильм вышел в восьмидесятые.')
    elif 1990 <= year <= 1999:
        print('Фильм вышел в девяностые.')
    elif 2000 <= year <= 2009:
        print('Фильм вышел в нулевые.')
    else:
        print('Эпоха не определена')

# task

marks = [91, 35, 65, 89, 78, 93]

for mark in marks:
    if 0 <= mark <= 59:
        print(2)
    elif 60 <= mark <= 72:
        print(3)
    elif 73 <= mark <= 84:
        print(4)
    elif 85 <= mark <= 100:
        print(5)

# task

countries = ['СССР', 'Новая Зеландия', 'Италия', 'Италия', 'СССР', 'США']

for country in countries:
    if country == 'СССР':
        print('Фильм вышел в СССР.')
    elif country == 'США':
        print('The movie was released in USA.')
    elif country == 'Италия':
        print('Il film e stato rilasciato in Italia.')
    else:
        print('Страна не определена.')