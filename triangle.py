import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's speed
t.speed(3)

# Draw the first side of the triangle
t.forward(100)

# Draw the second side of the triangle
t.right(120)
t.forward(100)

# Draw the third side of the triangle
t.right(60)
t.forward(100)

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()
