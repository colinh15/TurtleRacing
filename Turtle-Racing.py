# Used for all graphical elements
from turtle import *

# Used to randomize the results of the race
import random

# Set up the background color and window size
colormode(255)
screen = Screen()
screen.setup(1280, 720)
screen.bgcolor(0, 70, 0)

# The y positions that each turtle will race at
y_positions = [25, -25, 75, -75, 125, -125, 175, -175, 225, -225, 275, -275, 325, -325]

# The colors of the turtles
colors = ["red", "orange", "green", "blue", "purple", "yellow", "pink", "white", "black", "gray", "gold", "cyan", "navy", "salmon"]

is_race_on = False  # Determines whether the turtles should continue racing
all_turtles = []    # Array of Turtle objects
winning_color = ""  # Color of the winning turtle
screen.tracer(0)    # Makes sure that the screen does not load until the game is finished loading

# Ask the user how many turtles should race. (Will only accept a number between 2 and 14)
num_turtles = screen.numinput("Number of Turtles", "How many turtles should race? (MAX 14): ", None, 2, 14)
num_turtles = int(num_turtles)

# Create the text string which will be used to ask the user which turtle will win the race.
text_prompt = "Which turtle will win the race?  Options: "
for i in range(num_turtles):
    text_prompt += colors[i]
    if i != num_turtles - 1:
        text_prompt += ", "
    else:
        text_prompt += ".  Enter a color: "

# Popup asking user to choose which turtle they think will win the race.
input_is_valid= False
while True:
    user_bet = screen.textinput("Make your bet.", text_prompt).lower()

    # Input checking
    for i in range (num_turtles):
        if user_bet == colors[i]:
            input_is_valid = True

    if input_is_valid:
        break
    else:
        print("Please choose a valid color.")

# Popup asking for user to make a monetary bet.
money_bet = screen.numinput("Make your bet.", "How much money do you want to bet?  Do not include a \"$\".  Just write the amount.  (Max 1000)", None, 0, 1000)
money_bet = int(money_bet)

# The profit that the user will gain if their turtle wins.
# Calculated based upon the number of turtles in the race.
win_profit = (money_bet * num_turtles) - money_bet

# Set the speed that the turtles will move, depending on the number of turtles in the race
# This is to balance out the length of the races, at least somewhat
if num_turtles > 10:
    turtle_speed = 0
elif num_turtles > 5:
    turtle_speed = num_turtles
else:
    turtle_speed = num_turtles - 1

# Set up a helper turtle that will draw the finish line
helper = Turtle()
helper.speed("fastest")
helper.pu()
helper.goto(620, 600)
helper.pencolor("black")
helper.pensize(40)
helper.right(90)
helper.pd()

# Draw the finish line
for i in range(30):
    if i % 2 == 0:
        helper.pencolor("black")
    else:
        helper.pencolor("white")
    helper.forward(40)

# Create the turtle objects for the turtles that will be racing, set their colors to
# the colors in the "colors" list, and move each of them to their starting positions
for turtle_index in range(num_turtles):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.pu()
    new_turtle.speed("fastest")
    new_turtle.goto(x=-600, y=y_positions[turtle_index])
    new_turtle.speed(turtle_speed)
    all_turtles.append(new_turtle)


# Start the race, and turn the tracer back on so the screen updates as normal
is_race_on = True
screen.tracer(1, 10)

while is_race_on:

    # Constantly loop through each turtle and choose how much to move it
    for turtle in range(len(all_turtles)):

        # Choose how much boost to give the selected turtle
        boost = random.randint(0,500)

        # Uncomment the four lines below to rig the race for the red turtle
        # if turtle == 0:
        #     boost = random.randint(500, 500)
        # else:
        #     boost = random.randint(0, 500)

        # These are the turtle movement chances in the code below:
        # 20% chance: Move turtle backward 1 step
        # 20% chance: Move turtle forward 1 step
        # 20% chance: Move turtle forward 4 steps
        # 20% chance: Move turtle forward 9 steps
        # 19% chance: Move turtle forward 16 steps
        # 0.8% chance: Give turtle a boost that will move it 50 steps.
        #              The turtle will leave a dark orange trail behind.
        # 0.2% chance: Give turtle a boost that will move it 100 steps.
        #              The turtle will leave a light orange trail behind.

        if 0 <= boost < 100:
            all_turtles[turtle].backward(1)
        elif 100 <= boost < 200:
            all_turtles[turtle].forward(1)
        elif 200 <= boost < 300:
            all_turtles[turtle].forward(4)
        elif 300 <= boost < 400:
            all_turtles[turtle].forward(9)
        elif 400 <= boost < 495:
            all_turtles[turtle].forward(16)
        elif 495 <= boost < 500:
            all_turtles[turtle].pencolor("DarkOrange")
            all_turtles[turtle].pensize(3)
            all_turtles[turtle].pd()
            all_turtles[turtle].forward(50)
            all_turtles[turtle].pu()
            all_turtles[turtle].pencolor(colors[turtle])
            all_turtles[turtle].pensize(0)
        elif boost == 500:
            all_turtles[turtle].pencolor("orange")
            all_turtles[turtle].pensize(5)
            all_turtles[turtle].pd()
            all_turtles[turtle].forward(100)
            all_turtles[turtle].pu()
            all_turtles[turtle].pencolor(colors[turtle])
            all_turtles[turtle].pensize(0)

        # If one of the turtles crosses the finish line (x-coordinate > 600), end the race.
        if all_turtles[turtle].xcor() > 600:
            # Determine which turtle won the race.
            winning_color = colors[turtle]

            # If the winning color is what the user bet at the start, display a "you won" prompt.
            # If the user bet money, show winnings.
            if winning_color == user_bet:
                if money_bet > 0:
                    screen.textinput("You won!", f"The {user_bet} turtle was the winning turtle.  You made a profit of ${win_profit}!  PRESS OK TO CONTINUE...")
                else:
                    screen.textinput("You won!",f"The {user_bet} turtle was the winning turtle.  PRESS OK TO CONTINUE...")

            # If the winning color is not what the user bet at the start, display a "you lost" prompt.
            # If the user bet money, display "you lost all of your money".
            else:
                if money_bet > 0:
                    screen.textinput("You lost...",f"The {user_bet} turtle was not the winning turtle.  You lost all of your money...  PRESS OK TO CONTINUE...")
                else:
                    screen.textinput("You lost...",f"The {user_bet} turtle was not the winning turtle.  PRESS OK TO CONTINUE...")

            # Ends the race
            is_race_on = False