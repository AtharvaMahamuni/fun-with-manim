from manim import *

class CodeExample(Scene):
    def construct(self):
        code = Code(
            "example.java",   # Path to your code file
            language="java",
            background="window",
        )
        self.play(Write(code))
