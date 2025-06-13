from manim import *
class DefaultTemplate(Scene):
    def construct(self):
        
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            x_length=10,
            y_length=6,
            axis_config={"color": WHITE},
            tips=False
        )
        axes.add_coordinates()
        self.add(axes)
        
        # axes = Axes(x_range=[-3,3,1], y_range=[-3,3,1], x_length=6, y_length=6)
        # axes.to_edge(LEFT, buff=0.5)
        
        circle = Circle(stroke_width=6, stroke_color=YELLOW, fill_color=RED_C, fill_opacity=0.8)
        circle.set_width(2).to_edge(DR, buff=0)
        
        circle2 = Circle(1)
        self.play(Write(circle2))

        triangle = Triangle(stroke_color = ORANGE, stroke_width = 10, fill_color = GREY).set_height(2).shift(DOWN*3+RIGHT*3)

        dot = Dot().shift(UP*2 + RIGHT*2)
        self.play(FadeIn(dot))

        self.play(Write(axes))
        self.play(DrawBorderThenFill(circle))
        self.play(circle.animate.set_width(0))
        self.play(Transform(circle, triangle), run_time=3)

        square = Square(2)
        self.play(Write(square))