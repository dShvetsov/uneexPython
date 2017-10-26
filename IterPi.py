#!/usr/bin/env python3

# Пользуясь формулой Лейбница для вычисления числа Пи.
# Написать бесконечный генератор pigen(), возвращающий последовательно 4, 4-4/3, 4-4/3+4/5, …;
# ввести некоторое расстояние E и вывести номер элемента этой последовательности,
# первым попадающего в E/2-окрестность числа Пи.
# Внимание! Тесты написаны из расчёта, что проверка такая:
# как только очередное значение pigen() по модулю перестанет отличаться от предыдущего
# значения больше, чем на E, выводим, на каком обороте цикла это произошло.
# Input:
#
# 0.001
#
# Output:
#
# 2000

def IterPi():
    pi = 0
    denominator = 1
    sign = +1
    factor = 4
    while True :
        pi += sign * (1 / denominator)
        yield pi * factor
        sign *= -1
        denominator += 2


epsilon = eval(input())

iter_pi = IterPi()
last_pi = 0

for step_count, i_pi in enumerate(iter_pi):
    if abs(i_pi - last_pi) < epsilon :
        print (step_count)
        break
    last_pi = i_pi
