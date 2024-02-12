import turtle as t
from random import randint, choice
import colorgram


timmy = t.Turtle()
screen = t.Screen()
timmy.hideturtle()
timmy.penup()
t.colormode(255)
coul = colorgram.extract('hirst.jpg', 40)

t.title("Drawspot")
timmy.shape("turtle")
timmy.speed(0)

for j in range(0, 600, 100):
    y = j - 300
    for i in range(0, 800, 100):
        x = i - 400
        timmy.goto(x, y)
        timmy.dot(40, choice(coul).rgb)


# # Couleur random
# def rand_color():
#     r = (randint(0, 255))
#     g = (randint(0, 255))
#     b = (randint(0, 255))
#     couleur = (r, g, b)
#     return couleur
## fin couleur random

# # Spyrographe
# for i in range(int(720/5/2)):
#     timmy.color(rand_color())
#     timmy.circle(100)
#     timmy.right(180)
#     timmy.forward(50)
#     timmy.color(rand_color())
#     timmy.circle(100)
#     timmy.forward(50)
#     timmy.right(10)
# # Fin Spyro



# # Random Draw - with saving files #
# for i in range(1):
#     for _ in range(1000):
#         timmy.color(rand_color())
#         timmy.forward(randint(0, 20))
#         timmy.right(randint(0, 360))
#
#     #nomfichier = "image" + str(i+1) + ".ps"
#     #timmy.getscreen().getcanvas().postscript(file=nomfichier)
#     #timmy.goto(0, 0)
#     #t.clear()
# # Random Draw #

# # Drawing multi shapes 3 sides to 10 sides
# couleur = ['black', 'black', 'black', 'black', 'purple', 'blue', 'green', 'yellow', 'orange', 'red' ]
# for i in range(3, 10):
    # for j in range(i):
    #     timmy.pendown()
    #     timmy.color(couleur[i])
    #     timmy.forward(100)
    #     timmy.right(360/i)
# # End of Draw multi

t.exitonclick()

