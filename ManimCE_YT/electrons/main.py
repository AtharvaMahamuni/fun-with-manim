from manim import *
import numpy as np

class SubtleElectronBackground(Scene):
    def construct(self):
        num_electrons = 1000
        # Settings for subtlety
        electron_radius = 0.09
        electron_color = GRAY_BROWN .opacity(0.002)
        orbit_radius = 2.5  # Spread out orbits
        duration = 0.7  # Slow movement

        electrons = VGroup()
        for i in range(num_electrons):
            # Place electrons in random orbits/angles
            angle = np.random.uniform(0, 2*np.pi)
            r = np.random.uniform(orbit_radius * 0.7, orbit_radius * 1.2)
            center = np.random.uniform(-5, 5), np.random.uniform(-3, 3)
            dot = Dot(
                point=[center[0] + r * np.cos(angle), center[1] + r * np.sin(angle), 0],
                radius=electron_radius,
                color=electron_color
            )
            electrons.add(dot)

        self.add(electrons)  # Add electrons as the bottom layer

        # Animate all electrons on their own gentle circular path
        animations = []
        for i, dot in enumerate(electrons):
            # Each gets its own subtle orbit
            center = dot.get_center() - (orbit_radius * np.array([np.cos(0), np.sin(0), 0]))
            orbit_angle = np.random.uniform(0, 2*np.pi)
            orbit_center = dot.get_center() + np.array([
                np.cos(orbit_angle) * 0.6,
                np.sin(orbit_angle) * 0.6,
                0
            ])
            def make_updater(dot, center=orbit_center, phase=orbit_angle):
                return lambda m, dt: m.move_to(center + np.array([
                    np.cos(phase + self.time / duration) * orbit_radius * 0.12,
                    np.sin(phase + self.time / duration) * orbit_radius * 0.12,
                    0
                ]))
            dot.add_updater(make_updater(dot))

        # Let the electrons swirl softly in the background
        self.wait(15)  # You can adjust to how long you want the animation

        # When you add more animation or drawing, just add it after this block
        # Example: Draw a circle above the background
        # self.play(Create(circle))
        
        circle = Circle(radius=1.5, color=YELLOW).set_stroke(width=5)
        self.play(Create(circle), run_time=2)
        self.wait(0.5)
        self.play(circle.animate.shift(RIGHT * 2).set_color(RED), run_time=2)
        self.wait(1)

        # Everything plays together for the duration
        self.wait(10)
