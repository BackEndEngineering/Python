import turtle as tu
import random as rn


def draw_star(x, y, color, side):
    tu.color(color)
    tu.begin_fill()
    tu.penup()
    tu.goto(x, y)
    tu.pendown()
    for k in range(5):
        tu.forward(side)
        tu.right(144)
        tu.forward(side)
    tu.end_fill()


def random_length():
    return rn.randrange(5, 25)


def random_xy_coord():
    return rn.randrange(-290, 290), rn.randrange(-270, 270)
tu.title('a star filled sky')
tu.bgcolor('black')
tu.speed('fastest')
colors = [
            'red', 'orange', 'magenta',
            'green', 'blue', 'yellow',
            'white'
         ]
stars = 1000

for k in range(stars):
    color = rn.choice(colors)
    side = random_length()
    x, y  = random_xy_coord()
    draw_star(x, y, color, side)

tu.done()
