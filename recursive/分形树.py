# coding: utf-8
'''
用递归算法画一颗具有分形性质的树

'''
import turtle


def draw_a_tree(point=(0, 20), angle=90.0, start_len=72.0, stop_len=5.0, turn_angle=30):
    if start_len < stop_len:
        return

    right_angle, left_angle, next_len = angle - turn_angle, angle + turn_angle, start_len * 0.65
    tree.goto(*point)
    tree.setheading(right_angle)
    tree.forward(start_len)
    draw_a_tree(tree.pos(), right_angle, next_len)

    tree.penup()
    tree.goto(*point)
    tree.pendown()
    tree.setheading(left_angle)
    tree.forward(start_len)
    draw_a_tree(tree.pos(), left_angle, next_len)


tree = turtle.Turtle()
tree.pencolor('green')
tree.pensize(2)
tree.goto(0, -100)
tree.setheading(90)
tree.forward(120)
draw_a_tree()
tree.hideturtle()
turtle.done()
