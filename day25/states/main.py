import turtle
import os

from image_dimension import get_gif_dimensions

screen = turtle.Screen()
screen.title('U.S States Game')

image = "blank_states_img.gif"

# Get image dimensions directly from GIF file
width, height = get_gif_dimensions(image)
print(width, height)
if width and height:
    # Add small padding for window borders (can't be eliminated completely)
    # Most OS window managers add borders regardless
    screen.setup(width=width + 5, height=height + 25)
    screen.screensize(width, height)
else:
    # Fallback - adjust these to your image size
    width, height = 800, 600
    screen.setup(width=width, height=height)
    screen.screensize(width, height)

# Use as background image
screen.bgpic(image)

# Hide the turtle cursor
screen.turtles().clear()
turtle.hideturtle()

answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
print(answer_state)

def get_mouse_click_color(x, y):
    print(f"Clicked at: ({x}, {y})")
    
turtle.onscreenclick(get_mouse_click_color)

screen.mainloop()