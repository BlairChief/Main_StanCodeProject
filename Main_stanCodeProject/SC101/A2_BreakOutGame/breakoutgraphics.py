"""
File: breakoutgraphics.py
Name: Blair
-----------------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 15  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        self.full_mark = brick_rows * brick_cols

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.color = 'dimgray'
        self.paddle.fill_color = 'dimgray'
        self.window.add(self.paddle, x=(self.window.width - self.paddle.width) / 2,
                        y=self.window.height - paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.r = ball_radius
        self.ball.filled = True
        self.ball.color = 'dimgray'
        self.ball.fill_color = 'dimgray'
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # # Initialize variables
        self.game_start = False

        # Initialize our mouse listeners
        onmouseclicked(self.drop_the_ball)
        onmousemoved(self.paddle_slide)

        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                brick = GRect(brick_width, brick_height, x=(brick_width + brick_spacing) * i,
                              y=(brick_height + brick_spacing) * j + brick_offset)
                brick.filled = True
                if j // 2 == 0:
                    brick.fill_color = brick.color = 'blue'
                elif j // 2 == 1:
                    brick.fill_color = brick.color = 'royalblue'
                elif j // 2 == 2:
                    brick.fill_color = brick.color = 'skyblue'
                elif j // 2 == 3:
                    brick.fill_color = brick.color = 'lightsteelblue'
                else:
                    brick.fill_color = brick.color = 'aliceblue'

                self.window.add(brick)

        # Life board
        self.live_board = GLabel('Lives: ')
        self.live_board.font = '-18'
        self.live_board.color = 'dimgray'
        self.window.add(self.live_board, x=self.window.width - 1.5 * self.live_board.width,
                        y=self.live_board.height * 1.5)

        # Scoreboard
        self.scoreboard = GLabel('Score: ')
        self.scoreboard.font = '-30'
        self.scoreboard.color = 'dimgray'
        self.window.add(self.scoreboard, x=10, y=self.scoreboard.height * 1.2)

        # Success announcement
        self.success_sign = GLabel('Nicely Done!')
        self.success_sign.font = '-60'
        self.success_sign.color = 'green'

        # Failure announcement
        self.fail_sign = GLabel('FAIL ^____^')
        self.fail_sign.font = '-60'
        self.fail_sign.color = 'red'

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self, new_dx):
        self.__dx = new_dx

    def set_dy(self, new_dy):
        self.__dy = new_dy

    def drop_the_ball(self, event):
        """
        This function sets the velocity of the ball.
        :param event: the mouse event.
        :return: None
        """
        if not self.game_start:
            self.game_start = True
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def paddle_slide(self, event):
        """
        This function has the paddle slide with its center following the mouse.
        :param event: the mouse event.
        :return: None
        """

        self.paddle.x = event.x - self.paddle.width // 2
        if self.paddle.x <= 0:
            self.paddle.x = 0
        if (self.paddle.x + self.paddle.width) >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
