import turtle

# opens a window to draw on
window = turtle.Screen()
# makes the window white
window.bgcolor("white")


def draw_square(new_turtle):
    for x in range(0, 4):
        new_turtle.pendown()
        new_turtle.right(90)
        new_turtle.forward(150)

def draw_star(new_star):
    for x in range(0, 5):
        new_star.pendown()
        new_star.right(144)
        new_star.forward(100)


def draw():
    # create an instance of Turtle
    jane = turtle.Turtle()

    # set values on attributes in the Turtle module
    jane.shape("turtle")
    jane.color("pink", "white")  # outline color, fill color
    jane.penup()
    jane.setx(150)

    # create another instance of Turtle and set its values
    ginger = turtle.Turtle()
    ginger.shape("classic")
    ginger.color("red")
    ginger.penup()
    ginger.sety(-150)

    # draw one square filled with color with the jane instance
    jane.begin_fill()
    draw_square(jane)
    jane.end_fill()

    for x in range(0, 10):
    # draw offset squares in a loop with the ginger instance
        draw_square(ginger)
        ginger.right(10)
    # draw function star 
    skarli = turtle.Turtle()
    #set values
    skarli.shape("classic")
    skarli.color("violet")
    skarli.penup()
    skarli.sety(150)

    draw_star(skarli)

    window.exitonclick()
    
# Sometimes we only want code to run if we are running this file directly.
# If we were to import this file, we wouldn't necessarily want our functions to
# run.
# By using the following conditional the draw function will not be called unless
# we run this file directly -- by calling `python turtleshapesdemo.py`
# Want to learn more about if __name__ == '__main__':?
# Check out:
# http://stackoverflow.com/a/20158605 and/or
# https://www.youtube.com/watch?v=sugvnHA7ElY
if __name__ == '__main__':
    draw()