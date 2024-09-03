"""
File: breakout.py
Name: Blair
----------------------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.
"""
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Number of attempts
POINTS = 0


def main():
    """
    This program executes breakout game.
    """
    live = NUM_LIVES
    points = POINTS
    graphics = BreakoutGraphics()
    graphics.live_board.text = 'Lives: ' + str(live)
    graphics.scoreboard.text = 'Scores: ' + str(points)

    dx = graphics.get_dx()
    dy = graphics.get_dy()

    while True:
        pause(FRAME_RATE)
        if graphics.game_start:
            graphics.game_start = False
            dx = graphics.get_dx()
            dy = graphics.get_dy()

        graphics.ball.move(dx, dy)

        # Hits the side walls and bounces
        if graphics.ball.x <= 0 or (graphics.ball.x + graphics.ball.width) >= graphics.window.width:
            graphics.set_dx(-dx)
            dx = graphics.get_dx()

        # Hits the ceiling and bounces
        if graphics.ball.y <= 0:
            graphics.set_dy(-dy)
            dy = graphics.get_dy()

        # Loses life
        if (graphics.ball.y + graphics.ball.height) >= graphics.window.height:
            graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2,
                                y=(graphics.window.height - graphics.ball.height) / 2)

            graphics.set_dx(0)
            dx = graphics.get_dx()

            graphics.set_dy(0)
            dy = graphics.get_dy()

            live -= 1
            graphics.live_board.text = 'Lives: ' + str(live)

        # Check if the ball hits the paddle or any bricks
        for i in range(2):
            for j in range(2):  # Check for Collisions on 4 corners of the ball
                obj = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width * i,
                                                    graphics.ball.y + graphics.ball.height * j)
                if obj is graphics.paddle:
                    graphics.window.add(graphics.ball, x=graphics.ball.x,
                                        y=graphics.paddle.y - graphics.ball.height - 1)
                    graphics.set_dy(-dy)
                    dy = graphics.get_dy()
                    break
                elif obj is not None and obj is not graphics.live_board and obj is not graphics.scoreboard:
                    graphics.window.remove(obj)
                    points += 1
                    graphics.scoreboard.text = 'Scores: ' + str(points)
                    graphics.set_dy(-dy)
                    dy = graphics.get_dy()
                    break

        # Ends the game
        if live == 0:
            graphics.window.remove(graphics.ball)
            graphics.window.remove(graphics.paddle)
            graphics.window.add(graphics.fail_sign, x=(graphics.window.width - graphics.fail_sign.width) / 2,
                                y=(graphics.window.height - graphics.fail_sign.height) / 2)
            break
        if points == graphics.full_mark:
            graphics.window.remove(graphics.ball)
            graphics.window.remove(graphics.paddle)
            graphics.window.add(graphics.success_sign, x=(graphics.window.width - graphics.success_sign.width) / 2,
                                y=(graphics.window.height - graphics.success_sign.height) / 2)
            break


if __name__ == '__main__':
    main()
