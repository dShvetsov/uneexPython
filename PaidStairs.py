#!/usr/bin/env python3

stairs = eval(input())

# we can reach 0 and 1 stair for one step
paid_to_stair = [stairs[0], stairs[1]]

for stair_cost in stairs[2:] :
    added_value = stair_cost + min(paid_to_stair[-1], paid_to_stair[-2])
    paid_to_stair.append(added_value)

print(paid_to_stair[-1])
