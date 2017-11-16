#!/usr/bin/env python3

# Ввести произвольную последовательность (не обязательно кортеж) натуральных чисел, не превышающих 1000000.
# Вывести, сколько среди них различных чисел, являющихся суммой трёх квадратов.
#
#     Пояснение. Поскольку входная последовательность обрабатывается eval(), она может быть, например, такой:
#                                                     (1+i%10 for i in range(100000)), в этом случае ответ — тоже 3 :)
#
# 3, 4, 2, 9, 1, 5, 6, 7, 8, 3, 6
#
# 3

from math import sqrt, ceil


if __name__ == "__main__":
    sequance = set(eval(input()))
    max_number = max(sequance)
    term1 = (i ** 2 for i in range(1, ceil(sqrt(max_number))) )
    term2 = lambda x: (i ** 2 for i in range(round(sqrt(x)), ceil(sqrt(max_number - x))))
    term3 = lambda x, y: (i ** 2 for i in range(round(sqrt(y)), ceil(sqrt(max_number - x - y)) + 1))

    squares = {i + j + k for i in term1 for j in term2(i) for k in term3(i, j)}
    result = squares & sequance
    print(len(result))
