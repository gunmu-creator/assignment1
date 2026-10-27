import turtle
import time

# ============================================================
#  PART 1: TURTLE DRAWING
# ============================================================

# Colour list (used to dynamically change colours)
colors = ["red", "orange", "yellow", "green",
          "cyan", "blue", "purple", "pink", "white"]

# Drawing speed: 1 = slowest, 10 = fastest
# Try 1, 2, or 3 for a nice slow visual effect
DRAW_SPEED = 0


def setup_turtle():
    """Create and return a configured turtle screen and turtle."""
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Colourful Turtle Patterns")
    screen.setup(width=800, height=800)
    # NOTE: No tracer(0) — we want to see the animation

    t = turtle.Turtle()
    t.speed(DRAW_SPEED)       # Slow speed so the drawing is visible
    t.hideturtle()
    return screen, t


def draw_star_pattern(t):
    """Draw many rotating colourful 5-pointed stars using a for loop."""
    t.penup()
    t.goto(0, 0)
    t.pendown()

    for i in range(36):                      # Loop 36 times
        t.color(colors[i % len(colors)])     # Dynamically change colour
        t.pensize(2)

        length = 100 + i * 5                 # Length changes dynamically

        for _ in range(5):                   # Each star has 5 edges
            t.forward(length)
            t.right(144)

        t.right(10)                          # Rotate to spread the stars


def draw_square_pattern(t):
    """Draw rotating colourful squares using nested for loops."""
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

        t.right(7)


def draw_triangle_pattern(t):
    """Draw a colourful triangle spiral using nested for loops."""
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


def run_turtle_drawing():
    """Run the full turtle drawing showcase."""
    print("\nOpening the turtle window...")
    print("A window will appear. Close it when you are done viewing.\n")

    screen, t = setup_turtle()

    # Draw each pattern slowly so the user can watch
    print("Drawing star pattern...")
    draw_star_pattern(t)
    time.sleep(1.5)          # Pause so the pattern is visible
    t.clear()

    print("Drawing square pattern...")
    draw_square_pattern(t)
    time.sleep(1.5)
    t.clear()

    print("Drawing triangle pattern...")
    draw_triangle_pattern(t)
    time.sleep(1.5)

    print("\nAll patterns finished. Close the turtle window to return to the menu.")

    # Keep the window open until the user closes it
    screen.mainloop()


# ============================================================
#  PART 2: QA BOT
# ============================================================

def run_qa_bot():
    """Interactive bot that answers questions using conditional logic."""
    print("\n" + "=" * 50)
    print("Welcome to the smart QA Bot! (type 'bye' to exit)")
    print("You can ask me about: HKU / robot / jetson / ai / human")
    print("=" * 50)

    while True:
        # Receive the user's input
        question = input("\nPlease enter your question: ").strip().lower()

        # Exit condition
        if question in ("bye", "exit", "quit"):
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


# ============================================================
#  MAIN MENU
# ============================================================

def main():
    """Main menu that lets the user choose a feature or exit."""
    while True:
        print("\n" + "=" * 50)
        print("        ASSIGNMENT ONE — MAIN MENU")
        print("=" * 50)
        print("  1. Turtle Drawing  (colourful patterns)")
        print("  2. QA Bot          (ask me questions)")
        print("  3. Exit")
        print("=" * 50)

        choice = input("Please choose an option (1 / 2 / 3): ").strip()

        if choice == "1":
            run_turtle_drawing()

        elif choice == "2":
            run_qa_bot()

        elif choice == "3":
            print("\nThank you for using the program. Goodbye! 👋")
            break

        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")


# ============================================================
#  PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
