from cairo_template import *
FILE_NAME = os.path.basename(__file__)

class Shape(Figure):
    def on_draw(self, cr):
        cr.set_line_width(12)

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

        cr.set_source_rgb(1, 1, 1)
        cr.set_line_width(1.5)

        cr.move_to(30, 35)
        cr.line_to(30, 145)
        cr.stroke()

        cr.move_to(150, 35)
        cr.line_to(150, 145)
        cr.stroke()

        cr.move_to(155, 35)
        cr.line_to(155, 145)
        cr.stroke()

app = Shape(FILE_NAME,180,180,transparency=False)
app.write()

