import cairo
import os
FILE_NAME = os.path.basename(__file__)
WIDTH = 800
HEIGHT = 800
# - Create surface
ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
# - Create context
cr = cairo.Context(ims)
# ---- FIRST RECTANGLE
# Set stroke width
cr.set_line_width(40)
# Set stroke color
cr.set_source_rgb(1, 0.5, 0)
# Set the figure
#             x     y   w    h
cr.rectangle(150, 80, 400, 500)
cr.stroke_preserve() # With this line the stroke is not removed
# Set the fill color
cr.set_source_rgb(0, 0.5, 0.5)
# Create the rectangle with fill and stroke
cr.fill()
# ----- SECOND RECTANGLE
cr.rectangle(250, 50, 400, 600)
cr.set_source_rgb(0.2, 0, 0)
# Create rectangle as stroke
cr.stroke()


ims.write_to_png(f"./exports/{FILE_NAME[:-3]}.png")
