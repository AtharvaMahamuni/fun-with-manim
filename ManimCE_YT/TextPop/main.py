from manim import *
import random

class BecomingTheBeginner(Scene):
    def construct(self):
        # Helper to create and layout a list of letter mobjects for a word
        def word_letters(word, color, size):
            letters = [Text(char, font_size=size, color=color) for char in word]
            widths = [m.width for m in letters]
            total_width = sum(widths)
            # Calculate center positions for each letter
            left = -total_width / 2
            centers = []
            for w in widths:
                centers.append(left + w / 2)
                left += w
            return letters, centers

        letter_mobs = []
        final_positions = []

        # --- Top Row ---
        top_specs = [
            ("FOR", -3.1, 2.4, RED_C, 28),
            ("BEGINNERS", -1.1, 2.4, RED_C, 28),
        ]
        for word, base_x, base_y, color, size in top_specs:
            letters, xs = word_letters(word, color, size)
            for l, x in zip(letters, xs):
                # random start
                rx, ry = random.uniform(-7, 7), random.uniform(-3.5, 3.5)
                l.move_to([rx, ry, 0])
                letter_mobs.append(l)
                final_positions.append([base_x + x, base_y, 0])

        # --- Main Headline: centered as a whole group ---
        headline_specs = [
            ("WHAT", WHITE, 60),
            ("IS", WHITE, 60),
            ("PROGERAMMING?", WHITE, 60),
        ]
        gap = 0.8  # space between headline words
        # Make all letter mobs and measure widths
        headline_word_letters = []
        headline_word_widths = []
        for word, color, size in headline_specs:
            lets, _ = word_letters(word, color, size)
            w = sum(l.width for l in lets)
            headline_word_letters.append((lets, color, size))
            headline_word_widths.append(w)
        total_headline_width = sum(headline_word_widths) + gap * (len(headline_word_widths) - 1)
        headline_base_y = 0.7
        curr_x = -total_headline_width / 2
        for (lets, color, size), w in zip(headline_word_letters, headline_word_widths):
            # Calculate letter offsets
            xs = []
            left = curr_x
            for l in lets:
                xs.append(left + l.width / 2)
                left += l.width
            for l, x in zip(lets, xs):
                rx, ry = random.uniform(-7, 7), random.uniform(-3.5, 3.5)
                l.move_to([rx, ry, 0])
                letter_mobs.append(l)
                final_positions.append([x, headline_base_y, 0])
            curr_x += w + gap

        # --- "or" ---
        # or_word = "or"
        # or_y = -0.5
        # letters, xs = word_letters(or_word, RED_C, 36)
        # for l, x in zip(letters, xs):
        #     rx, ry = random.uniform(-7, 7), random.uniform(-3.5, 3.5)
        #     l.move_to([rx, ry, 0])
        #     letter_mobs.append(l)
        #     final_positions.append([x, or_y, 0])

        # --- Bottom Row ---
        bottom_specs = [
            ("FOR", 1.1, -2.4, RED_C, 28),
            ("EVERYONE", 3.1, -2.4, RED_C, 28),
       ]
        for word, base_x, base_y, color, size in bottom_specs:
            letters, xs = word_letters(word, color, size)
            for l, x in zip(letters, xs):
                rx, ry = random.uniform(-7, 7), random.uniform(-3.5, 3.5)
                l.move_to([rx, ry, 0])
                letter_mobs.append(l)
                final_positions.append([base_x + x, base_y, 0])

        # --- Animate ---
        for mob in letter_mobs:
            mob.set_opacity(0)
            self.add(mob)

        self.play(LaggedStart(
            *[mob.animate.set_opacity(1) for mob in letter_mobs],
            lag_ratio=0.03,
            run_time=1.3
        ))

        self.wait(0.4)

        self.play(
            *[
                mob.animate.move_to(pos)
                for mob, pos in zip(letter_mobs, final_positions)
            ],
            run_time=2.5,
            rate_func=smooth
        )
        self.wait(2)
