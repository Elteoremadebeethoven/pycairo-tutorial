import os
import sys
sys.path.append(os.getcwd())
from imports import *
IMAGE_CONFIG = {
    "width": 800,
    "height": 800,
    "scale": 1, # default
    "transparency": True # default
}

class Shape(Figure):
    def on_draw(self, cr: cairo.Context):
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

if __name__ == "__main__":
    app = Shape(**IMAGE_CONFIG)
    full_path = get_full_path_to_export(os,__file__)
    app.write(full_path)
