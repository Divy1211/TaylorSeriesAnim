import copy

from manim import *

from manim_voiceover import VoiceoverScene

from svc import svc


class SecondOrderApprox(VoiceoverScene):
    def construct(self):
        self.set_speech_service(svc)

        parab = (
            MathTex(r"\hat{f}({{ {x} }}) {{=}} {{a_0}}({{ {x} }} - {{x_1}}){{^2}} {{+}} {{a_1}}({{ {x} }} - {{x_1}}) {{+}} {{a_2}}")
                .set_color_by_tex(r"a_", RED)
                .set_color_by_tex(r"{x}", BLUE)
        )
        parab.align_on_border(LEFT + UP)

        eq_a0 = (
            MathTex(r"{{a_0}} {{=}} { f({{x_1}} + {{ {h} }}) + f({{x_1}} - {{ {h} }}) - 2 f({{x_1}}) \over 2{{ {h} }}{{^2}} }")
                .set_color_by_tex(r"x_1", BLUE)
                .set_color_by_tex(r"{h}", BLUE)
                .set_color_by_tex(r"a", RED)
        )
        eq_a0[5].set_color(BLUE)
        eq_a0[9].set_color(BLUE)
        eq_a0.next_to(parab, DOWN)
        eq_a0.align_on_border(LEFT)

        eq_a1 = (
            MathTex(r"{{a_1}} {{=}} { f({{x_1}} + {{ {h} }}) - f({{x_1}} - {{ {h} }}) \over 2{{ {h} }} }")
                .set_color_by_tex(r"x_1", BLUE)
                .set_color_by_tex(r"{h}", BLUE)
                .set_color_by_tex(r"a", RED)
        )
        eq_a1[5].set_color(BLUE)
        eq_a1[9].set_color(BLUE)
        eq_a1.next_to(eq_a0, DOWN)
        eq_a1.align_on_border(LEFT)

        eq_a2 = (
            MathTex(r"{{a_2}} {{=}} f({{ {x_1} }})")
                .set_color_by_tex(r"{x_1}", BLUE)
                .set_color_by_tex(r"a", RED)
        )
        eq_a2.next_to(eq_a1, DOWN)
        eq_a2.align_on_border(LEFT)

        self.add(parab, eq_a0, eq_a1, eq_a2)

        eq_a0_lim = (
            MathTex(r"{{ { \lim\limits_{h \to 0} } }} {{a_0}} {{=}} {{ \lim\limits_{h \to 0} }} {{\left[}} { f({{x_1}} + {{ {h} }}) + f({{x_1}} - {{ {h} }}) - 2 f({{x_1}}) \over 2{{ {h} }}{{^2}} } {{\right]}}")
                .set_color_by_tex(r"x_1", BLUE)
                .set_color_by_tex(r"{h}", GREEN)
                .set_color_by_tex(r"a", RED)
                .set_color_by_tex(r"\lim", GREEN)
                .set_color_by_tex(r"\left[", GREEN)
                .set_color_by_tex(r"\right]", GREEN)
        )
        eq_a0_lim.next_to(parab, DOWN)
        eq_a0_lim.align_on_border(LEFT)

        eq_a1_lim = (
            MathTex(r"{{ { \lim\limits_{h \to 0} } }} {{a_1}} {{=}} {{ \lim\limits_{h \to 0} }} {{\left[}} { f({{x_1}} + {{ {h} }}) - f({{x_1}} - {{ {h} }}) \over 2{{ {h} }} } {{\right]}}")
                .set_color_by_tex(r"x_1", BLUE)
                .set_color_by_tex(r"{h}", GREEN)
                .set_color_by_tex(r"a", RED)
                .set_color_by_tex(r"\lim", GREEN)
                .set_color_by_tex(r"\left[", GREEN)
                .set_color_by_tex(r"\right]", GREEN)
        )
        eq_a1_lim.next_to(eq_a0_lim, DOWN)
        eq_a1_lim.align_on_border(LEFT)

        eq_a2_lim = (
            MathTex(r"{{a_2}} {{=}} f({{ {x_1} }})")
                .set_color_by_tex(r"{x_1}", BLUE)
                .set_color_by_tex(r"a", RED)
        )
        eq_a2_lim.next_to(eq_a1_lim, DOWN)
        eq_a2_lim.align_on_border(LEFT)

        eq_a0_simpl = (
            MathTex(r"{{a_0}} {{=}} {{ \lim\limits_{h \to 0} }} {{\left[}} { f({{x_1}} + {{ {h} }}) + f({{x_1}} - {{ {h} }}) - 2 f({{x_1}}) \over 2{{ {h} }}{{^2}} } {{\right]}}")
                .set_color_by_tex(r"x_1", BLUE)
                .set_color_by_tex(r"{h}", GREEN)
                .set_color_by_tex(r"a", RED)
                .set_color_by_tex(r"\lim", GREEN)
                .set_color_by_tex(r"\left[", GREEN)
                .set_color_by_tex(r"\right]", GREEN)
        )
        eq_a0_simpl.next_to(parab, DOWN)
        eq_a0_simpl.align_on_border(LEFT)

        eq_a1_simpl = (
            MathTex(r"{{a_1}} {{=}} {{ \lim\limits_{h \to 0} }} {{\left[}} { f({{x_1}} + {{ {h} }}) - f({{x_1}} - {{ {h} }}) \over 2{{ {h} }} } {{\right]}}")
                .set_color_by_tex(r"x_1", BLUE)
                .set_color_by_tex(r"{h}", GREEN)
                .set_color_by_tex(r"a", RED)
                .set_color_by_tex(r"\lim", GREEN)
                .set_color_by_tex(r"\left[", GREEN)
                .set_color_by_tex(r"\right]", GREEN)
        )
        eq_a1_simpl.next_to(eq_a0_simpl, DOWN)
        eq_a1_simpl.align_on_border(LEFT)

        second_der = MathTex(r"g''(x) = \lim\limits_{h \to 0} { g(x + h) - 2g(x) + g(x - h) \over h^2 }", color = GRAY, font_size = 24)
        second_der.next_to(eq_a0, RIGHT)

        first_der = Text(
            "You may want to look up the forward difference, the central\n"
            "difference, and the backward difference definitions of the derivative!",
            color = GRAY, font_size = 12
        )
        first_der.next_to(eq_a1, RIGHT)

        second_order1 = (
            MathTex(r"\hat{f}({{ {x} }}) {{=}} { f''({{x_1}}) \over 2 } {{(}}{{ {x} }} - {{x_1}}){{^2}} {{+}} f'({{x_1}}) {{(}}{{ {x} }} - {{x_1}}) {{+}} f({{x_1}})")
                .set_color_by_tex(r"{x}", BLUE)
                .set_color_by_tex(r"x_1", RED)
        )
        second_order1.align_on_border(LEFT + UP)

        second_order2 = (
            MathTex(r"\hat{f}({{ {x} }}) {{=}} f({{x_1}}) {{+}} f'({{x_1}}) {{(}}{{ {x} }} - {{x_1}}) {{+}} { { f''({{x_1}}) \over 2 } {{(}}{{ {x} }} - {{x_1}}){{^2}} }")
                .set_color_by_tex(r"{x}", BLUE)
                .set_color_by_tex(r"x_1", RED)
        )
        second_order2.align_on_border(LEFT + UP)

        second_order = copy.deepcopy(second_order2)
        second_order.scale(0.75)
        second_order.align_on_border(LEFT + UP)

        eq_a0_fin = (
            MathTex(
                r"{{a_0}} {{=}} { f''({{x_1}}) \over 2 }"
            )
            .set_color_by_tex(r"x_1", BLUE)
            .set_color_by_tex(r"a", RED)
        )
        eq_a0_fin.next_to(second_order2, DOWN)
        eq_a0_fin.align_on_border(LEFT)

        eq_a1_fin = (
            MathTex(
                r"{{a_1}} {{=}} f'({{x_1}})"
            )
            .set_color_by_tex(r"x_1", BLUE)
            .set_color_by_tex(r"a", RED)
        )
        eq_a1_fin.next_to(eq_a0_fin, DOWN)
        eq_a1_fin.align_on_border(LEFT)

        eq_a2_fin = (
            MathTex(r"{{a_2}} {{=}} f({{ {x_1} }})")
            .set_color_by_tex(r"{x_1}", BLUE)
            .set_color_by_tex(r"a", RED)
        )
        eq_a2_fin.next_to(eq_a1_fin, DOWN)
        eq_a2_fin.align_on_border(LEFT)

        with self.voiceover(text = (
            "Notice that once again, the expression for a0 looks suspiciously similar to that of the"
            " <bookmark mark='A'/> second derivative with an extra <bookmark mark='B'/> 2 in the denominator. Also, the"
            " expression for a1 is once again suspiciously similar to that of the <bookmark mark='C'/> first derivative."
            " <bookmark mark='D'/> Taking the limits again, and making the substitutions for a0, a1, and a2 we arrive at"
            " the final approximation!"
        )):
            self.wait_until_bookmark("A")
            self.play(FadeIn(second_der))
            self.wait_until_bookmark("B")
            self.play(Flash(eq_a0[13][2]), Indicate(eq_a0[13][2]))
            self.wait_until_bookmark("C")
            self.play(FadeIn(first_der))
            self.wait_until_bookmark("D")
            self.play(FadeOut(second_der, first_der))
            self.play(
                TransformMatchingTex(eq_a0, eq_a0_lim),
                TransformMatchingTex(eq_a1, eq_a1_lim),
                TransformMatchingTex(eq_a2, eq_a2_lim),
            )
            self.play(
                TransformMatchingTex(eq_a0_lim, eq_a0_simpl),
                TransformMatchingTex(eq_a1_lim, eq_a1_simpl),
            )
            self.play(
                TransformMatchingTex(eq_a0_simpl, eq_a0_fin),
                TransformMatchingTex(eq_a1_simpl, eq_a1_fin),
                TransformMatchingTex(eq_a2_lim, eq_a2_fin),
            )
            self.play(TransformMatchingTex(parab, second_order1))
            self.play(TransformMatchingTex(second_order1, second_order2))
            self.play(
                FadeOut(eq_a0_fin, eq_a1_fin, eq_a2_fin),
                TransformMatchingTex(second_order2, second_order),
            )

        const = MathTex(r"x_1 = 0", color = YELLOW)
        const.scale(0.75)
        const.next_to(second_order, DOWN)
        const.align_on_border(LEFT)

        eq1 = (
            MathTex(r"\hat{f}({{ {x} }}) {{=}} f({{0}}) {{+}} f'({{0}}) ({{ {x} }} - {{0}}) {{+}} { f''({{0}}) \over 2 } ({{ {x} }} - {{0}})^2")
                .set_color_by_tex(r"{x}", BLUE)
                .set_color_by_tex(r"0", RED)
        )
        eq1.scale(0.75)
        eq1.next_to(const, DOWN)
        eq1.align_on_border(LEFT)

        eq2 = (
            MathTex(r"\hat{f}({{ {x} }}) {{=}} e^{{0}} {{+}} e^{{0}} ({{ {x} }}) {{+}} { e^{{0}} \over 2 } ({{ {x} }})^2")
                .set_color_by_tex(r"{x}", BLUE)
                .set_color_by_tex(r"0", RED)
        )
        eq2.scale(0.75)
        eq2.next_to(const, DOWN)
        eq2.align_on_border(LEFT)

        eq3 = (
            MathTex(r"\hat{f}({{ {x} }}) {{=}} 1 {{+}} {{ {x} }} {{+}} { {{ {x} }}^2 \over 2 }")
            .set_color_by_tex(r"{x}", BLUE)
            .set_color_by_tex(r"0", RED)
        )
        eq3.scale(0.75)
        eq3.next_to(const, DOWN)
        eq3.align_on_border(LEFT)

        axes = Axes(
            x_range = [-4, 4],
            y_range = [-0.5, 7.5],
            tips = False
        )
        exp_graph = axes.plot(lambda x: np.exp(x), color = GREEN)
        exp_label = axes.get_graph_label(exp_graph, label = r"f(x) = e^x", x_val = 2.5, color = GREEN)
        exp_graph.add(exp_label)

        parab_graph = axes.plot(lambda x: 1 + x + x**2/2, color = BLUE)
        parab_label = axes.get_graph_label(parab_graph, label = r"\hat{f}(x) = 1 + x + { x^2 \over 2 }", x_val = 0, direction = RIGHT, color = BLUE)
        parab_label.move_to(parab_label.get_center() + RIGHT * 0.1)
        parab_graph.add(parab_label)

        with self.voiceover(text = (
            "Let's now plug in zero for x1 <bookmark mark='A'/>, and see what the graph looks like!"
        )):
            self.wait_until_bookmark("A")
            self.play(Write(const))
            self.play(Write(eq1))
            self.play(TransformMatchingTex(eq1, eq2))
            self.play(TransformMatchingTex(eq2, eq3))
            self.wait(2)
            self.play(Write(axes.x_axis), Write(axes.y_axis), Write(exp_graph))
            self.play(Write(parab_graph))

        with self.voiceover(text = (
            "Once again, the parabola is tangential to the original curve, since by taking the limits earlier, we"
            " brought x2 and x3 infinitely close to x1."
        )):
            pass

        self.wait(1)
        ls = []
        ls2 = []
        ls3 = []
        for i, x in enumerate(range(-3, 5), 1):
            point = Dot(axes.coords_to_point(x, np.exp(x)))
            ls.append(point)
            point = Dot(axes.coords_to_point(x - 0.5, np.exp(x - 0.5)))
            ls2.append(point)
            point1 = Dot(axes.coords_to_point(x - 0.25, np.exp(x - 0.25)))
            point2 = Dot(axes.coords_to_point(x - 0.75, np.exp(x - 0.75)))
            ls3.append(point1)
            ls3.append(point2)

        with self.voiceover(text = (
            "What happens if we keep increasing the number of sample points <bookmark mark='A'/> further and"
            " <bookmark mark='B'/> further? That means the approximation is exactly equal to our function at more"
            " points! Hang on, what if we sampled an *infinite* number of points? Would that make the functions somehow"
            " exactly equal?"
        )):
            self.play(FadeOut(const, eq3, parab_graph, second_order))
            self.play(*map(FadeIn, ls))
            self.wait_until_bookmark("A")
            self.play(*[ReplacementTransform(copy.deepcopy(p1), p2) for (p1, p2) in zip(ls, ls2)])
            self.wait_until_bookmark("B")
            anims = []
            for (p1, p2, p3, p4) in zip(ls, ls2, ls3[::2], ls3[1::2]):
                anims.extend([
                    ReplacementTransform(copy.deepcopy(p1), p3),
                    ReplacementTransform(copy.deepcopy(p2), p4)
                ])
            self.play(*anims)

        with self.voiceover(text = (
            "Okay, but there's a few problems with that idea, we can't exactly visualize an infinite degree curve on a"
            " graph, and how do we even solve for an infinite number of coefficients?"
        )):
            pass
