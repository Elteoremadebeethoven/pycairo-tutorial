import os
import sys
sys.path.append(os.getcwd())
from imports import *
IMAGE_CONFIG = {
    "width": 500,
    "height": 500,
    "scale": 1,
}

class Shape(Figure):
    def on_draw(self, cr: cairo.Context):
        w,h = self.width, self.height
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

if __name__ == "__main__":
    app = Shape(**IMAGE_CONFIG)
    full_path = get_full_path_to_export(os,__file__)
    app.write(full_path)
