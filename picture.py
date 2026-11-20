from turtle import *

cube_count = int(input('Sisesta kuubikute arv: '))

for n in range(cube_count):
    for i in range(4):
        forward(100)
        left(90)
    n += 1
    right(45)
    forward(50)

done()