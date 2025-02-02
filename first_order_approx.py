import numpy as np
from manim import *

from manim_voiceover import VoiceoverScene

from svc import svc


E = np.exp(1)

class FirstOrderApprox(VoiceoverScene):
    def construct(self):
        self.set_speech_service(svc)

        # tpf = two point form
        tpf = MathTex(r"\hat{f}(x) = f(x_1) + {f(x_1 + h) - f(x_1) \over h}(x - x_1)")
        tpf.align_on_border(LEFT + UP)

        self.add(tpf)

        tpf_derivative = MathTex(r"\hat{f}(x) {{=}} f(x_1) {{+}} {f(x_1 + h) - f(x_1) \over h} {{(x - x_1)}}")
        tpf_derivative.set_color_by_tex(r"x_1 + h", RED)
        tpf_derivative.align_on_border(LEFT + UP)

        with self.voiceover(text = (
            "Hey, after all is said and done, the <bookmark mark='A'/> expression for the slope of this line looks"
            " suspiciously like the definition of the derivative taken at the point x1!"
        )):
            self.wait_until_bookmark("A")
            self.play(TransformMatchingTex(tpf, tpf_derivative))

        tpf_limit = MathTex(
            r"\lim\limits_{h \to 0} {{\hat{f}(x)}} {{=}} \lim\limits_{h \to 0} {{\left[}} f(x_1) {{+}} {f(x_1 + {{ {h} }}) - f(x_1) \over {{ {h} }} } {{(x - x_1)}} \right]"
        )
        tpf_limit.set_color_by_tex(r"x_1 + h", RED)
        tpf_limit.set_color_by_tex(r"\lim", GREEN)
        tpf_limit.set_color_by_tex(r"{h}", GREEN)
        tpf_limit.align_on_border(LEFT + UP)

        tpf_simpl = MathTex(r"\hat{f}(x) {{=}} f(x_1) {{+}} \lim\limits_{h \to 0} {{\left[}} {f(x_1 + {{ {h} }}) - f(x_1) \over {{ {h} }} } {{\right]}} (x - x_1)")
        tpf_simpl.set_color_by_tex(r"x_1 + h", RED)
        tpf_simpl.set_color_by_tex(r"\lim", RED)
        tpf_simpl.set_color_by_tex(r"\left[", RED)
        tpf_simpl.set_color_by_tex(r"{h}", RED)
        tpf_simpl.set_color_by_tex(r"\right]", RED)
        tpf_simpl.align_on_border(LEFT + UP)

        first_order = MathTex(r"\hat{f}(x) {{=}} f(x_1) {{+}} f'(x_1) {{(x - x_1)}}")
        first_order.set_color_by_tex(r"f'(x_1)", RED)
        first_order.align_on_border(LEFT + UP)

        with self.voiceover(text = (
            "The only thing missing is the limit, so let's <bookmark mark='A'/> take the limit! Now This may feel a"
            " little arbitrary, but recognising patterns and exploring things that look similar is a big part of"
            " inventing new maths!"
        )):
            self.wait_until_bookmark("A")
            self.play(TransformMatchingTex(tpf_derivative, tpf_limit))

        self.play(TransformMatchingTex(tpf_limit, tpf_simpl))
        self.play(TransformMatchingTex(tpf_simpl, first_order))

        const = MathTex(r"x_1 = 0", color = YELLOW)
        const.next_to(first_order, DOWN)
        const.align_on_border(LEFT)

        eq1 = MathTex(r"\hat{f}(x) {{=}} f(0) {{+}} f'(0) {{(x - 0)}}")
        eq1.set_color_by_tex("x_1", GRAY)
        eq1.next_to(const, DOWN)
        eq1.align_on_border(LEFT)

        eq2 = MathTex(r"\hat{f}(x) {{=}} e^0 {{+}} e^0 {{x}}")
        eq2.set_color_by_tex("x_1", GRAY)
        eq2.next_to(const, DOWN)
        eq2.align_on_border(LEFT)

        eq3 = MathTex(r"\hat{f}(x) {{=}} 1 {{+}} x")
        eq3.set_color_by_tex("x_1", GRAY)
        eq3.next_to(const, DOWN)
        eq3.align_on_border(LEFT)

        axes = Axes(
            x_range = [-2, 2],
            y_range = [-0.5, 3.5],
            tips = False
        )
        exp_graph = axes.plot(lambda x: np.exp(x), color = GREEN)
        exp_label = axes.get_graph_label(exp_graph, label = r"f(x) = e^x", x_val = 1.5, color = GREEN)
        exp_graph.add(exp_label)

        line_graph = axes.plot(lambda x: 1 + x, color = BLUE)
        line_label = axes.get_graph_label(line_graph, label = r"\hat{f}(x) = 1 + x", x_val = 0, direction = RIGHT, color = BLUE)
        line_label.move_to(line_label.get_center() + RIGHT * 0.1)
        line_graph.add(line_label)

        with self.voiceover(text = (
            "And look! We've arrived at a linear approximation which only uses one point, x1! If we"
            " plug in zero for x1 <bookmark mark='A'/>, we can now go back to the original graph, and see what it looks"
            " like!"
        )):
            self.wait_until_bookmark("A")
            self.play(Write(const))
            self.play(Write(eq1))
            self.play(TransformMatchingTex(eq1, eq2))
            self.play(TransformMatchingTex(eq2, eq3))
            self.wait(2)
            self.play(Write(axes.x_axis), Write(axes.y_axis), Write(exp_graph))
            self.play(Write(line_graph))

        with self.voiceover(text = (
            "It shouldn't be too surprising that the line is a tangent, since by taking the limit earlier, we brought"
            " x2 infinitely close to x1 in some sense. The question now is, how could we further improve this"
            " approximation?"
        )):
            pass

        self.play(FadeOut(first_order), FadeOut(eq3), FadeOut(const), FadeOut(line_graph))

        return [axes, axes.x_axis, axes.y_axis, exp_graph, exp_label]
