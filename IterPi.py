#!/usr/bin/env python3

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
