import turtle


def draw_square(tur):
    tur.forward(100)
    tur.right(90)
    tur.forward(100)
    tur.right(90)
    tur.forward(100)
    tur.right(90)
    tur.forward(100)
    tur.right(90)


def draw_circle(tur):
    tur.circle(80)


def draw():
    window = turtle.Screen()
    window.bgcolor('red')

    brad = turtle.Turtle()

    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(100)

    count = 0
    while count < 360:
        brad.right(12)
        draw_square(brad)
        count += 12

    angie = turtle.Turtle()
    angie.shape('turtle')
    angie.color('white')

    draw_circle(angie)

    chap = turtle.Turtle()
    chap.right(45)
    chap.forward(100)
    chap.right(135)
    chap.forward(141.4)
    chap.right(135)
    chap.forward(100)

    window.exitonclick()


draw()
