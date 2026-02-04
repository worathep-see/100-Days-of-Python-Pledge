import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
colors_list = [(249, 248, 243), (250, 245, 248), (243, 250, 246), (241, 246, 250), (234, 225, 83), (195, 8, 69), (231, 54, 132), (194, 164, 15), (112, 178, 214), (199, 77, 15), (216, 162, 101), (34, 187, 112), (29, 104, 167), (14, 23, 64), (20, 29, 168), (212, 136, 175), (231, 224, 7), (197, 34, 130), (15, 181, 210), (231, 167, 197), (126, 189, 163), (10, 48, 29), (40, 131, 75), (141, 217, 203), (61, 22, 10), (60, 13, 27), (108, 91, 210), (235, 64, 34), (131, 217, 230), (183, 17, 9)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dot = 100

for _ in range(1, number_of_dot + 1):
    tim.dot(20, random.choice(colors_list))
    tim.forward(50)

    if _ % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
