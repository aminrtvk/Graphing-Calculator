# COURSE CPSC 231 FALL 2021
# INSTRUCTOR: Jonathan Hudson
# Tutorial: marcus
# ID: 30127594
# Date:22/10/2021


from math import *
import turtle

# Constants
BACKGROUND_COLOR = "white"
WIDTH = 800
HEIGHT = 600
AXIS_COLOR = "black"
TIK_LENGTH = 7  # the length of the the tik line
DISTANCE_LABEL = 15  # the pixel distance between the axis and the label
DELTA = 0.02

def get_color(equation_counter):
    """
    Get color for an equation based on counter of how many equations have been drawn (this is the xth equation)
    :param equation_counter: Number x, for xth equation being drawn
    :return: A string color for turtle to use
    """
    # x is a local variable it is the remainder of 3
    # color is a local variable (string)
    color = ""
    x = equation_counter % 3
    if x == 0:
        color = "red"
    if x == 1:
        color = "green"
    if x == 2:
        color = "blue"
    return color


def calc_to_screen_coord(x, y, x_origin, y_origin, ratio):
    """
    Convert a calculator (x,y) to a pixel (screen_x, screen_y) based on origin location and ratio
    :param x: Calculator x
    :param y: Calculator y
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (screen_x, screen_y) pixel version of calculator (x,y)
    """
    # screen_y and screen_x are local variables
    screen_x = (ratio * x) + x_origin
    screen_y = (ratio * y) + y_origin
    return screen_x, screen_y


def calc_minmax_x(x_origin, ratio):
    """
    Calculate smallest and largest calculator INTEGER x value to draw for a 0->WIDTH of screen
    Smallest: Convert a pixel x=0 to a calculator value and return integer floor
    Largest : Convert a pixel x=WIDTH to a calculator value and return integer ceiling
    :param x_origin: Pixel x origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (Smallest, Largest) x value to draw for a 0->WIDTH of screen
    """
    # min_x and max_x are local variables
    min_x = int(floor(-x_origin/ratio))
    max_x = int(floor((WIDTH-x_origin)/ratio))
    return min_x, max_x


def calc_minmax_y(y_origin, ratio):
    """
    Calculate smallest and largest calculator INTEGER y value to draw for a 0->HEIGHT of screen
    Smallest: Convert a pixel y=0 to a calculator value and return integer floor
    Largest : Convert a pixel y=HEIGHT to a calculator value and return integer ceiling
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (Smallest, Largest) y value to draw for a 0->HEIGHT of screen
    """
    # min_x and max_x are local variables
    min_y = int(floor(-y_origin/ratio))
    max_y = int(floor((HEIGHT-y_origin)/ratio))
    return min_y, max_y


def draw_line(pointer, screen_x1, screen_y1, screen_x2, screen_y2):
    """
    Draw a line between tow pixel coordinates (screen_x_1, screen_y_1) to (screen_x_2, screen_y_2)
    :param pointer: Turtle pointer to draw with
    :param screen_x1: The pixel x of line start
    :param screen_y1: The pixel y of line start
    :param screen_x2: The pixel x of line end
    :param screen_y2: The pixel y of line end
    :return: None (just draws in turtle)
    """
    pointer.penup()
    pointer.goto(screen_x1, screen_y1)
    pointer.pendown()
    pointer.goto(screen_x2, screen_y2)
    pointer.penup()
    pass


def draw_x_axis_tick(pointer, screen_x, screen_y):
    """
    Draw an x-axis tick for location (screen_x, screen_y)
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :return: None (just draws in turtle)
    """
    pointer.penup()
    pointer.goto(screen_x, screen_y - TIK_LENGTH)
    pointer.pendown()
    pointer.goto(screen_x, screen_y + TIK_LENGTH)
    pointer.penup
    pass


def draw_x_axis_label(pointer, screen_x, screen_y, label_text):
    """
    Draw an x-axis label for location (screen_x, screen_y), label is label_text
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :param label_text: The string label to draw
    :return: None (just draws in turtle)
    """
    pointer.penup()
    pointer.goto(screen_x, screen_y - DISTANCE_LABEL)
    pointer.pendown()
    pointer.write(label_text)
    pointer.penup
    pass


def draw_y_axis_tick(pointer, screen_x, screen_y):
    """
    Draw an y-axis tick for location (screen_x, screen_y)
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :return: None (just draws in turtle)
    """

    pointer.penup()
    pointer.goto(screen_x - TIK_LENGTH, screen_y)
    pointer.pendown()
    pointer.goto(screen_x + TIK_LENGTH, screen_y)
    pointer.penup
    pass


def draw_y_axis_label(pointer, screen_x, screen_y, label_text):
    """
    Draw an y-axis label for location (screen_x, screen_y), label is label_text
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :param label_text: The string label to draw
    :return: None (just draws in turtle)
    """
    pointer.penup()
    pointer.goto(screen_x - DISTANCE_LABEL, screen_y)
    pointer.pendown()
    pointer.write(label_text)
    pointer.penup
    pass


def draw_x_axis(pointer, x_origin, y_origin, ratio):
    """
    Draw an x-axis centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """
    min_x, max_x = calc_minmax_x(x_origin, ratio)
    draw_line(pointer, 0, y_origin, WIDTH, y_origin)
    label_quantifier = min_x
    while min_x <= label_quantifier <= max_x:
        label_text = label_quantifier
        pixel_label_quantifier, y = calc_to_screen_coord(label_quantifier, y_origin, x_origin, y_origin, ratio)
        draw_x_axis_tick(pointer, pixel_label_quantifier, y_origin)
        draw_x_axis_label(pointer, pixel_label_quantifier, y_origin, label_text)
        label_quantifier = label_quantifier + 1
    pass


def draw_y_axis(pointer, x_origin, y_origin, ratio):
    """
    Draw an y-axis centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """
    min_y, max_y = calc_minmax_y(y_origin, ratio)
    draw_line(pointer, x_origin, 0, x_origin, HEIGHT)
    label_quantifier = min_y
    while min_y <= label_quantifier <= max_y:
        label_text = label_quantifier
        x, pixel_label_quantifier = calc_to_screen_coord(x_origin, label_quantifier, x_origin, y_origin, ratio)
        draw_y_axis_tick(pointer, x_origin, pixel_label_quantifier)
        draw_y_axis_label(pointer, x_origin, pixel_label_quantifier, label_text)
        label_quantifier += 1
    pass



def draw_expression(pointer, expr, colour, x_origin, y_origin, ratio):
    """
    Draw expression centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param expr: The string expression to draw
    :param colour: The colour to draw the expression
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """
    pointer.color(colour)
    min_y, max_y = calc_minmax_y(y_origin, ratio)
    min_x, max_x = calc_minmax_x(x_origin, ratio)
    x_1 = min_x

    while min_x <= x_1 <= max_x:
        y_1 = calc(expr, x_1)
        x_2 = x_1 + DELTA
        y_2 = calc(expr, x_2)
        pixel_x_1, pixel_y_1 = calc_to_screen_coord(x_1, y_1, x_origin, y_origin, ratio)
        pixel_x_2, pixel_y_2 = calc_to_screen_coord(x_2, y_2, x_origin, y_origin, ratio)
        if y_2 > max_y or y_2 < min_y:
            pointer.penup
        else:
            draw_line(pointer, pixel_x_1, pixel_y_1, pixel_x_2, pixel_y_2)
        x_1 += DELTA
    pass


# YOU SHOULD NOT NEED TO CHANGE ANYTHING BELOW THIS LINE UNLESS YOU ARE DOING THE BONUS


def calc(expr, x):
    """
    Return y for y = expr(x)
    Example if x = 10, and expr = x**2, then y = 10**2 = 100.
    :param expr: The string expression to evaluate where x is the only variable
    :param x: The value to evaluate the expression at
    :return: y = expr(x)
    """
    return eval(expr)


def setup():
    """
    Sets the window up in turtle
    :return: None
    """
    turtle.bgcolor(BACKGROUND_COLOR)
    turtle.setup(WIDTH, HEIGHT, 0, 0)
    screen = turtle.getscreen()
    screen.screensize(WIDTH, HEIGHT)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    screen.delay(delay=0)
    pointer = turtle
    pointer.hideturtle()
    pointer.speed(0)
    pointer.up()
    return pointer


def main():
    """
    Main loop of calculator
    Gets the pixel origin location in the window and a ratio
    Loops a prompt getting expressions from user and drawing them
    :return: None
    """
    # Setup
    pointer = setup()
    # turtle.tracer(0)
    # Get configuration
    x_origin, y_origin = eval(input("Enter pixel coordinates of chart origin (x,y): "))
    ratio = int(input("Enter ratio of pixels per step: "))
    # Draw axis
    pointer.color(AXIS_COLOR)
    draw_x_axis(pointer, x_origin, y_origin, ratio)
    draw_y_axis(pointer, x_origin, y_origin, ratio)
    # turtle.update()
    # Get expressions
    expr = input("Enter an arithmetic expression: ")
    equation_counter = 0
    while expr != "":
        # Get colour and draw expression
        colour = get_color(equation_counter)
        draw_expression(pointer, expr, colour, x_origin, y_origin, ratio)
        # turtle.update()
        expr = input("Enter an arithmetic expression: ")
        equation_counter += 1


main()
turtle.exitonclick()
