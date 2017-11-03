#!/usr/bin/env python3

# Ввести целые M и N, вывести последовательность 0 1 2 3 4 5 6 7 8 9 0 1 2 3 … в виде спирально
# (по часовой стрелке, из верхнего левого угла) заполненной таблицы M×N.
# Не забываем про то, что M и N могут быть чётными, нечётными и неизвестно, какое больше.
# Input:
#
# 6,5
#
# Output:
#
# 0 1 2 3 4 5
# 7 8 9 0 1 6
# 6 7 8 9 2 7
# 5 6 5 4 3 8
# 4 3 2 1 0 9

# directions
Right = "right"
Left = "left"
Up = "up"
Down = "down"

unacceptable_value = -1

def rotate(direction):
    if direction == Right:
        return Down
    elif direction == Left:
        return Up
    elif direction == Up:
        return Right
    elif direction == Down:
        return Left

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def can_be_there(self, mat):
        if self.x < 0 or self.y < 0:
            return False
        if len(mat) <= self.y :
            return False
        y_coord = mat[self.y]
        if len(y_coord) <= self.x:
            return False
        return True

    def never_been_there(self, mat):
        y_coord = mat[self.y]
        return y_coord[self.x] == unacceptable_value

def step(pos, direction):
    x, y = pos.x, pos.y
    if direction == Right:
        x += 1
    elif direction == Left:
        x -= 1
    elif direction == Up:
        y -= 1
    elif direction == Down:
        y += 1
    return Position(x, y)

class Map:
    def __init__(self, mat):
        self.mat = mat
        self.pos = Position(0,0)

    def set_in_position(self, value):
        self.mat[self.pos.y][self.pos.x] = value

    def try_step(self, direction):
        new_pos = step(self.pos, direction)
        if new_pos.can_be_there(self.mat) and new_pos.never_been_there(self.mat):
            self.pos = new_pos
            return True
        else:
            return False

#digit_generator
def digits():
    digs = [i for i in range(10)]
    while True:
        for i in digs:
            yield i

def print_matrix(mat):
    for line in mat:
        print (*line)

n,m = eval(input())

mat = [ [unacceptable_value for i in range(n)] for j in range(m) ]

mapp = Map(mat)
direction = Right

for digit in digits():
    mapp.set_in_position(digit)
    success = mapp.try_step(direction)
    if not success:
        direction = rotate(direction)
        if not mapp.try_step(direction): # cann't step after channging direction
            break

print_matrix(mapp.mat)
