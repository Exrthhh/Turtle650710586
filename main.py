"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()

for c in ['red', 'lightblue', 'purple', 'brown', 'blue', 'black','yellow', 'lightblue','gold', 'blue','red','lightgreen']:
    t.color(c)
    t.forward(60)
    t.left(30)