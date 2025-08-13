import turtle
import colorsys

# Set up the screen for the graphic
screen = turtle.Screen()
screen.bgcolor("black")

# Create and configure the turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# Initialize hue for color cycling
hue = 0.0

# Loop to draw the rotating squares
for i in range(150):
    # Set the color for the current square
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.pencolor(color)

    # Draw one square
    for _ in range(4):
        t.forward(i * 2.5)
        t.right(90)

    # Rotate for the next square and update color
    t.right(7)
    hue += 0.005

turtle.done()