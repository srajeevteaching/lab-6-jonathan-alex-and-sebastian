# Programmers: Jonathan, Alex, Sebastian
# Course: CS151, Dr. Rajeev
# Date: October 21st, 2021
# Lab Number: 6
# Program Inputs:
# Program Outputs:

from graphicsCS151 import *
from graphics import *
import random


def make_circle(x, y, radius):
    circle = Circle(Point(x, y), radius)
    circle.setFill("red")
    circle.setOutline("black")
    return circle


def find_x(min, max, message):
    initial = False
    return_statement = None

    while not initial:
        print("Please enter a number between " + str(min) + " and " + str(max))
        message = input(message)

        while not message.isdigit():
            print("Please re-enter a number: ")
            message = input(message)

        message = int(message)
        initial = message in range(min, max)
        return_statement = message
    return return_statement


def color_change():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_generator = [r, g, b]
    generate_color = color_rgb(color_generator[0], color_generator[1], color_generator[2])
    return generate_color


def main():
    initial_x = find_x(50, 450, "At which point would you like to start: ")
    print("Your x value is valid")
    height = 500
    width = height
    radius = 20
    motion_x = 5
    motion_y = 5

    window = make_window("lab-6", width, height)
    window.setBackground("black")

    left = window.getWidth() - 20
    right = radius
    bottom = radius
    top = window.getHeight() - 20

    circle = make_circle(initial_x, radius, radius)
    circle.draw(window)

    while window.checkMouse() is None:
        while True:
            circle.move(motion_x, motion_y)

            if circle.getCenter().getY() <= bottom or circle.getCenter().getY() >= top:
                motion_y = -motion_y
                circle.setFill(color_change())
            elif circle.getCenter().getX() <= right or circle.getCenter().getX() >= left:
                motion_x = -motion_x
                circle.setFill(color_change())

    window.getMouse()
    window.close()


main()