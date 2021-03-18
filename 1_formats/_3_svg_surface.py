import cairo
import os
FILE_NAME = os.path.basename(__file__)
WIDTH = 500
HEIGHT = 300

ps = cairo.SVGSurface(f"./1_formats/{FILE_NAME[:-3]}.svg", WIDTH, HEIGHT)
cr = cairo.Context(ps)
# - Define color source
cr.set_source_rgb(50, 0, 0)
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
    cairo.FONT_WEIGHT_BOLD
)
cr.set_font_size(100)
cr.set_source_rgb(50, 0, 10)
cr.move_to(70, 130)
cr.show_text("World")

cr.show_page()