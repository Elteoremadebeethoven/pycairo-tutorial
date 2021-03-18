from gi.repository import Gtk
import cairo
# Installation: https://pygobject.readthedocs.io/en/latest/getting_started.html
# Tutorial: https://zetcode.com/gfx/pycairo/backends/

'''
ZetCode PyCairo tutorial 

This program uses PyCairo to 
draw on a window in GTK.

Author: Jan Bodnar
Website: zetcode.com
'''


class Example(Gtk.Window):

    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        darea = Gtk.DrawingArea()
        darea.connect("draw", self.on_draw)
        self.add(darea)

        self.set_title("My first GTK window")
        self.resize(420, 120)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_draw(self, wid, cr):
        cr.set_source_rgb(5, 0, 0)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL,
            cairo.FONT_WEIGHT_NORMAL)
        cr.set_font_size(40)
        
        cr.move_to(60, 50)
        cr.show_text("Hello world")

def main():
    app = Example()
    Gtk.main()

if __name__ == "__main__":
    main()