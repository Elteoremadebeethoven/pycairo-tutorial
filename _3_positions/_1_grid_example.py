import os
import sys
sys.path.append(os.getcwd())
from imports import *
IMAGE_CONFIG = {
    "width": 400,
    "height": 400,
    "scale": 1.2,
    "transparency": False,
}

class Shape(Figure):
    def on_draw(self, cr: cairo.Context):
        cr.set_source_rgb(1, 1, 1)
        self.set_grid()

if __name__ == "__main__":
    app = Shape(**IMAGE_CONFIG)
    full_path = get_full_path_to_export(os,__file__)
    app.write(full_path)