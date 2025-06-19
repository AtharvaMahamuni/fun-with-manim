from manim import *

class EndScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Try a clean, minimal sans font
        font_name = "Montserrat"  # Replace with any installed font you like

        the_end = Text(
            "The End",
            font_size=54,     # Small, cinematic
            color=BLACK,
            font=font_name,   # Use your chosen font
            weight=BOLD       # Optional: BOLD or other weights if supported
        )
        self.add(the_end)

        cover = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_color=BLACK,
            fill_opacity=0.0,
            stroke_opacity=0.0,
        )
        self.add(cover)
        self.bring_to_back(cover)

        self.wait(1)

        self.play(
            cover.animate.set_fill(opacity=1.0),
            the_end.animate.set_color(WHITE),
            run_time=2,
            rate_func=smooth,
        )

        self.camera.background_color = BLACK
        self.remove(cover)
        self.wait(1.5)
