import turtle

def draw_square(color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()


def draw_border(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("black")
    turtle.width(2)
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)


def draw_shadow(x, y):
    turtle.penup()
    turtle.goto(x + 10, y - 10)
    turtle.pendown()
    turtle.color("gray")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()


def draw_gradient_square(color1, color2, x, y):
    for i in range(10):
        turtle.penup()
        turtle.goto(x + i * 5, y - i * 5)
        turtle.pendown()
        turtle.color(color1)
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(100 - i * 10)
            turtle.right(90)
        turtle.end_fill()
        color1 = color2  # Change color for gradient effect


def setup_screen():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Enhanced Microsoft Logo with Turtle")
    turtle.speed(7)
    turtle.hideturtle()


def draw_microsoft_logo():
    setup_screen()

    # Draw shadows
    draw_shadow(-110, 50)
    draw_shadow(10, 50)
    draw_shadow(-110, -60)
    draw_shadow(10, -60)

    # Draw gradient squares with borders
    draw_gradient_square("red", "darkred", -110, 50)
    draw_border(-110, 50)

    draw_gradient_square("green", "darkgreen", 10, 50)
    draw_border(10, 50)

    draw_gradient_square("blue", "darkblue", -110, -60)
    draw_border(-110, -60)

    draw_gradient_square("yellow", "gold", 10, -60)
    draw_border(10, -60)

    turtle.done()


# Call the main function to execute the program
draw_microsoft_logo()
