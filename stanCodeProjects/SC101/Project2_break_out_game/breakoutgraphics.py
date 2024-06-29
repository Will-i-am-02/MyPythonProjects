"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (self.window.width-paddle_width)/2, window_height-paddle_offset)
        # Center a filled ball in the graphical window
        self.ball_radius = ball_radius
        self.ball = GOval(width=ball_radius*2, height=ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, (self.window.width-ball_radius*2)/2, (self.window.height-ball_radius*2)/2)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        self.switch = False
        onmouseclicked(self.switch_open)
        onmousemoved(self.move_paddle)
        # Draw bricks
        cols = 0
        rows = brick_offset
        self.num_brick = BRICK_COLS * BRICK_ROWS
        for i in range(brick_rows):
            for j in range(brick_cols):
                if 0 <= i <= 1:
                    self.brick = GRect(width=brick_width, height=brick_height)
                    self.brick.filled = True
                    self.brick.color = 'red'
                    self.brick.fill_color = 'red'
                    self.window.add(self.brick, cols, rows)
                    cols += brick_width + brick_spacing

                elif 2 <= i <= 3:
                    self.brick = GRect(width=brick_width, height=brick_height)
                    self.brick.filled = True
                    self.brick.color = 'orange'
                    self.brick.fill_color = 'orange'
                    self.window.add(self.brick, cols, rows)
                    cols += brick_width + brick_spacing
                elif 4 <= i <= 5:
                    self.brick = GRect(width=brick_width, height=brick_height)
                    self.brick.filled = True
                    self.brick.color = 'yellow'
                    self.brick.fill_color = 'yellow'
                    self.window.add(self.brick, cols, rows)
                    cols += brick_width + brick_spacing
                elif 6 <= i <= 7:
                    self.brick = GRect(width=brick_width, height=brick_height)
                    self.brick.filled = True
                    self.brick.color = 'green'
                    self.brick.fill_color = 'green'
                    self.window.add(self.brick, cols, rows)
                    cols += brick_width + brick_spacing
                else:
                    self.brick = GRect(width=brick_width, height=brick_height)
                    self.brick.filled = True
                    self.brick.color = 'blue'
                    self.brick.fill_color = 'blue'
                    self.window.add(self.brick, cols, rows)
                    cols += brick_width + brick_spacing
            rows += brick_height + brick_spacing
            cols = 0

    def move_paddle(self, event):
        if event.x-self.paddle.width/2 <= 0:
            self.paddle.x = 0
        elif event.x >= self.window.width - self.paddle.width/2:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = event.x - self.paddle.width / 2
        self.paddle.y = self.window.height - PADDLE_OFFSET

    def reset_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = random.randint(INITIAL_Y_SPEED, INITIAL_Y_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        if random.random() > 0.5:
            self.__dy = -self.__dy

    def bounce(self):
        for i in range(0, 3, 2):
            for j in range(0, 3, 2):
                obj = self.window.get_object_at(self.ball.x + i*BALL_RADIUS, self.ball.y + j*BALL_RADIUS)
                if obj is not None:
                    if obj is self.paddle:
                        return True
                    else:
                        self.window.remove(obj)   # bricks
                        self.num_brick -= 1
                        return True
        return False

    def move_or_not(self):
        return self.switch

    def switch_open(self, event):
        if not self.switch:
            self.switch = True

    def reset_ball(self):
        self.window.remove(self.ball)
        self.window.add(self.ball, (self.window.width-self.ball_radius*2)/2, (self.window.height-self.ball_radius*2)/2)

    @staticmethod
    def get_vx():
        return random.randint(1, MAX_X_SPEED)

    @staticmethod
    def get_vy():
        return random.randint(INITIAL_Y_SPEED, INITIAL_Y_SPEED)

