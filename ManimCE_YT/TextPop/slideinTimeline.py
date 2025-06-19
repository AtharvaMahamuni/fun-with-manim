from manim import *
import numpy as np

class SlideInTimeline(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # CONFIGURABLE PARAMETERS
        num_years = 13           # Number of years to show
        year_start = 1900        # Starting year
        year_step = 10           # Step between years
        spread = 20             # Width over which numbers/ticks are distributed
        y_label = 0.5            # Y position for year labels (close to line)
        tick_length = 0.2        # Length of each tick (vertical line)
        timeline_y = 0           # Y position of the timeline (and center of ticks)

        # Generate years and their positions
        years_list = [str(year_start + i * year_step) for i in range(num_years)]
        year_xs = np.linspace(-spread/2, spread/2, num_years)

        # 1. Numbers just above the timeline
        year_labels = VGroup(*[
            Text(year, color=WHITE, font_size=28).move_to([x, y_label, 0])
            for x, year in zip(year_xs, years_list)
        ])
        year_labels.shift(LEFT * 4)  # Start offscreen left
        self.add(year_labels)

        # 2. Timeline (horizontal line) - extra long!
        timeline = Line(LEFT * 25, RIGHT * 25, color=WHITE, stroke_width=4).shift(DOWN * 0.1)

        # 3. Vertical tall ticks
        ticks = VGroup(*[
            Line(
                [x, timeline_y - tick_length, 0],   # Start lower
                [x, timeline_y + tick_length, 0],   # End higher
                color=YELLOW, stroke_width=3
            ) for x in year_xs
        ])
        timeline_group = VGroup(timeline, ticks)
        timeline_group.shift(RIGHT * 4)  # Start offscreen right
        self.add(timeline_group)

        # 4. Animate timeline/ticks and year labels sliding in from opposite sides
        self.play(
            year_labels.animate.shift(RIGHT * 4),
            timeline_group.animate.shift(LEFT * 4),
            run_time=2.5,
            rate_func=smooth
        )
        self.wait(0.5)

        # 5. Highlight the central year and tick
        center_index = num_years // 2
        center_label = year_labels[center_index]
        center_tick = ticks[center_index]
        self.play(
            center_label.animate.set_color(YELLOW).scale(1.2),
            center_tick.animate.set_color(RED).scale(1.5),
            run_time=1
        )
        self.wait(1.5)
