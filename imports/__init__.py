import cairo
from math import pi as PI
import numpy as np
import sys
WIDTH = 400
HEIGHT = 400


def set_grid(cr, step=10, color=(1, 1, 1), stroke=1, opacity=0.3):
    cr.set_source_rgba(*color,opacity)
    cr.set_line_width(stroke)
    for v, s in zip([(1,0),(0,1)],[WIDTH, HEIGHT]):
        for i in np.arange(0, s+step, step):
            vector = np.array(v) * i
            end = vector + np.array(v)[::-1] * s
            cr.move_to(*vector)
            cr.line_to(*end)
            cr.stroke()


class Figure:
    def __init__(self, file_name, width=WIDTH, height=HEIGHT, scale=1, transparency=True):
        cf = cairo.FORMAT_ARGB32 if transparency else cairo.FORMAT_RGB24
        ims = cairo.ImageSurface(cf, int(width*scale), int(height*scale))
        cr = cairo.Context(ims)
        self.file_name = file_name
        self.cr = cr
        cr.scale(scale,scale)
        self.on_draw(cr)
        self.ims = ims

    def on_draw(self, cr: cairo.Context):
        pass

    def write(self):
        self.ims.write_to_png(f"./exports/{self.file_name[:-3]}.png")
