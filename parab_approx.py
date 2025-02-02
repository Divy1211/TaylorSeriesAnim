import numpy as np
from manim import *

from manim_voiceover import VoiceoverScene

from svc import svc


E = np.exp(1)

class ParabApprox(VoiceoverScene):
    def construct(self):
        self.set_speech_service(svc)

        axes = Axes(
            x_range = [-2, 2],
            y_range = [-0.5, 3.5],
            tips = False
        )
        exp_graph = axes.plot(lambda x: np.exp(x), color = GREEN)
        exp_label = axes.get_graph_label(exp_graph, label = r"f(x) = e^x", x_val = 1.5, color = GREEN)

        self.add(axes, axes.x_axis, axes.y_axis, exp_graph, exp_label)

        point1 = Dot(axes.coords_to_point(0, 1))
        label1 = MathTex(r"(0, 1)")
        label1.move_to(point1.get_center() + DOWN * 0.5 + RIGHT * 0.6)

        point2 = Dot(axes.coords_to_point(1, E))
        label2 = MathTex(r"(1, e)")
        label2.move_to(point2.get_center() + UP * 0.25 + LEFT * 0.6)

        point3 = Dot(axes.coords_to_point(0.5, E**0.5))
        label3 = MathTex(r"(0.5, \sqrt{e})")
        label3.move_to(point3.get_center() + RIGHT * 1.25)

        parab_graph = axes.plot(lambda x: (2*E - 4*E**0.5 + 2)*x**2 + (4*E**0.5 - E - 3)*x + 1, color = BLUE)
        parab_label = axes.get_graph_label(parab_graph, label = r"\hat{f}(x) = (2e - 4\sqrt{e} + 2)x^2 + (4\sqrt{e} - e - 3)x + 1", x_val = -2, direction = RIGHT, color = BLUE)
        parab_label.move_to(parab_label.get_center() + UP + LEFT)

        self.play(Write(point1), Write(label1), Write(point2), Write(label2))
        with self.voiceover(text = (
            "How about if we increase the number of points that we sampled? Let's try three <bookmark mark='A'/>. Once"
            " again, if we <bookmark mark='B'/> couldn't see the function and only these three points, what could be"
            " our best guess as to what the real function might look like? If you said a <bookmark mark='C'/> parabola,"
            " you'd be correct!"
        )):
            self.wait_until_bookmark("A")
            self.play(Write(point3), Write(label3))
            self.wait_until_bookmark("B")
            self.play(FadeOut(exp_graph, exp_label))
            self.wait_until_bookmark("C")
            self.play(Write(parab_graph), Write(parab_label))
            self.wait(1)
            self.play(FadeIn(exp_graph, exp_label))

        axes2 = Axes(
            x_range = [-4, 4],
            y_range = [-0.5, 7.5],
            tips = False
        )
        exp_graph2 = axes2.plot(lambda x: np.exp(x), color = GREEN)
        exp_label2 = axes2.get_graph_label(exp_graph2, label = r"f(x) = e^x", x_val = 2.5, color = GREEN)

        point21 = Dot(axes2.coords_to_point(0, 1))
        label21 = MathTex(r"(0, 1)")
        label21.move_to(point21.get_center() + DOWN * 0.5 + RIGHT * 0.6)

        point22 = Dot(axes2.coords_to_point(1, E))
        label22 = MathTex(r"(1, e)")
        label22.move_to(point22.get_center() + UP * 0.25 + LEFT * 0.6)

        point23 = Dot(axes2.coords_to_point(0.5, E ** 0.5))
        label23 = MathTex(r"(0.5, \sqrt{e})")
        label23.move_to(point23.get_center() + RIGHT * 1.25)

        parab_graph2 = axes2.plot(
            lambda x: (2 * E - 4 * E ** 0.5 + 2) * x ** 2 + (4 * E ** 0.5 - E - 3) * x + 1, color = BLUE
        )
        parab_label2 = axes2.get_graph_label(
            parab_graph2, label = r"\hat{f}(x) = (2e - 4\sqrt{e} + 2)x^2 + (4\sqrt{e} - e - 3)x + 1", x_val = -4,
            direction = RIGHT, color = BLUE
        )
        parab_label2.move_to(parab_label2.get_center() + UP * 0.5 + LEFT * 0.5)

        new_label1 = MathTex(r"(x_1, y_1)")
        new_label2 = MathTex(r"(x_2, y_2)")
        new_label3 = MathTex(r"(x_3, y_3)")

        new_label1.align_on_border(UP + LEFT)
        new_label2.next_to(new_label1, RIGHT)
        new_label3.next_to(new_label2, RIGHT)

        new_parab_label = MathTex(r"\hat{f}(x) = a_0x^2 + a_1x + a_2")
        new_parab_label.next_to(new_label1, DOWN)
        new_parab_label.align_on_border(LEFT)

        with self.voiceover(text = (
            "This approximation seems to already be doing much better! <bookmark mark='A'/> Let's play around with it"
            " and attempt to generalize it as well."
        )):
            self.play(
                Transform(axes, axes2),
                exp_graph.animate.become(exp_graph2),
                parab_graph.animate.become(parab_graph2),
                Transform(exp_label, exp_label2), Transform(parab_label, parab_label2),
                Transform(point1, point21), Transform(label1, label21),
                Transform(point2, point22), Transform(label2, label22),
                Transform(point3, point23), Transform(label3, label23),
            )
            self.wait_until_bookmark("A")
            self.play(
                Transform(label1, MathTex(r"(x_1, y_1)").move_to(label1.get_center() + LEFT * 0.2)),
                Transform(label3, MathTex(r"(x_2, y_2)").move_to(label3.get_center() + RIGHT * 0.2)),
                Transform(label2, MathTex(r"(x_3, y_3)").move_to(label2.get_center() + LEFT * 0.2)),
                Transform(parab_label, MathTex(r"\hat{f}(x) = a_0x^2 + a_1x + a_2").move_to(parab_label2.get_center() + LEFT)),
            )

            self.wait(2)

            self.play(
                Transform(label1, new_label1), Transform(label2, new_label3),
                Transform(label3, new_label2), Transform(parab_label, new_parab_label),
                FadeOut(axes, exp_graph, parab_graph, exp_label, point1, point2, point3)
            )

        return [label1, label2, label3, parab_label]
