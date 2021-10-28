# Programmers: Jonathan, Alex, Sebastian
# Course: CS151, Dr. Rajeev
# Date: October 21st, 2021
# Lab Number: 6
# Program Inputs:
# Program Outputs:

from graphicsCS151 import *
from graphics import *


def get_coordinate (min, max, message):
    coord = int(input(message))
    while not (coord >= min and coord <= max):
        coord = int(input(message))
    return coord


height = 500
width = height
radius = 28

def make_window( title, width, height ):
    win = GraphWin( title, width, height )
    return win


def make_circle( x, y, radius ):
    return Circle( Point( x, y ), radius )


def color_circle(circle, color ):
    circle.setFill( color )
    circle.setOutline( color )


def move( circle, moveX, moveY ):
    circle.move( moveX, moveY  )

def change_title( window,title ):
    window.master.title( title )

def sleep( ms):
    time.sleep( ms / 1000 )


def main():
    win = GraphWin("My Circle", 500, 500)
    c = Circle(Point(50, 50), 10)
    c.draw(win)
    win.getMouse()  # Pause to view result
    win.close()  # Close window when done
    x = get_coordinate(50, 450, "Enter starting x coordinate between 50 and 450: ")
    y = 20
    circle = make_circle(x, y, 20)
    dx = 2
    dy = 2
    hit_top = False

    while not hit_top:

        move(circle, dx, dy)

        if (circle.GetCenter().x + circle.GetRadius()) >= win.GetWidth() or (
            circle.GetCenter().x - circle.GetRadius()) <= 0:
            dx = -dx

        if (circle.GetCenter().y + circle.GetRadius()) >= win.getHeight():
            dy = -dy
        hit_top = True

        if (circle.GetCenter().y - circle.GetRadius()) <= 0:
            hit_top = True
            sleep(1)


main()







