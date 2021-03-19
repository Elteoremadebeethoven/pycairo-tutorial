from .basic_libs import *

class Figure:
    def __init__(self, width=400, height=400, scale=1, transparency=True):
        # Transparency config
        cf = cairo.FORMAT_ARGB32 if transparency else cairo.FORMAT_RGB24
        # Define image surface
        ims = cairo.ImageSurface(cf, int(width*scale), int(height*scale))
        # Create context
        cr = cairo.Context(ims)
        self.width, self.height = width, height
        self.cr = cr
        # Set scale
        cr.scale(scale,scale)
        # Draw (abstract method)
        self.on_draw(cr)
        self.ims = ims

    def on_draw(self, cr: cairo.Context):
        pass

    def write(self,full_path):
        self.ims.write_to_png(f"{full_path[:-2]}png")

    def get_context(self):
        return self.cr

    def set_grid(self, step=10, color=(1, 1, 1), stroke=1, opacity=0.3):
        cr = self.get_context()
        cr.set_source_rgba(*color,opacity)
        cr.set_line_width(stroke)
        for v, s in zip([(1,0),(0,1)],[self.width, self.height]):
            for i in np.arange(0, s+step, step):
                vector = np.array(v) * i
                end = vector + np.array(v)[::-1] * s
                cr.move_to(*vector)
                cr.line_to(*end)
                cr.stroke()
