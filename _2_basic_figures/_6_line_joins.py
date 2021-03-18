from cairo_template import *
FILE_NAME = os.path.basename(__file__)

class Shape(Figure):
    def on_draw(self, cr):
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

app = Shape(FILE_NAME,300,300,transparency=False)
app.write()

