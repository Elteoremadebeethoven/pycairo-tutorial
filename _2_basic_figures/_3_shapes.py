import os
import sys
sys.path.append(os.getcwd())
from imports import *
IMAGE_CONFIG = {
    "width": 400,
    "height": 230,
    "scale": 1.8,
    "transparency": False,
}

class Shape(Figure):
    def on_draw(self, cr: cairo.Context):
        cr.set_source_rgb(1, 1, 1)

        cr.rectangle(20, 20, 120, 80)
        cr.rectangle(180, 20, 80, 80)
        cr.fill()

        cr.arc(330, 60, 40, 0, 2*PI)
        cr.fill()
        
        cr.arc(90, 160, 40, PI/4, PI)
        cr.fill()

        cr.translate(220, 180)
        cr.scale(1, 0.7)
        cr.arc(0, 0, 50, 0, 2*PI)
        cr.fill()

if __name__ == "__main__":
    app = Shape(**IMAGE_CONFIG)
    full_path = get_full_path_to_export(os,__file__)
    app.write(full_path)
