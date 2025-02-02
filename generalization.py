import copy

from manim import *

from manim_voiceover import VoiceoverScene

from svc import svc


class Generalization(VoiceoverScene):
    def construct(self):
        self.set_speech_service(svc)

        first_order = (
            MathTex(r"\hat{f}(x) {{=}} {{ { f } (}}{{x_1}}{{ {)} }} {{+}} {{ { f }'(}}{{x_1}}{{ {)} }} (x - {{x_1}})")
                .set_color_by_tex(r"x_1", RED)
                .set_color_by_tex(r"{ f }", BLUE)
                .set_color_by_tex(r"{)}", BLUE)
                .align_on_border(LEFT + UP)
        )

        second_order = (
            MathTex(r"\hat{f}({{ {x} }}) {{=}} {{ { f } (}}{{x_1}}{{ {)} }} {{+}} {{ { f }'(}}{{x_1}} {{ {)} }} {{(}}{{ {x} }} - {{x_1}}) {{+}} { { { f }''({{x_1}}{{ {)} }} \over 2 } {{(}}{{ {x} }} - {{x_1}}){{^2}} }")
                .set_color_by_tex(r"x_1", RED)
                .set_color_by_tex(r"{ f }", BLUE)
                .set_color_by_tex(r"{)}", BLUE)
                .set_color_by_tex(r"\over 2", BLUE)
                .next_to(first_order, DOWN)
                .align_on_border(LEFT)
        )

        with self.voiceover(text = (
            "Let's go back to the abstract for a bit, and see what we have so far."
        )):
            self.play(Write(first_order), Write(second_order))

        linear = (
            MathTex(r"y = {{a_0}} + {{a_1}} (x - {{x_1}})")
                .set_color_by_tex(r"x_1", RED)
                .set_color_by_tex(r"a", BLUE)
                .next_to(second_order, DOWN)
                .align_on_border(LEFT)
        )

        quad = (
            MathTex(r"y = {{a_0}} + {{a_1}} (x - {{x_1}}) + {{a_2}} (x - {{x_1}})^2")
            .set_color_by_tex(r"x_1", RED)
            .set_color_by_tex(r"a", BLUE)
            .next_to(linear, DOWN)
            .align_on_border(LEFT)
        )

        deg_n = (
            MathTex(r"y {{=}} \sum\limits_{k = 0 }^{ {{n}} } {{a_k}}({{x}} - {{x_1}}){{^k}}")
                .set_color_by_tex(r"x_1", RED)
                .set_color_by_tex(r"a_k", BLUE)
                .next_to(quad, DOWN)
                .align_on_border(LEFT)
        )

        inf = (
            MathTex(r"y {{=}} \sum\limits_{k = 0 }^{ {{\infty}} } {{a_k}}({{x}} - {{x_1}}){{^k}}")
                .set_color_by_tex(r"x_1", RED)
                .set_color_by_tex(r"a_k", BLUE)
                .next_to(quad, DOWN)
                .align_on_border(LEFT)
        )

        with self.voiceover(text = (
            "To get both of these approximations, we started with the general forms of the curves of"
            " <bookmark mark='A'/> degree one and two. In general, the curve of degree n <bookmark mark='B'/> looks"
            " like this. So following our idea of approximating by sampling an infinite number of points, if we just"
            " turn that <bookmark mark='C'/> n into infinity, maybe we have a start!"
        )):
            self.wait_until_bookmark("A")
            self.play(Write(linear), Write(quad))
            self.wait_until_bookmark("B")
            self.play(Write(deg_n))
            self.wait_until_bookmark("C")
            self.play(ReplacementTransform(deg_n, inf))

        derive_n = (
            MathTex(r"{ d^n y \over dx^n } {{=}} \sum\limits_{k = n }^{ {{\infty}} } k!\ {{a_k}}({{x}} - {{x_1}}){{^{(k-n)} }}")
                .set_color_by_tex(r"x_1", RED)
                .set_color_by_tex(r"a_k", BLUE)
                .next_to(inf, DOWN)
                .align_on_border(LEFT)
        )

        derive_n2 = (
            MathTex(r"{ d^n y \over dx^n } {{=}} {{n!}}\ {{a_n}} {{+}} \sum\limits_{k = n + 1 }^{ {{\infty}} } k!\ {{a_k}}({{x}} - {{x_1}}){{^{(k-n)} }}")
                .set_color_by_tex(r"x_1", RED)
                .set_color_by_tex(r"a_", BLUE)
                # .set_color_by_tex(r"n!", BLUE)
                .next_to(inf, DOWN)
                .align_on_border(LEFT)
        )

        derive_n3 = (
            MathTex(r"{{\left(}} { d^n y \over dx^n } {{\right)}}_{{ {x_1} }} {{=}} {{n!}}\ {{a_n}} {{+}} \sum\limits_{k = n + 1 }^{ {{\infty}} } k!\ {{a_k}}({{x_1}} - {{x_1}}){{^{(k-n)} }}")
                .set_color_by_tex(r"x_1", RED)
                .set_color_by_tex(r"a_", BLUE)
                # .set_color_by_tex(r"n!", BLUE)
                .next_to(inf, DOWN)
                .align_on_border(LEFT)
        )

        derive_n4 = (
            MathTex(r"f^{(n)}({{x_1}}{{ {)} }} {{=}} {{n!}}\ {{a_n}} {{+}} \sum\limits_{k = n + 1 }^{ {{\infty}} } k!\ {{a_k}}({{0}}){{^{(k-n)} }}")
                .set_color_by_tex(r"0", RED)
                .set_color_by_tex(r"x_1", RED)
                .set_color_by_tex(r"a_", BLUE)
                .set_color_by_tex(r"f", BLUE)
                # .set_color_by_tex(r"n!", BLUE)
                .set_color_by_tex(r"{)}", BLUE)
                .next_to(inf, DOWN)
                .align_on_border(LEFT)
        )

        eq_an = (
            MathTex(r"f^{(n)}({{x_1}}{{ {)} }} {{=}} {{n!}}\ {{a_n}}")
                .set_color_by_tex(r"x_1", RED)
                .set_color_by_tex(r"a_", BLUE)
                .set_color_by_tex(r"f", BLUE)
                # .set_color_by_tex(r"n!", BLUE)
                .set_color_by_tex(r"{)}", BLUE)
                .next_to(inf, DOWN)
                .align_on_border(LEFT)
        )

        eq_an2 = (
            MathTex(r"{{a_n}} {{=}} { f^{(n)}( {{x_1}} ) \over n! }")
            .set_color_by_tex(r"x_1", RED)
            .set_color_by_tex(r"a_", BLUE)
            .set_color_by_tex(r"f", BLUE)
            .set_color_by_tex(r")", BLUE)
            .next_to(inf, DOWN)
            .align_on_border(LEFT)
        )

        with self.voiceover(text = (
            "Okay, but how do we solve for an infinite number of coefficients? It feels like the coefficients should"
            " somehow involve higher order derivatives, following the pattern for <bookmark mark='A'/> two and three"
            " points. And this is the final insight! Notice that if we differentiate <bookmark mark='B'/> the"
            " polynomial n times, it eliminates the first n terms, and we can <bookmark mark='C'/> pull the first term"
            " out of the summation, and it doesn't involve x at all! So if we plug in <bookmark mark='D'/> x1 for x,"
            " every single remaining term goes to zero, and we get an expression for a_n!"
        )):
            self.wait_until_bookmark("A")
            self.play(
                *[Indicate(first_order[i]) for i in [3, 4, 5, 9, 10, 11]],
                *[Indicate(second_order[i]) for i in [5, 6, 7, 11, 12, 14, 22, 23, 24, 25]]
            )
            self.wait_until_bookmark("B")
            self.play(TransformMatchingTex(copy.deepcopy(inf), derive_n))
            self.wait_until_bookmark("C")
            self.play(TransformMatchingTex(derive_n, derive_n2))
            self.wait_until_bookmark("D")
            self.play(TransformMatchingTex(derive_n2, derive_n3))
            self.play(TransformMatchingTex(derive_n3, derive_n4))
            self.play(TransformMatchingTex(derive_n4, eq_an))
            self.play(TransformMatchingTex(eq_an, eq_an2))

        taylor = (
            MathTex(r"f(x) = \sum\limits_{k = 0}^{\infty} { {{ f^{(k)}( }} {{x_1}} {{ {)} }} (x - {{x_1}})^k \over {{k!}}}", font_size = 72)
                .set_color_by_tex(r"x_1", RED)
                .set_color_by_tex(r"k!", BLUE)
                .set_color_by_tex(r"f^", BLUE)
                .set_color_by_tex(r"{)}", BLUE)
        )


        with self.voiceover(text = (
            "And just like that, we've re-discovered the Taylor Series!"
        )):
            self.play(FadeOut(inf, linear, quad, first_order, second_order, eq_an2))
            self.play(Write(taylor))
            self.wait(8)
