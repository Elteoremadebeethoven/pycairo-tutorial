import cairo
import os
from math import pi as PI

WIDTH = 400
HEIGHT = 400

class Figure:
    def __init__(self, file_name, width=WIDTH, height=HEIGHT, transparency=True):
        if transparency:
            ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        else:
            ims = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
        cr = cairo.Context(ims)
        self.file_name = file_name
        self.on_draw(cr)
        self.ims = ims

    def on_draw(self, cr):
        pass

    def write(self):
        self.ims.write_to_png(f"./exports/{self.file_name[:-3]}.png")
