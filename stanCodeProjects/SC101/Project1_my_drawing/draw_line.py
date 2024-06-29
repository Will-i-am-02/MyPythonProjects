"""
File: draw_line.py
Name: William
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 5
window = GWindow()
circle = GOval(SIZE * 2, SIZE * 2)
click = 1


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(event):
    global click
    if click % 2 != 0:
        window.add(circle, x=event.x - SIZE, y=event.y - SIZE)
    else:
        line = GLine(x0=circle.x, y0=circle.y, x1=event.x, y1=event.y)
        window.remove(circle)
        window.add(line)
    click += 1


if __name__ == "__main__":
    main()
