from manim import *

from manim_voiceover import VoiceoverScene

from svc import svc

E = np.exp(1)

class LinearApprox(VoiceoverScene):
    def construct(self):
        self.set_speech_service(svc)

        axes = Axes(
            x_range = [-2, 2],
            y_range = [-0.5, 3.5],
            tips = False
        )
        exp_graph = axes.plot(lambda x: np.exp(x), color = GREEN)
        exp_label = axes.get_graph_label(exp_graph, label = r"f(x) = e^x", x_val = 1, color = GREEN)
        exp_graph.add(exp_label)

        with self.voiceover(text = (
            "With that out of the way, let's get right to it! <bookmark mark='A'/> let's say we want to approximate the"
            " function <bookmark mark='B'/> e to the x, what is the easiest approximation to make?"
        )):
            self.wait_until_bookmark("A")
            self.play(Write(axes.x_axis), Write(axes.y_axis))
            self.wait_until_bookmark("B")
            self.play(Write(exp_graph))

        point1 = Dot(axes.coords_to_point(0, 1))
        label1 = MathTex(r"(0, 1)")
        label1.move_to(point1.get_center() + DOWN * 0.5 + RIGHT * 0.6)
        # point1.add(label1)

        const_graph = axes.plot(lambda x: 1, color = BLUE)
        const_label = axes.get_graph_label(const_graph, label = r"\hat{f}(x) = 1", x_val = -0.5, direction = UP, color = BLUE)
        const_graph.add(const_label)

        with self.voiceover(text = (
            "A constant! we'll just sample our function at one point, say <bookmark mark='A'/> x = 0, and that'll be"
            " the approximation."
        )):
            self.wait_until_bookmark("A")
            self.play(Write(point1), Write(label1))
            self.play(Write(const_graph))

        point2 = Dot(axes.coords_to_point(1, E))
        label2 = MathTex(r"(1, e)")
        label2.move_to(point2.get_center() + UP * 0.25 + LEFT * 0.6)
        # point2.add(label2)

        line_graph = axes.plot(lambda x: 1 + (E - 1)*x, color = BLUE)
        line_label = axes.get_graph_label(line_graph, label = r"\hat{f}(x) = 1 + (e - 1) x", x_val = -1, direction = RIGHT, color = BLUE)
        line_label.move_to(line_label.get_center() + RIGHT * 0.1)
        # line_graph.add(line_label)
        with self.voiceover(text = (
            "Okay, admittedly, this isn't very good. It's only correct at <bookmark mark='A'/> one point, and it"
            " diverges quite quickly. Is there any way we can do better? Perhaps an approximation that is correct at"
            " two points? It's not much better, but it's a start! Lets sample another point, say <bookmark mark='B'/>"
            " x = 1. Now If we couldn't <bookmark mark='C'/> see the real function, given two points, what would be"
            " our best guess as to what this function could look like? <bookmark mark='D'/> If you said a line you'd be"
            " correct!"
        )):
            self.wait_until_bookmark("A")
            self.play(Indicate(point1), Indicate(label1))
            self.wait_until_bookmark("B")
            self.play(Write(point2), Write(label2))
            self.wait_until_bookmark("C")
            self.play(FadeOut(exp_graph), FadeOut(const_graph))
            self.wait_until_bookmark("D")
            self.play(Write(line_graph), Write(line_label))
            self.wait(1)
            self.play(FadeIn(exp_graph))

        two_point_form = MathTex(r"\hat{f}(x) = y_1 + \cfrac{y_2 - y_1}{x_2 - x_1}(x - x_1)")
        two_point_form.align_on_border(LEFT + UP)

        with self.voiceover(text = (
            "Let's generalise this approximation to any two points, <bookmark mark='A'/> x1 y1 and <bookmark mark='B'/>"
            " x2 y2, and we'll start using the general <bookmark mark='C'/> two point form of the line."
        )):

            self.wait_until_bookmark("A")
            self.play(Transform(label1, MathTex(r"(x_1, y_1)").move_to(label1.get_center() + RIGHT * 0.2)))
            self.wait_until_bookmark("B")
            self.play(Transform(label2, MathTex(r"(x_2, y_2)").move_to(label2.get_center() + LEFT * 0.2)))
            self.wait_until_bookmark("C")
            self.play(Transform(
                line_label,
                MathTex(r"\hat{f}(x) = y_1 + \cfrac{y_2 - y_1}{x_2 - x_1}(x - x_1)", color = BLUE)
                    .move_to(line_label.get_center() + RIGHT)
            ))

        with self.voiceover(text = (
            "Let's play with this two point form a little bit to see if we can somehow make it easier to work with."
        )):
            self.play(
                FadeOut(axes, exp_graph, exp_label, line_graph, point1, label1, point2, label2),
                ReplacementTransform(line_label, two_point_form)
            )

        return [two_point_form]
