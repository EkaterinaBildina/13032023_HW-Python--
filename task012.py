# Задача 12: Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

sum_of_numbers = int(input("Сумма чисел S =  "))
multiplication_of_numbers = int(input("Произведение чисел P =  "))
if sum_of_numbers <= 1000 and multiplication_of_numbers <=1000:
    for i in range(sum_of_numbers):
        for j in range(multiplication_of_numbers):
            if sum_of_numbers == i + j and multiplication_of_numbers == i * j:
                print(i, j)
else:
    print("Проверьте корректномть ввода данных")