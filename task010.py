# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

eagleqty = int(input("Количество монеток. Орел:  "))
tailsqty = int(input("Количество монеток. Решка:  "))

if eagleqty < tailsqty:
    print(f"Необходимо перевернуть {eagleqty} монеток")
elif eagleqty == tailsqty:
    print (f"Необходимо перевернуть {eagleqty} монеток")
elif eagleqty > tailsqty:
    print(f"Необходимо перевернуть {tailsqty} монеток")