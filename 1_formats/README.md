# Formats

## Image Surface

```python
import cairo
import os
FILE_NAME = os.path.basename(__file__)
WIDTH = 390
HEIGHT = 60
# - Create surface
ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
# - Create context
cr = cairo.Context(ims)
# - Define color source
cr.set_source_rgb(1, 0, 0)
# ------ Text 1
# - Define some text - 1
cr.select_font_face(
    "Arial",
    cairo.FONT_SLANT_NORMAL,
    cairo.FONT_WEIGHT_NORMAL
)
# - Define font size
cr.set_font_size(50)
# - Define position
cr.move_to(30, 50)
# - Add text to context
cr.show_text("Hello")
# ------ Text 2
cr.select_font_face(
    "Noto Sans",
    cairo.FONT_SLANT_ITALIC,
    cairo.FONT_WEIGHT_NORMAL
)
cr.set_source_rgb(50, 50, 0)
cr.move_to(160, 50)
cr.show_text("World")

ims.write_to_png(f"./1_formats/{FILE_NAME[:-3]}.png")
```

<p align="center"><img src ="../exports/_1_image_surface.png" /></p>

## PDF surface

```python
import cairo
import os
FILE_NAME = os.path.basename(__file__)
WIDTH = 500
HEIGHT = 300
# - Create surface PDF
ps = cairo.PDFSurface(f"./1_formats/{FILE_NAME[:-3]}.pdf", WIDTH, HEIGHT)
cr = cairo.Context(ps)
# - Define color source
cr.set_source_rgb(50, 0, 0)
# ------ Text 1
# - Define some text - 1
cr.select_font_face(
    "Arial",
    cairo.FONT_SLANT_NORMAL,
    cairo.FONT_WEIGHT_NORMAL
)
# - Define font size
cr.set_font_size(50)
# - Define position
cr.move_to(30, 50)
# - Add text to context
cr.show_text("Hello")
# ------ Text 2
cr.select_font_face(
    "Noto Sans",
    cairo.FONT_SLANT_ITALIC,
    cairo.FONT_WEIGHT_BOLD
)
cr.set_source_rgb(0, 200, 10)
cr.move_to(100, 100)
cr.show_text("World")

cr.show_page()
```

## SVG surface

```python
import cairo
import os
FILE_NAME = os.path.basename(__file__)
WIDTH = 500
HEIGHT = 300

ps = cairo.SVGSurface(f"./1_formats/{FILE_NAME[:-3]}.svg", WIDTH, HEIGHT)
cr = cairo.Context(ps)
# - Define color source
cr.set_source_rgb(50, 0, 0)
# ------ Text 1
# - Define some text - 1
cr.select_font_face(
    "Arial",
    cairo.FONT_SLANT_NORMAL,
    cairo.FONT_WEIGHT_NORMAL
)
# - Define font size
cr.set_font_size(50)
# - Define position
cr.move_to(30, 50)
# - Add text to context
cr.show_text("Hello")
# ------ Text 2
cr.select_font_face(
    "Noto Sans",
    cairo.FONT_SLANT_ITALIC,
    cairo.FONT_WEIGHT_BOLD
)
cr.set_font_size(100)
cr.set_source_rgb(50, 0, 10)
cr.move_to(70, 130)
cr.show_text("World")

cr.show_page()
```

## GTK (optional)

```python
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
```