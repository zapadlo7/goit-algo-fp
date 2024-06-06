import turtle
import math


def draw_pythagoras_tree(branch_length, angle, level):
    if level == 0:
        return

    turtle.forward(branch_length)
    turtle.left(angle)

    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, angle, level - 1)

    turtle.right(2 * angle)

    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, angle, level - 1)

    turtle.left(angle)
    turtle.backward(branch_length)


if __name__ == "__main__":
    level = int(input("Введіть рівень рекурсії: "))
    branch_length = 100
    angle = 45

    turtle.speed(0)
    turtle.left(90)
    turtle.up()
    turtle.goto(0, -200)
    turtle.down()

    draw_pythagoras_tree(branch_length, angle, level)

    turtle.done()