"""
Pixel Art & Geometric Shape Studio
Interactive canvas built with Python's Turtle graphics and Tkinter dialogs.
"""
import turtle
import tkinter as tk
from tkinter import colorchooser, simpledialog, messagebox
import sys


def draw_pixel(x, y, color, size):
    turtle.penup()
    turtle.goto(x - size // 2, y - size // 2)
    turtle.pendown()
    turtle.dot(size, color)


def draw_square(x, y, color, size, fill=False):
    turtle.penup()
    turtle.goto(x - size // 2, y - size // 2)
    turtle.pendown()
    if fill:
        turtle.fillcolor(color)
        turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)
    if fill:
        turtle.end_fill()


def draw_circle(x, y, color, size, fill=False):
    turtle.penup()
    turtle.goto(x, y - size // 2)
    turtle.pendown()
    if fill:
        turtle.fillcolor(color)
        turtle.begin_fill()
    turtle.circle(size // 2)
    if fill:
        turtle.end_fill()


def draw_triangle(x, y, color, size, fill=False):
    turtle.penup()
    turtle.goto(x, y - size // 2)
    turtle.pendown()
    if fill:
        turtle.fillcolor(color)
        turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    if fill:
        turtle.end_fill()


def draw_diamond(x, y, color, size, fill=False):
    turtle.penup()
    turtle.goto(x, y - size // 2)
    turtle.pendown()
    if fill:
        turtle.fillcolor(color)
        turtle.begin_fill()
    for _ in range(2):
        turtle.forward(size)
        turtle.left(45)
        turtle.forward(size)
        turtle.left(135)
    if fill:
        turtle.end_fill()


def draw_heart(x, y, color, size, fill=False):
    turtle.penup()
    turtle.goto(x, y - size // 2)
    turtle.pendown()
    if fill:
        turtle.fillcolor(color)
        turtle.begin_fill()
    turtle.left(50)
    turtle.forward(size)
    turtle.circle(size // 2, 180)
    turtle.right(140)
    turtle.circle(size // 2, 180)
    turtle.forward(size)
    turtle.setheading(0)
    if fill:
        turtle.end_fill()


def draw_polygon(x, y, color, size, sides, fill=False):
    turtle.penup()
    turtle.goto(x, y - size // 2)
    turtle.pendown()
    if fill:
        turtle.fillcolor(color)
        turtle.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(size)
        turtle.left(angle)
    if fill:
        turtle.end_fill()


def draw_line(x, y, color, size, thickness):
    turtle.penup()
    turtle.goto(x - size // 2, y)
    turtle.pendown()
    turtle.pensize(thickness)
    turtle.pencolor(color)
    turtle.forward(size)


def draw_star(x, y, color, size, points, fill=False):
    turtle.penup()
    turtle.goto(x, y - size // 2)
    turtle.pendown()
    if fill:
        turtle.fillcolor(color)
        turtle.begin_fill()
    for _ in range(points):
        turtle.forward(size)
        turtle.right(144)
    if fill:
        turtle.end_fill()


def draw_spiral(x, y, color, size, loops):
    turtle.penup()
    turtle.goto(x, y - size // 2)
    turtle.pendown()
    turtle.pencolor(color)
    for _ in range(loops * 36):
        turtle.forward(size / 20)
        turtle.right(10)


def main():
    root = tk.Tk()
    root.withdraw()

    turtle.speed(0)
    turtle.title("Pixel Art & Shape Studio")
    turtle.setup(800, 600)

    canvas = turtle.Screen()
    canvas.bgcolor("white")

    color = "black"
    size = 20

    print("Starting Pixel Art Generator canvas...")

    while True:
        try:
            pattern = simpledialog.askstring(
                "Pattern",
                "Choose: square, circle, triangle, diamond, heart, polygon, star, spiral, pixel, clear, bg, exit:"
            )
        except Exception:
            break

        if pattern is None or pattern.strip().lower() == 'exit':
            break

        pattern = pattern.strip().lower()

        if pattern == 'clear':
            turtle.clear()
            canvas.update()
            continue

        if pattern == 'bg':
            chosen = colorchooser.askcolor(title="Choose background color")
            if chosen[1]:
                canvas.bgcolor(chosen[1])
            continue

        # Choose color
        chosen = colorchooser.askcolor(title=f"Choose color for {pattern}")
        if chosen[1]:
            color = chosen[1]

        # Choose size
        s_input = simpledialog.askinteger("Size", "Enter size (5-100):", initialvalue=size, minvalue=5, maxvalue=200)
        if s_input:
            size = s_input

        # Draw shape
        if pattern == 'square':
            draw_square(0, 0, color, size, fill=True)
        elif pattern == 'circle':
            draw_circle(0, 0, color, size, fill=True)
        elif pattern == 'triangle':
            draw_triangle(0, 0, color, size, fill=True)
        elif pattern == 'diamond':
            draw_diamond(0, 0, color, size, fill=True)
        elif pattern == 'heart':
            draw_heart(0, 0, color, size, fill=True)
        elif pattern == 'star':
            draw_star(0, 0, color, size, 5, fill=True)
        elif pattern == 'spiral':
            draw_spiral(0, 0, color, size, 3)
        elif pattern == 'polygon':
            sides = simpledialog.askinteger("Sides", "Number of sides (3-12):", initialvalue=6, minvalue=3, maxvalue=12)
            if sides:
                draw_polygon(0, 0, color, size, sides, fill=True)
        elif pattern == 'pixel':
            draw_pixel(0, 0, color, size)
        else:
            messagebox.showinfo("Unknown Pattern", f"Pattern '{pattern}' not recognized.")

        canvas.update()

    try:
        turtle.bye()
    except Exception:
        pass


if __name__ == "__main__":
    main()
