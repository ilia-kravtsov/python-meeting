# len

favorite_character = 'Tommy_Shelby'
print(len(favorite_character))

# concatenation

phrase1 = 'Я люблю '
phrase2 = 'складывать '
phrase3 = 'строки!'
print(phrase1 + phrase2 + phrase3) # Я люблю складывать строки!

# multiplying strings

print('lol' * 5) # lollollollollol
print(3 * 'ha') # hahaha

# upper

word = 'hello'

new_word = word.upper()
print(new_word) # HELLO

# replace

some_string = 'leaving'
print(some_string) # leaving
some_string = some_string.replace('leav', 'stay') 
print(some_string) # staying

# find

word = 'hey, hello, hello, hello, how low?'
ind = word.find('hello')
print(ind) # 5

# lower

word = 'AbRacaDABRA'
lower_word = word.lower()
print(lower_word) # abracadabra

# f strings

name = 'John'
age = 30
height = 173.5

introduction = f'Hello, this is {name}, he is {age}, his height is {height}'
print(introduction) # Hello, this is John, he is 30, his height is 173.5
print(type(introduction)) # <class 'str'>