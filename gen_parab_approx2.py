import copy

from manim import *

from manim_voiceover import VoiceoverScene

from svc import svc


class GenParabApprox2(VoiceoverScene):
    def construct(self):
        self.set_speech_service(svc)

        label1 = MathTex(r"(x_1, f(x_1))")
        label2 = MathTex(r"(x_2, f(x_1 + h))")
        label3 = MathTex(r"(x_3, f(x_1 - h))")
        label1.align_on_border(UP + LEFT)
        label2.next_to(label1, RIGHT)
        label3.next_to(label2, RIGHT)

        parab = (
            MathTex(r"\hat{f}(x) {{=}} {{a_0}}({{x}} - x_1)^2 {{+}} {{a_1}}({{x}} - x_1) + {{a_2}}")
                .set_color_by_tex(r"a_", RED)
        )
        parab.next_to(label1, DOWN)
        parab.align_on_border(LEFT)

        self.add(label1, label2, label3, parab)

        parab_xs = (
            MathTex(r"\hat{f}({{ {x} }}) {{=}} {{a_0}}({{ {x} }} - x_1)^2 {{+}} {{a_1}}({{ {x} }} - x_1) + {{a_2}}")
                .set_color_by_tex(r"a_", RED)
                .set_color_by_tex(r"{x}", BLUE)
        )
        parab_xs.next_to(label1, DOWN)
        parab_xs.align_on_border(LEFT)

        eq_subc_a2 = (
            MathTex(r"f({{ {x_1} }}) {{=}} {{a_0}}({{ {x_1} }} - x_1)^2 {{+}} {{a_1}}({{ {x_1} }} - x_1) + {{a_2}}")
                .set_color_by_tex(r"a", RED)
                .set_color_by_tex(r"{x_1}", BLUE)
        )
        eq_subc_a2.next_to(parab, DOWN)
        eq_subc_a2.align_on_border(LEFT)

        eq_x1phs = (
            MathTex(r"f({{ {x_1} }}) {{=}} {{a_0}}({{x_1 - x_1}})^2 {{+}} {{a_1}}({{x_1 - x_1}}) + {{a_2}}")
                .set_color_by_tex(r"x_1 - x_1", GREEN)
                .set_color_by_tex(r"a", RED)
                .set_color_by_tex(r"{x_1}", BLUE)
        )
        eq_x1phs.next_to(parab, DOWN)
        eq_x1phs.align_on_border(LEFT)

        eq_0s = (
            MathTex(r"f({{ {x_1} }}) {{=}} {{a_0}}({{ {0} }})^2 {{+}} {{a_1}}({{ {0} }}) + {{a_2}}")
                .set_color_by_tex(r"{0}", GREEN)
                .set_color_by_tex(r"a", RED)
                .set_color_by_tex(r"{x_1}", BLUE)
        )
        eq_0s.next_to(parab, DOWN)
        eq_0s.align_on_border(LEFT)

        eq_a21 = (
            MathTex(r"f({{ {x_1} }}) {{=}} {{a_2}}")
                .set_color_by_tex(r"{x_1}", BLUE)
                .set_color_by_tex(r"a", RED)
        )
        eq_a21.next_to(parab, DOWN)
        eq_a21.align_on_border(LEFT)

        eq_a2 = (
            MathTex(r"{{a_2}} {{=}} f({{ {x_1} }})")
                .set_color_by_tex(r"{x_1}", BLUE)
                .set_color_by_tex(r"a", RED)
        )
        eq_a2.next_to(parab, DOWN)
        eq_a2.align_on_border(LEFT)

        text = Tex(
            r"\begin{flushleft}"
            r"Note that it is fine to replace $\hat{f}$ with $f$ here, since by definition\\"
            r"our approximation equals the function at $x_1$, $x_1 + h$, and $x_1 - h$"
            r"\end{flushleft}",
            color = GRAY, font_size = 24
        )
        text.next_to(eq_a2, RIGHT)

        with self.voiceover(text = (
            "Now plugging in x1 into the equation will give us the value of a2"
        )):
            self.play(TransformMatchingTex(parab, parab_xs))
            self.play(TransformMatchingTex(copy.deepcopy(parab_xs), eq_subc_a2))
            self.play(FadeOut(eq_subc_a2), FadeIn(eq_x1phs))
            self.play(TransformMatchingTex(eq_x1phs, eq_0s))
            self.play(TransformMatchingTex(eq_0s, eq_a21))
            self.play(TransformMatchingTex(eq_a21, eq_a2), FadeIn(text))

        eq_subc = (
            MathTex(r"f({{x_1 + h}}) {{=}} {{a_0}}({{x_1 + h}} - x_1)^2 {{+}} {{a_1}}({{x_1 + h}} - x_1) + {{a_2}}")
                .set_color_by_tex(r"a", RED)
                .set_color_by_tex(r"x_1 + h", BLUE)
        )
        eq_subc.next_to(eq_a2, DOWN)
        eq_subc.align_on_border(LEFT)

        eq_x1phs = (
            MathTex(r"f({{ {x_1 + h} }}{)} {{=}} {{a_0}}{{(}}{{x_1 + h - x_1}}){{^2}} {{+}} {{a_1}}{{(}}{{x_1 + h - x_1}}) {{+}} {{a_2}}")
                .set_color_by_tex(r"x_1 + h - x_1", GREEN)
                .set_color_by_tex(r"{x_1 + h}", BLUE)
                .set_color_by_tex(r"a", RED)
        )
        eq_x1phs.next_to(eq_a2, DOWN)
        eq_x1phs.align_on_border(LEFT)

        eq_simpl = (
            MathTex(r"f({{ {x_1 + h} }}{)} {{=}} {{a_0}}({{ {h} }}){{^2}} {{+}} {{a_1}}({{ {h} }}) {{+}} {{a_2}}")
                .set_color_by_tex(r"{h}", BLUE)
                .set_color_by_tex(r"a", RED)
                .set_color_by_tex(r"{x_1 + h}", BLUE)
        )
        eq_simpl.next_to(eq_a2, DOWN)
        eq_simpl.align_on_border(LEFT)

        eq1 = (
            MathTex(r"f({{ {x_1 + h} }}{)} {{=}} {{a_0}}{{ {h} }}{{^2}} {{+}} {{a_1}}{{ {h} }} {{+}} {{a_2}}")
                .set_color_by_tex(r"{h}", BLUE)
                .set_color_by_tex(r"a", RED)
                .set_color_by_tex(r"{x_1 + h}", BLUE)
        )
        eq1.next_to(eq_a2, DOWN)
        eq1.align_on_border(LEFT)

        eq2 = (
            MathTex(r"f({{ {x_1 - h} }}{)} {{=}} {{a_0}}{{ {h} }}{{^2}} {{-}} {{a_1}}{{ {h} }} {{+}} {{a_2}}")
                .set_color_by_tex(r"{h}", BLUE)
                .set_color_by_tex(r"a", RED)
                .set_color_by_tex(r"{x_1 - h}", BLUE)
        )
        eq2.next_to(eq1, DOWN)
        eq2.align_on_border(LEFT)

        with self.voiceover(text = (
            "Now, we have to do a little more work for getting the value of a0 and a1. <bookmark mark='A'/> Plugging in"
            " x1 + h gives us this equation, and in a similar manner, plugging in x1 - h gives us <bookmark mark='B'/>"
            " this second equation"
        )):
            self.wait_until_bookmark("A")
            self.play(TransformMatchingTex(copy.deepcopy(parab_xs), eq_subc), FadeOut(text))
            self.play(FadeOut(eq_subc), FadeIn(eq_x1phs))
            self.play(TransformMatchingTex(eq_x1phs, eq_simpl))
            self.play(TransformMatchingTex(eq_simpl, eq1))
            self.wait_until_bookmark("B")
            self.play(Write(eq2))

        eq_a0 = (
            MathTex(r"{{a_0}} {{=}} { f({{x_1 + h}}) + f({{x_1 - h}}) - 2 f({{x_1}}) \over 2{{ {h} }}^2 }")
                .set_color_by_tex(r"x_1", BLUE)
                .set_color_by_tex(r"{h}", BLUE)
                .set_color_by_tex(r"a", RED)
        )
        eq_a0.next_to(eq2, DOWN)
        eq_a0.align_on_border(LEFT)

        eq_a1 = (
            MathTex(r"{{a_1}} {{=}} { f({{x_1 + h}}) - f({{x_1 - h}}) \over 2{{ {h} }} }")
                .set_color_by_tex(r"x_1", BLUE)
                .set_color_by_tex(r"{h}", BLUE)
                .set_color_by_tex(r"a", RED)
        )
        eq_a1.next_to(eq_a0, DOWN)
        eq_a1.align_on_border(LEFT)

        parab_up = (
            MathTex(r"\hat{f}({{ {x} }}) {{=}} {{a_0}}({{ {x} }} - x_1)^2 {{+}} {{a_1}}({{ {x} }} - x_1) + {{a_2}}")
                .set_color_by_tex(r"a_", RED)
                .set_color_by_tex(r"{x}", BLUE)
        )
        parab_up.align_on_border(LEFT + UP)

        eq_a0_up = (
            MathTex(r"{{a_0}} {{=}} { f({{x_1 + h}}) + f({{x_1 - h}}) - 2 f({{x_1}}) \over 2{{ {h} }}^2 }")
                .set_color_by_tex(r"x_1", BLUE)
                .set_color_by_tex(r"{h}", BLUE)
                .set_color_by_tex(r"a", RED)
        )
        eq_a0_up.next_to(parab_up, DOWN)
        eq_a0_up.align_on_border(LEFT)

        eq_a1_up = (
            MathTex(r"{{a_1}} {{=}} { f({{x_1 + h}}) - f({{x_1 - h}}) \over 2{{ {h} }} }")
                .set_color_by_tex(r"x_1", BLUE)
                .set_color_by_tex(r"{h}", BLUE)
                .set_color_by_tex(r"a", RED)
        )
        eq_a1_up.next_to(eq_a0_up, DOWN)
        eq_a1_up.align_on_border(LEFT)

        eq_a2_up = (
            MathTex(r"{{a_2}} {{=}} f({{ {x_1} }})")
                .set_color_by_tex(r"{x_1}", BLUE)
                .set_color_by_tex(r"a", RED)
        )
        eq_a2_up.next_to(eq_a1_up, DOWN)
        eq_a2_up.align_on_border(LEFT)

        with self.voiceover(text = (
            "You can solve these for a0 and a1 by adding and subtracting the equations respectively, and you get the"
            " <bookmark mark='A'/> following values:"
        )):
            self.wait_until_bookmark("A")
            self.play(Write(eq_a0), Write(eq_a1))
            self.wait(2)
            self.play(FadeOut(eq1, eq2, label1, label2, label3))
            self.play(
                TransformMatchingTex(eq_a0, eq_a0_up),
                TransformMatchingTex(eq_a1, eq_a1_up),
                TransformMatchingTex(eq_a2, eq_a2_up),
                TransformMatchingTex(parab_xs, parab_up),
            )

        return [parab_up, eq_a0_up, eq_a1_up, eq_a2_up]