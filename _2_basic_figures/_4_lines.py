from cairo_template import *
FILE_NAME = os.path.basename(__file__)

class Shape(Figure):
    def on_draw(self, cr):
        cr.set_source_rgba(1, 0, 0, 1)
        cr.set_line_width(5)

        cr.set_dash([8,16,24])
        cr.move_to(40, 30)  
        cr.line_to(750, 30)
        cr.stroke()

        cr.set_dash([14.0, 6.0])
        cr.move_to(40, 130)
        cr.line_to(750, 130)
        cr.stroke()

        cr.set_dash([1.0])
        cr.move_to(40, 230)
        cr.line_to(750, 230)
        cr.stroke()

app = Shape(FILE_NAME,800,260,transparency=False)
app.write()

