# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

new_list=[1984,7.7, False, None, "Привет", -2021, [2134,234]]

def check_type(i):
    for i in range(len(new_list)):
        print(new_list[i],type(new_list[i]))

check_type(new_list)
