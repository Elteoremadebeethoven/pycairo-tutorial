import os
import sys
sys.path.append(os.getcwd())
from imports import *
IMAGE_CONFIG = {
    "width": 180,
    "height": 180,
    "scale": 3,
    "transparency": False,
}

class Shape(Figure):
    def on_draw(self, cr: cairo.Context):
        cr.set_line_width(10)

        cr.set_source_rgb(1, 0, 0)
        cr.set_line_cap(cairo.LINE_CAP_BUTT)
        cr.move_to(30, 50)
        cr.line_to(150, 50)
        cr.stroke()

        cr.set_source_rgb(0, 1, 0)
        cr.set_line_cap(cairo.LINE_CAP_ROUND)
        cr.move_to(30, 90)
        cr.line_to(150, 90)
        cr.stroke()

        cr.set_source_rgb(0, 0, 1)
        cr.set_line_cap(cairo.LINE_CAP_SQUARE)
        cr.move_to(30, 130)
        cr.line_to(150, 130)
        cr.stroke()

        cr.set_source_rgba(1, 1, 1,0.5)
        cr.set_line_width(1)

        cr.move_to(30, 35)
        cr.line_to(30, 145)
        cr.stroke()

        cr.move_to(150, 35)
        cr.line_to(150, 145)
        cr.stroke()

        cr.move_to(155, 35)
        cr.line_to(155, 145)
        cr.stroke()

if __name__ == "__main__":
    app = Shape(**IMAGE_CONFIG)
    full_path = get_full_path_to_export(os,__file__)
    app.write(full_path)
