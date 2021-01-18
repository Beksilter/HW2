# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

#Списки (словари) через list и dict
seasons_dict = {
    1 : "Зима",
    2 : "Весна",
    3 : "Лето",
    4 : "Осень"
}
seasons_list = ["Зима", "Весна", "Лето", "Осень"]

month = int(input("Введите номер месяца: "))

if month in (1,2,12):
    print(seasons_dict.get(1))
    print(seasons_list[0])

elif month in (3,4,5):
    print(seasons_dict.get(2))
    print(seasons_list[1])

elif month in (6,7,8):
    print(seasons_dict.get(3))
    print(seasons_list[2])

elif month in (9,10,11):
    print(seasons_dict.get(4))
    print(seasons_list[3])

else:
    print("Такого месяца не бывает. Попробуйте снова.")