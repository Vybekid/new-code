import turtle
import math
import colorsys as cs
# Set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen.tracer(0) # Turn off screen updates for instant drawing

# Define the golden angle
golden_angle = 137.5

# Drawing loop
for i in range(500):
    # Calculate the radius (distance from the center)
    # The radius increases, making the spiral grow outwards
    radius = 4 * math.sqrt(i)
    
    # Calculate the angle for the current dot
    angle = i * golden_angle
    
    # Convert polar coordinates (radius, angle) to Cartesian (x, y)
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    
    # Use the radius to determine the color, creating a gradient
    # from the center outwards
    hue = (radius / 300) % 1  # Normalize radius for hue value
    r, g, b = turtle.cs.hsv_to_rgb(hue, 1, 1)
    
    # Move to position and draw a dot
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(15, (r, g, b)) # Draw a dot of size 15 with the calculated color

# Update the screen to show the final drawing
screen.update()
turtle.done()