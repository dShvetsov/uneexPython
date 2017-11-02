#!/usr/bin/env python3

# Написать генератор цифр последовательности Конвея «Look and Say».
# Ввести N⩾0 и вывести N-ю цифру последовательности.
# Input:
#
# 100500
#
# Output:
#
# 2

from collections import deque

def looksaydigit():
    # Becouse 0 is never there in looksay sequance
    # we will be used it for dividing numbers
    deq = deque([1, 0])
    current_number = 1
    count_of_number = 0
    while True :
        number = deq.popleft()
        if number != 0 :
            yield number

        if number == current_number :
            count_of_number += 1
        else:
            if current_number != 0:
                deq.append(count_of_number)
            deq.append(current_number)
            count_of_number = 1
            current_number = number



n = eval(input())
looksay = looksaydigit()
for i, v in enumerate(looksay):
    if i == n :
        print (v)
        break

