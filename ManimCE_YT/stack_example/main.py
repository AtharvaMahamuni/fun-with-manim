from manim import *

class StackPushPopAnimated(Scene):
    def construct(self):
        # Pseudo-code steps
        pseudo_code = [
            "Initialize empty stack",
            "PUSH 1",
            "PUSH 2",
            "POP",
            "PUSH 3"
        ]
        
        # Create the pseudo-code on the left
        code_text = VGroup(*[
            Text(line, font="Monospace", font_size=36).set_opacity(0.6)
            for line in pseudo_code
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.35).to_edge(LEFT)

        self.add(code_text)
        
        # Position for stack visualization
        stack_origin = ORIGIN + RIGHT * 3
        stack_vgroup = VGroup()
        self.add(stack_vgroup)

        # Helper to highlight current pseudo-code step
        def highlight_line(idx):
            for i, line in enumerate(code_text):
                line.set_opacity(1.0 if i == idx else 0.6)
                line.set_color(YELLOW if i == idx else WHITE)
        
        # Stack as Python list and corresponding rectangles
        stack = []
        rectangles = []

        def animate_push(value):
            # Position above the current stack top
            target_y = len(stack) * 0.7
            rect = Rectangle(width=1, height=0.6, color=BLUE, fill_opacity=0.7)
            rect.move_to(stack_origin + UP * (target_y + 1))  # Start above stack
            label = Text(str(value), font_size=32).move_to(rect.get_center())
            group = VGroup(rect, label)
            rectangles.append(group)
            self.add(group)
            # Animate falling into place and fading in
            self.play(
                group.animate.move_to(stack_origin + UP * target_y),
                FadeIn(group),
                run_time=0.5
            )
            stack.append(value)

        def animate_pop():
            if not stack:
                return
            top_group = rectangles.pop()
            # Flash red and fade out
            self.play(
                top_group.animate.set_color(RED),
                run_time=0.2
            )
            self.play(
                FadeOut(top_group),
                run_time=0.3
            )
            stack.pop()

        # Initialize: empty stack
        highlight_line(0)
        self.wait(0.7)

        # PUSH 1
        highlight_line(1)
        animate_push(1)
        self.wait(0.7)

        # PUSH 2
        highlight_line(2)
        animate_push(2)
        self.wait(0.7)

        # POP
        highlight_line(3)
        animate_pop()
        self.wait(0.7)

        # PUSH 3
        highlight_line(4)
        animate_push(3)
        self.wait(1.2)

        # Remove highlight at end
        for line in code_text:
            line.set_opacity(0.6)
            line.set_color(WHITE)

        # Optional: Add "Stack Top" annotation
        arrow = Arrow(
            start=stack_origin + UP * (len(stack) * 0.7 + 0.6),
            end=stack_origin + UP * (len(stack) * 0.7),
            buff=0.1,
            color=YELLOW
        )
        label = Text("Top", font_size=28).next_to(arrow, UP, buff=0.1)
        self.play(FadeIn(arrow), FadeIn(label))
        self.wait(1.5)

