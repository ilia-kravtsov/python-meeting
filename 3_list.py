# %%

# list

my_list = [1, 2, 3, "hello", True]

# create list using list()

# my_list_2 = list([1, 2, 3])  # из другого списка
# print(my_list_2) # [1, 2, 3]
# my_list_3 = list("abc")      # из строки → ['a', 'b', 'c']
# print(my_list_3) # ['a', 'b', 'c']
# my_list_4 = list(range(5))   # из диапазона → [0, 1, 2, 3, 4]
# print(my_list_4) # [0, 1, 2, 3, 4]

# indexes

first_row = ['Побег из Шоушенка', 'США', 1994, 'драма', 142, 9.111]
print(first_row[0], first_row[1], first_row[-1]) # Побег из Шоушенка США 9.111

# slices

first_row = ['Побег из Шоушенка', 'США', 1994, 'драма', 142, 9.111]
# from first to third
print(first_row[1:4]) # ['США', 1994, 'драма']
# from zero to second
print(first_row[:3]) # ['Побег из Шоушенка', 'США', 1994]
# from second to last
print(first_row[2:]) # [1994, 'драма', 142, 9.111]

# len() — list length

first_row_2 = ['Побег из Шоушенка', 'США', 1994, 'драма', 142, 9.111]
print(len(first_row_2)) # 6

# append() — adds one element to the end of the list

first_row_3 = ['Побег из Шоушенка', 'США', 1994, 'драма', 142, 9.111]
first_row_3.append('Фрэнк Дарабонт')
print(first_row_3) # ['Побег из Шоушенка', 'США', 1994, 'драма', 142, 9.111, 'Фрэнк Дарабонт']

# extend() — adds several elements to the end of the list

second_row = ['Крёстный отец', 'США', 1972]
second_row.extend(['Фрэнсис Форд Коппола', 'Нино Рота'])
print(second_row) # ['Крёстный отец', 'США', 1972, 'Фрэнсис Форд Коппола', 'Нино Рота']

# insert() — adds one element at a specified index in the list

dark_knight_movie = ['Тёмный рыцарь', 'США', 'фантастика, боевик, триллер', 152]
dark_knight_movie.insert(2, 2008)
print(dark_knight_movie) # ['Тёмный рыцарь', 'США', 2008, 'фантастика, боевик, триллер', 152]

# insert() — is able to add a new element at the end of the list, but why?

dark_knight_movie = ['Тёмный рыцарь', 'США', 'фантастика, боевик, триллер', 152, 8.499]
dark_knight_movie.insert(len(dark_knight_movie), 'Кристофер Нолан')
print(dark_knight_movie) # ['Тёмный рыцарь', 'США', 'фантастика, боевик, триллер', 152, 8.499, 'Кристофер Нолан']

# pop()

movies = ['Матрица', 'Матрица-2', 'Матрица-3']
movies.pop()
print(movies) # ['Матрица', 'Матрица-2']

# summation lists

second_row = ['Крёстный отец', 'США', 1972, 'драма, криминал', 175, 8.730]
extra_info = [9.20, 'Фрэнсис Форд Коппола', 'Нино Рота']
updated_row = second_row + extra_info
print(updated_row) # ['Крёстный отец', 'США', 1972, 'драма, криминал', 175, 8.73, 9.2, 'Фрэнсис Форд Коппола', 'Нино Рота']

# multiplying lists

list =['умножь', 'меня']
list = list * 2
print(list) # ['умножь', 'меня', 'умножь', 'меня']

zeros = [0] * 100
print(zeros) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# sort

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1979, 1985] 

years.sort()
print(years) # [1962, 1966, 1972, 1979, 1985, 1993, 1994, 1994, 1999, 2003, 2008]
years.sort(reverse=True) 
print(years) # [2008, 2003, 1999, 1994, 1994, 1993, 1985, 1979, 1972, 1966, 1962]

# sorted — return a new list

years_sorted = sorted(years)
print(years_sorted) # [1962, 1966, 1972, 1979, 1985, 1993, 1994, 1994, 1999, 2003, 2008]
years_sorted = sorted(years, reverse=True)
print(years_sorted) # [2008, 2003, 1999, 1994, 1994, 1993, 1985, 1979, 1972, 1966, 1962]

# index

beatles = ['Джон Леннон', 'Пол Маккартни', 'Ринго Старр', 'Джордж Харрисон']
ind = beatles.index('Пол Маккартни')
print(ind) # 1

# split

phrase = 'Ку-ку, ку-ку, ку-ку, ку-ку.'
res = phrase.split() # res will contain a list of strings, but the original phrase string will remain unchanged.
print(res) # ['Ку-ку,', 'ку-ку,', 'ку-ку,', 'ку-ку.']
print(len(res)) # 4
res = phrase.split('-') # передаём методу строку-разделитель
print(res) # ['Ку', 'ку, ку', 'ку, ку', 'ку, ку', 'ку.']
phrase = 'Aladdin#Esmeralda#Hercules#Mulan'
words = phrase.split('#') 
print(words) # ['Aladdin', 'Esmeralda', 'Hercules', 'Mulan']

# join

words = ['Поезд', 'отправляется', 'с', 'первой', 'платформы', 'в', '16:00']
phrase = ' '.join(words) # forming a string from the words list items connected by a space
print(phrase) # Поезд отправляется с первой платформы в 16:00