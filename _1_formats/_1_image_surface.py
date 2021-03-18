import cairo
import os
FILE_NAME = os.path.basename(__file__)
WIDTH = 390
HEIGHT = 60
# - Create surface
ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
# - Create context
cr = cairo.Context(ims)
# - Define color source
cr.set_source_rgb(1, 0, 0)
# ------ Text 1
# - Define some text - 1
cr.select_font_face(
    "Arial",
    cairo.FONT_SLANT_NORMAL,
    cairo.FONT_WEIGHT_NORMAL
)
# - Define font size
cr.set_font_size(50)
# - Define position
cr.move_to(30, 50)
# - Add text to context
cr.show_text("Hello")
# ------ Text 2
cr.select_font_face(
    "Noto Sans",
    cairo.FONT_SLANT_ITALIC,
    cairo.FONT_WEIGHT_NORMAL
)
cr.set_source_rgb(1, 1, 0)
cr.move_to(160, 50)
cr.show_text("World")

ims.write_to_png(f"./exports/{FILE_NAME[:-3]}.png")
