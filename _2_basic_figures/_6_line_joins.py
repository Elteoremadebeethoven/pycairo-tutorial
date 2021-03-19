import os
import sys
sys.path.append(os.getcwd())
from imports import *
IMAGE_CONFIG = {
    "width": 300,
    "height": 300,
    "scale": 1.8,
    "transparency": False,
}

class Shape(Figure):
    def on_draw(self, cr: cairo.Context):
        cr.set_line_width(14)

        cr.rectangle(30, 30, 100, 100)
        cr.set_line_join(cairo.LINE_JOIN_MITER)
        cr.set_source_rgb(1, 0, 0)
        cr.stroke()

        cr.rectangle(160, 30, 100, 100)
        cr.set_line_join(cairo.LINE_JOIN_BEVEL)
        cr.set_source_rgb(0, 1, 0)
        cr.stroke()

        cr.rectangle(100, 160, 100, 100)
        cr.set_line_join(cairo.LINE_JOIN_ROUND)
        cr.set_source_rgb(0, 0, 1)
        cr.stroke()

if __name__ == "__main__":
    app = Shape(**IMAGE_CONFIG)
    full_path = get_full_path_to_export(os,__file__)
    app.write(full_path)