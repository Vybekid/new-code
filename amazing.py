import turtle
import colorsys

# Set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)  # Set the drawing speed to the fastest
t.pensize(2)

# Set the initial hue
h = 0.0

# Drawing loop
for i in range(120):
    # Convert HSV color to RGB
    c = colorsys.hsv_to_rgb(h, 1, 1)
    
    # Set the color
    t.pencolor(c)
    
    # Draw a circle
    t.circle(150)
    
    # Rotate the turtle for the next circle
    t.right(3)
    
    # Increment hue for color change
    h += 0.008

# Hide the turtle and keep the window open
t.hideturtle()
turtle.done()