import turtle

# سکرین کی سیٹنگز
screen = turtle.Screen()
screen.setup(width=600, height=800)
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(3)
t.pensize(4)


# رنگ بھرنے اور آؤٹ لائن بنانے کا فنکشن
def draw_polygon(points, fill_color):
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.color("black", fill_color)
    t.begin_fill()
    for point in points[1:]:
        t.goto(point)
    t.goto(points[0])
    t.end_fill()


# 1. مرکزی خول (Dark Green Center Shell)
# درمیان کا مسدس (Hexagon)
hex_center = [(0, 40), (45, 15), (45, -35), (0, -60), (-45, -35), (-45, 15)]
draw_polygon(hex_center, "#009a31")

# خول کے بیرونی حصے (Outer Shell Panels)
shell_top_right = [(0, 40), (45, 15), (95, 35), (55, 95), (0, 100)]
draw_polygon(shell_top_right, "#009a31")

shell_top_left = [(0, 40), (-45, 15), (-95, 35), (-55, 95), (0, 100)]
draw_polygon(shell_top_left, "#009a31")

shell_right = [(45, 15), (45, -35), (105, -30), (115, 20), (95, 35)]
draw_polygon(shell_right, "#009a31")

shell_left = Packing_list = [(-45, 15), (-45, -35), (-105, -30), (-115, 20), (-95, 35)]
draw_polygon(shell_left, "#009a31")

shell_bottom_right = [(45, -35), (0, -60), (40, -125), (95, -95), (105, -30)]
draw_polygon(shell_bottom_right, "#009a31")

shell_bottom_left = [(-45, -35), (0, -60), (-40, -125), (-95, -95), (-105, -30)]
draw_polygon(shell_bottom_left, "#009a31")


# 2. سر (Head - Light Green)
head_top = [(0, 230), (35, 190), (0, 160), (-35, 190)]
draw_polygon(head_top, "#7fcd91")

head_bottom_right = [(0, 160), (35, 190), (45, 140), (0, 100)]
draw_polygon(head_bottom_right, "#a6e3e9")

head_bottom_left = [(0, 160), (-35, 190), (-45, 140), (0, 100)]
draw_polygon(head_bottom_left, "#7fcd91")

# سر کی اندرونی لائنز
t.penup()
t.goto(0, 160)
t.pendown()
t.goto(0, 230)


# 3. دایاں بازو (Right Flipper)
flipper_r1 = [(55, 95), (95, 35), (155, 80), (105, 125)]
draw_polygon(flipper_r1, "#5cb85c")

flipper_r2 = [(105, 125), (155, 80), (225, 60), (145, 135)]
draw_polygon(flipper_r2, "#5cb85c")

flipper_r3 = [(55, 95), (105, 125), (145, 135), (45, 140), (0, 100)]
draw_polygon(flipper_r3, "#5cb85c")


# 4. بایاں بازو (Left Flipper)
flipper_l1 = [(-55, 95), (-95, 35), (-155, 80), (-105, 125)]
draw_polygon(flipper_l1, "#5cb85c")

flipper_l2 = [(-105, 125), (-155, 80), (-225, 60), (-145, 135)]
draw_polygon(flipper_l2, "#5cb85c")

flipper_l3 = [(-55, 95), (-105, 125), (-145, 135), (-45, 140), (0, 100)]
draw_polygon(flipper_l3, "#5cb85c")


# 5. دایاں پاؤں (Right Hind Leg)
leg_r1 = [(40, -125), (95, -95), (125, -120), (75, -155)]
draw_polygon(leg_r1, "#5cb85c")

leg_r2 = [(40, -125), (75, -155), (45, -155)]
draw_polygon(leg_r2, "#5cb85c")


# 6. بایاں پاؤں (Left Hind Leg)
leg_l1 = [(-40, -125), (-95, -95), (-125, -120), (-75, -155)]
draw_polygon(leg_l1, "#5cb85c")

leg_l2 = [(-40, -125), (-75, -155), (-45, -155)]
draw_polygon(leg_l2, "#5cb85c")


# ٹرٹل کو چھپانا اور سکرین روکنا
t.hideturtle()
screen.mainloop()
