from manim import *

class TubeDiagram(Scene):
    def construct(self):
        # Set up the background grid (blueprint style)
        grid = NumberPlane(
            x_range=[-8, 8, 1], y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.4
            }
        )
        self.add(grid)

        # Draw the vacuum tube outline (approximate)
        tube = VMobject()
        tube.set_points_as_corners([
            [-2, -2, 0], [-2.2, 0, 0], [-1.5, 2.8, 0],
            [0, 3.3, 0], [1.5, 2.8, 0], [2.2, 0, 0],
            [2, -2, 0], [1.8, -2.5, 0], [-1.8, -2.5, 0], [-2, -2, 0]
        ])
        tube.set_stroke(WHITE, width=3)
        tube.set_fill(WHITE, opacity=0.1)
        self.add(tube)

        # Cathode (bottom coil)
        cathode = Line([-0.5, -1.5, 0], [0.5, -1.5, 0], color=WHITE, stroke_width=5)
        cathode_coil = VMobject()
        cathode_coil.set_points_as_corners([
            [-0.5, -1.5, 0], [-0.4, -1.3, 0], [-0.3, -1.7, 0], 
            [-0.2, -1.3, 0], [-0.1, -1.7, 0], [0, -1.3, 0],
            [0.1, -1.7, 0], [0.2, -1.3, 0], [0.3, -1.7, 0], 
            [0.4, -1.3, 0], [0.5, -1.5, 0]
        ])
        cathode_coil.set_stroke(WHITE, width=2)
        self.add(cathode, cathode_coil)

        # Grid (mesh/line above cathode)
        grid_line = Line([-0.8, -0.7, 0], [0.8, -0.7, 0], color=WHITE, stroke_width=3)
        for x in np.linspace(-0.7, 0.7, 7):
            self.add(Line([x, -0.75, 0], [x, -0.65, 0], color=WHITE, stroke_width=1))
        self.add(grid_line)

        # Anode (plate at top)
        anode = Rectangle(width=1.5, height=0.2, color=WHITE, fill_opacity=0.2).move_to([0, 1.5, 0])
        self.add(anode)

        # Leads/wires
        self.add(Line([0, -2.5, 0], [0, -1.5, 0], color=WHITE, stroke_width=2))
        self.add(Line([0, -0.7, 0], [0, -1.5, 0], color=WHITE, stroke_width=2))
        self.add(Line([0, 1.5, 0], [0, 2.8, 0], color=WHITE, stroke_width=2))

        # Labels
        anode_label = Text("Anode", font="Arial", weight=BOLD, color=WHITE).scale(0.7).next_to(anode, RIGHT, buff=1)
        grid_label = Text("Grid", font="Arial", weight=BOLD, color=WHITE).scale(0.7).next_to(grid_line, RIGHT, buff=1)
        cathode_label = Text("Cathode", font="Arial", weight=BOLD, color=WHITE).scale(0.7).next_to(cathode, RIGHT, buff=1)
        self.add(anode_label, grid_label, cathode_label)

        # Negative Voltage
        neg_v = Text("-V", font="Arial", color=WHITE).scale(0.7).next_to([0, -2.5, 0], LEFT)
        self.add(neg_v)

        # Simple battery and bulb (bottom right, as in your diagram)
        battery = VGroup(
            Line([3, -2, 0], [3.5, -2, 0], color=WHITE, stroke_width=3),
            Line([3.5, -2.1, 0], [3.5, -1.9, 0], color=WHITE, stroke_width=3),
            Line([3.7, -2.1, 0], [3.7, -1.9, 0], color=WHITE, stroke_width=1),
        )
        bulb = SVGMobject("lightbulb.svg").scale(0.3).move_to([4.5, -2, 0])
        self.add(battery, bulb)

        # Connecting wires (draw with lines)
        self.add(Line([0, -2.5, 0], [3, -2, 0], color=WHITE, stroke_width=2))
        self.add(Line([3.5, -2, 0], [4.2, -2, 0], color=WHITE, stroke_width=2))
        self.add(Line([4.8, -2, 0], [6, -2, 0], color=WHITE, stroke_width=2))

        # Keep everything on screen
        self.wait(2)
