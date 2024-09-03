"""
File: babygraphics.py
Name: Blair
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]

GRAPH_MARGIN_SIZE = 20
COLORS = ['royalblue', 'thistle', 'plum', 'lightskyblue']

TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    gap = (width - GRAPH_MARGIN_SIZE * 2) // len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * gap
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE + TEXT_DX,
                           text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # make the datatypes the same to be comparable
    yn = list(map(lambda year: str(year), YEARS))
    # fit rank positions to the canvas's height
    scale = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / MAX_RANK
    for i in range(len(lookup_names)):
        lookup_name = lookup_names[i]
        # recycle the color sheet
        color = COLORS[i % len(COLORS)]
        # Start checking
        if lookup_name in name_data:
            name_data_l = name_data[lookup_name]
            # fill the blank data
            for year in yn:
                if year not in name_data_l:
                    name_data_l[year] = '*'
            line_base_l = sorted(name_data_l.items())
            for j in range(len(line_base_l) - 1):
                y1_base = line_base_l[j][1]
                y2_base = line_base_l[j + 1][1]
                yend_base = line_base_l[len(line_base_l) - 1][1]
                if y1_base == '*':
                    y1_add = MAX_RANK
                else:
                    y1_add = int(y1_base)
                if y2_base == '*':
                    y2_add = MAX_RANK
                else:
                    y2_add = int(y2_base)
                if yend_base == '*':
                    yend_add = MAX_RANK
                else:
                    yend_add = int(yend_base)
                canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j), GRAPH_MARGIN_SIZE + y1_add * scale,
                                   get_x_coordinate(CANVAS_WIDTH, j + 1), GRAPH_MARGIN_SIZE + y2_add * scale,
                                   width=LINE_WIDTH, fill=color)
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j) + TEXT_DX, GRAPH_MARGIN_SIZE + y1_add * scale,
                                   text=str(lookup_name) + ' ' + str(y1_base), anchor=tkinter.SW, fill=color)
            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, len(line_base_l) - 1),
                               GRAPH_MARGIN_SIZE + yend_add * scale, text=str(lookup_name) + ' ' + str(yend_base),
                               anchor=tkinter.SW, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
