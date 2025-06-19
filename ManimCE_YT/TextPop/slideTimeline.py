from manim import *

class SlidingTimeline(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Timeline and events
        event_positions = [-4, -2, 0, 2, 4]
        event_years = ["1900", "1947", "1971", "2000", "2024"]
        highlight_index = 2  # index of the year to highlight (1971 in center)

        # Timeline line and dots as a group
        timeline = Line(LEFT * 5, RIGHT * 5, color=WHITE, stroke_width=4)
        dots = VGroup(*[Dot(point=[x, 0, 0], color=YELLOW, radius=0.12) for x in event_positions])
        timeline_group = VGroup(timeline, *dots)
        self.play(Create(timeline))
        self.play(LaggedStart(*[FadeIn(dot) for dot in dots], lag_ratio=0.15))

        # Years (Text objects), each anchored at a fixed spot on screen
        labels = []
        for i, (x, year) in enumerate(zip(event_positions, event_years)):
            y_offset = 0.8 if i % 2 == 0 else -1.1
            label = Text(year, color=WHITE, font_size=32).move_to([x, y_offset, 0])
            self.add(label)
            labels.append(label)

        self.wait(1)

        # Shift the timeline so that the highlight event comes to the center (ORIGIN)
        highlight_x = event_positions[highlight_index]
        shift_amount = -highlight_x  # shift so highlight_x moves to 0

        self.play(
            timeline_group.animate.shift(RIGHT * shift_amount),
            run_time=2,
            rate_func=smooth
        )
        self.wait(0.5)

        # Highlight the year at the center
        highlight_label = labels[highlight_index]
        self.play(
            highlight_label.animate.set_color(YELLOW).scale(1.3),
            run_time=1
        )
        self.wait(2)
