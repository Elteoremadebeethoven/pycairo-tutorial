from cairo_template import *
FILE_NAME = os.path.basename(__file__)

class Shape(Figure):
    def on_draw(self, cr):
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

app = Shape(FILE_NAME,400,250)
app.write()
