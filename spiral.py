import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)

# Set the initial hue
hue = 0.0

# Loop to draw the spiral
for i in range(360):
    # Set the color using HSV color space
    rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.pencolor(rgb)

    # Move the turtle
    t.forward(i * 2)
    t.right(121)

    # Increment the hue for the next color
    hue += 0.005

turtle.done()
H