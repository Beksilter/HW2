# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
number = (input(f"\033[31mНаберите 'end' для выхода  \n\033[37mВведите новый элемент рейтинга: "))
while number != "end":
    for element in range(len(my_list)):
        if my_list[element] == int(number):
            my_list.insert(element + 1, int(number))
            break
        elif my_list[0] < int(number):
            my_list.insert(0, int(number))
        elif my_list[-1] > int(number):
            my_list.append(int(number))
        elif my_list[element] > int(number) and my_list[element + 1] < int(number):
            my_list.insert(element + 1, int(number))
    print(f"текущий список - {my_list}")
    number = (input(f"Введите новый элемент рейтинга:"))
print(f"текущий список - {my_list}")