from manim import *

class MyTimeline(Scene):
    def construct(self):
        # Draw the timeline
        timeline = NumberLine(
            x_range=[1800, 2000, 20],
            length=12,
            include_numbers=True,
            label_direction=DOWN
        )
        self.play(Create(timeline))
        self.wait(1)

        # Key events
        events = [
            (1809, "Darwin Born"),
            (1879, "Edison's Bulb"),
            (1969, "Moon Landing"),
            (1989, "Berlin Wall Falls"),
        ]
        dots = []
        labels = []
        for year, desc in events:
            dot = Dot(timeline.n2p(year), color=YELLOW)
            label = Text(f"{desc}\n{year}", font_size=20).next_to(dot, UP)
            dots.append(dot)
            labels.append(label)

        # Animate events one by one
        for dot, label in zip(dots, labels):
            self.play(FadeIn(dot), Write(label))
            self.wait(0.7)
