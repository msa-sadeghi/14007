import turtle

s = turtle.Screen()
s.bgcolor("orange")
s.title("hello everybody")
s.setup(800, 600)

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.pensize(5)
my_turtle.pencolor("red")
my_turtle.color("green")
my_turtle.begin_fill()
for i in range(3):
    my_turtle.forward(100)
    my_turtle.left(120)
my_turtle.end_fill()
for i in range(4):
    my_turtle.forward(100)
    my_turtle.left(90)
for i in range(6):
    my_turtle.forward(100)
    my_turtle.left(60)
    
    
turtle.done()