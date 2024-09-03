"""
File: best_photoshop_award.py
Name: Blair
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

THRESHOLD = 1.18
BLACK = 180


def main():
    """
    Creative concept：Feelings of finishing all the assignments.
    """
    fig = SimpleImage("image_contest/fig.jpg")
    bg = SimpleImage("image_contest/heaven.jpeg")
    bg.make_as_big_as(fig)
    new_img = combine(fig, bg)
    new_img.show()


def combine(fig, bg):
    """
    : param1 fig: SimpleImage, green screen figure image
    : param1 bg: SimpleImage, the background image
    : return fig: SimpleImage, the green screen pixels are replaced by pixels of background image
    """
    for x in range(fig.width):
        for y in range(fig.height):
            fig_pixel = fig.get_pixel(x, y)
            avg = (fig_pixel.red + fig_pixel.green + fig_pixel.blue) // 3
            total = fig_pixel.red + fig_pixel.green + fig_pixel.blue
            if fig_pixel.green > avg * THRESHOLD and total > BLACK:
                # Green Screen
                bg_pixel = bg.get_pixel(x, y)
                fig_pixel.red = bg_pixel.red
                fig_pixel.green = bg_pixel.green
                fig_pixel.blue = bg_pixel.blue
    return fig


if __name__ == '__main__':
    main()
