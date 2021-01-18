# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_text=input("Введите несколько слов через пробел: ")
words=[]
number_count = 1

for element in range(user_text.count(" ") + 1):
    words = user_text.split()
    if len(str(words)) <= 10:
        print(f" {number_count} {words [element]}")
        number_count += 1
    else:
        print(f" {number_count} {words [element] [0:10]}")
        number_count += 1

