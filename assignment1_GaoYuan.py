import turtle
import random

# ========== Set up the screen ==========
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colourful Turtle Patterns")
screen.setup(width=800, height=800)

t = turtle.Turtle()
t.speed(0)  # Fastest speed

# Colour list (dynamically change colours)
colors = ["red", "orange", "yellow", "green",
          "cyan", "blue", "purple", "pink", "white"]

# ========== 1. Draw a colourful star pattern ==========
def draw_star_pattern():
    """Use a for loop to draw many rotating colourful 5-pointed stars"""
    t.penup()
    t.goto(0, 0)
    t.pendown()

    for i in range(36):                      # Loop 36 times
        t.color(colors[i % len(colors)])     # Dynamically change colour
        t.pensize(2)

        # The length of each star changes dynamically with the loop
        length = 100 + i * 5

        for _ in range(5):                   # Each star has 5 edges
            t.forward(length)
            t.right(144)

        t.right(10)                          # Rotate 10 degrees each time

# ========== 2. Draw a colourful square pattern ==========
def draw_square_pattern():
    """Nested for loops to draw rotating squares"""
    t.penup()
    t.goto(0, 0)
    t.pendown()

    for i in range(50):
        t.color(colors[i % len(colors)])
        t.pensize(2)
        side = 50 + i * 4                    # Length changes dynamically

        for _ in range(4):                   # A square has 4 sides
            t.forward(side)
            t.right(90)

        t.right(7)                           # Rotation creates the pattern

# ========== 3. Draw a colourful triangle spiral ==========
def draw_triangle_pattern():
    t.penup()
    t.goto(0, 0)
    t.pendown()

    for i in range(60):
        t.color(colors[i % len(colors)])
        t.pensize(2)
        side = 20 + i * 3                    # Dynamic length

        for _ in range(3):                   # A triangle has 3 sides
            t.forward(side)
            t.right(120)

        t.right(6)

# ========== Main program: show the three patterns one by one ==========
draw_star_pattern()
t.clear()                # Clear the canvas
draw_square_pattern()
t.clear()
draw_triangle_pattern()

# Keep the window open
screen.mainloop()

# ========== QA Bot interactive program ==========
print("=" * 50)
print("Welcome to the smart QA Bot! (type 'bye' to exit)")
print("You can ask me about: HKU / robot / jetson / ai / human")
print("=" * 50)

while True:
    # Receive the user's input
    question = input("\nPlease enter your question: ").strip().lower()

    # Exit condition
    if question == "bye" or question == "exit" or question == "quit":
        print("Bot: Goodbye! Hope I was helpful 👋")
        break

    # Handle empty input
    elif question == "":
        print("Bot: Please enter a question :)")

    # Keyword 1: HKU
    elif "hku" in question:
        print("Bot: HKU stands for The University of Hong Kong, "
              "Hong Kong's oldest higher-education institution and "
              "one of the world's leading universities.")

    # Keyword 2: robot
    elif "robot" in question:
        print("Bot: A robot is a machine that can perform tasks "
              "automatically. It is used in industry, healthcare, "
              "education, and home services.")

    # Keyword 3: jetson
    elif "jetson" in question:
        print("Bot: Jetson is NVIDIA's embedded AI computing platform, "
              "widely used in robots, drones, and edge AI devices.")

    # Keyword 4: ai
    elif "ai" in question or "artificial intelligence" in question:
        print("Bot: AI (Artificial Intelligence) is the technology that "
              "lets machines simulate human intelligence — learning, "
              "reasoning, perception, and natural language processing.")

    # Keyword 5: human
    elif "human" in question:
        print("Bot: Human refers to people. The key difference between "
              "humans and AI lies in emotion, consciousness, and moral "
              "judgement — complex abilities AI lacks.")

    # Anything else
    else:
        print("Bot: Sorry, I don't understand that question yet. "
              "You can ask me about HKU, robot, jetson, ai, or human.")
