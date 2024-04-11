import turtle
sides=4
radius=30
window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
korok = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
korok.shape('turtle')
# Set your turtle's speed using .speed(2)
korok.speed(2)
# Set your turtle's color using .color('green') and .pencolor('blue')
korok.color('green')
korok.pencolor('blue')
# Move your turtle forward using .forward(100)
# TEST
for n in range(sides):
    korok.forward(100)

# Move your turtle left or right using .left(90) or .right(90)
    korok.left(90)
# Now put the forward and left/right code into a for loop to repeat 4 times.
# TEST    Did your turtle draw a square?
#yes
# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen
korok.goto(x=100, y=100)
# Have your turtle draw a circle using .circle(radius, steps=30)
# TEST yes  Did your turtle draw a circle?
korok.begin_fill()
korok.circle(radius, steps=radius)
# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below
korok.end_fill()
# Draw 3 more shapes with different fill colors!

# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()

