"""
File: bouncing_ball.py
Name: William
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')  # Use to create a window called "bouncing_ball.py"
black_dot = GOval(SIZE, SIZE, x=START_X, y=START_Y)   # Use to create a black_dot to let it fall.
start = False                                         # Use to control program, when mouse clicked again will start next run.


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    black_dot.filled = True
    window.add(black_dot)
    onmouseclicked(bounce)
    global start
    vy = 10
    original_vy = vy
    times = 0
    while True:
        if start:
            while True:
                black_dot.move(VX, vy)
                vy += GRAVITY
                if black_dot.y >= window.height:
                    vy = -vy * REDUCE
                pause(DELAY)
                if black_dot.x > window.width:
                    vy = original_vy
                    break
            window.remove(black_dot)
            window.add(black_dot, x=START_X, y=START_Y)
            vy = 0

            start = False
            times += 1
        if times >= 3:
            break
        pause(DELAY*DELAY)


def bounce(event):
    global start
    if event.x >= 0 or event.x <= window.width:
        start = True


if __name__ == "__main__":
    main()
