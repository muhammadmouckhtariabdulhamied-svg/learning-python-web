import turtle 

colours = ["green","orange","blue","violet","red","yellow","purple","pink","cyan","magenta","white","gray",]
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)

for x in range (360):
    t.pencolor(colours[x%12])
    t.width(x // 100 + 2)
    t.forward(x)
    t.left(59)
