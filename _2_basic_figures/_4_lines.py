import os
import sys
sys.path.append(os.getcwd())
from imports import *
FILE_NAME = os.path.basename(__file__)
IMAGE_CONFIG = {
    "width": 800,
    "height": 260,
    "transparency": False,
}


class Shape(Figure):
    def on_draw(self, cr: cairo.Context):
        cr.set_source_rgb(1, 0, 0)
        cr.set_line_width(5)
        cr.save()

        cr.set_dash([8,16,24])
        cr.move_to(40, 30)  
        cr.line_to(750, 30)
        cr.stroke()

        cr.set_dash([14.0, 6.0])
        cr.move_to(40, 130)
        cr.line_to(750, 130)
        cr.stroke()

        cr.restore()
        cr.move_to(40, 230)
        cr.line_to(750, 230)
        cr.stroke()

app = Shape(FILE_NAME,**IMAGE_CONFIG)
app.write()

