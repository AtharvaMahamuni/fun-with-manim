from manim import *


class CreateCircle(Scene):
    
    def construct(self):
        square = Square()
        square.set_shade_in_3d(BLUE)
        self.play(Create(square))