from manim import *

from manim import config
config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 7.0
config.frame_width = 12.0

class DefaultTemplate(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-15, 15, 1],  # min, max, step
            y_range=[-8, 8, 1],
            axis_config={"color": BLUE}
        )
        self.add(axes)
        
        box = Rectangle(stroke_color=GREEN_C, stroke_opacity=0.7, fill_color=RED_B, fill_opacity=0.5, height=1, width=1)
        
        self.add(box)
        self.play(box.animate.shift(RIGHT*2), run_time=2)
        self.play(box.animate.shift(UP*3), run_time=2)
        self.play(box.animate.shift(DOWN*5+LEFT*5), run_time=2)
        self.play(box.animate.shift(UP*1.5+RIGHT*1), run_time=2)