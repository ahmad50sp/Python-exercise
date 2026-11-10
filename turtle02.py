import turtle
import random

# Screen aur Turtle ki basic setting
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#1a1a2e")  # Dark Night Sky color
screen.tracer(0)  # Heavy coding me lag ko khatam karne ke liye fast drawing mode

t = turtle.Turtle()
t.speed(0)
t.hideturtle()


# --- STEP 1: STARS (Aasman me sitare) ---
def draw_stars():
    t.pencolor("white")
    for _ in range(40):
        t.penup()
        x = random.randint(-400, 400)
        y = random.randint(100, 250)
        t.goto(x, y)
        t.pendown()
        t.dot(random.randint(2, 4))


# --- STEP 2: WINDOWS (Khidkiyan banane ka function) ---
def draw_windows(start_x, start_y, b_width, b_height):
    t.pencolor("#f4d160")  # Glowing Yellow windows
    t.fillcolor("#f4d160")

    # Rows aur columns calculate karna building ke size ke hisab se
    rows = b_height // 40
    cols = b_width // 30

    for r in range(rows):
        for c in range(cols):
            # Har khidki random chalegi (kuch on, kuch off) realistic look ke liye
            if random.choice([True, True, False]):
                t.penup()
                t.goto(start_x + 10 + (c * 25), start_y + 10 + (r * 35))
                t.pendown()
                t.begin_fill()
                for _ in range(4):
                    t.forward(12)
                    t.left(90)
                t.end_fill()


# --- STEP 3: HEAVY BUILDINGS DESIGN ---
def draw_building(x, y, width, height, b_type, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor("#0f3460")  # Dark border
    t.fillcolor(color)
    t.begin_fill()

    # Building ka main structure
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

    # Building ke upar ke designs (Roof Details)
    if b_type == "tower":  # Unchi Teekhi Building
        t.penup()
        t.goto(x + width // 2, y + height)
        t.pendown()
        t.pencolor("red")
        t.goto(x + width // 2, y + height + 40)  # Antenna tower
    elif b_type == "dome":  # Gumbad wali building
        t.penup()
        t.goto(x, y + height)
        t.pendown()
        t.begin_fill()
        t.circle(width // 2, 180)  # Roof dome
        t.end_fill()

    # Windows draw karna
    draw_windows(x, y, width, height)


# --- EXECUTION (City ko screen par utarna) ---
draw_stars()

# Building Data: (X_Position, Y_Position, Width, Height, Type, Color)
buildings = [
    (-380, -250, 100, 350, "flat", "#16213e"),
    (-260, -250, 130, 420, "tower", "#0f3460"),
    (-110, -250, 150, 300, "dome", "#16213e"),
    (60, -250, 110, 460, "tower", "#0f3460"),
    (190, -250, 140, 320, "flat", "#16213e"),
    (350, -250, 120, 380, "dome", "#0f3460"),
]

# Ek ek karke saari heavy buildings draw karna
for b in buildings:
    draw_building(b[0], b[1], b[2], b[3], b[4], b[5])

# Screen ko update karna (kyunki tracer(0) use kiya tha)
screen.update()

# Close on click
screen.exitonclick()
