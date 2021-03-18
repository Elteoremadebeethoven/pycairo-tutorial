import cairo
import os
from math import pi as PI
FILE_NAME = os.path.basename(__file__)
WIDTH = 500
HEIGHT = 500
ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
cr = cairo.Context(ims)

w,h = WIDTH, HEIGHT

cr.set_line_width(20)
cr.set_source_rgb(0.7, 0.2, 0.0)

cr.arc(
    w/2,        # x
    h/2,        # y
    100,        # radius
    0,          # start angle
    2*PI        # end angle
)
# Preserve the stroke
cr.stroke_preserve()
# Set the fill color
cr.set_source_rgb(0.3, 0.4, 0.6)
cr.fill()

ims.write_to_png(f"./exports/{FILE_NAME[:-3]}.png")