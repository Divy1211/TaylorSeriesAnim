from manim import *

from manim_voiceover import VoiceoverScene

from svc import svc


class Preface(VoiceoverScene):
    def construct(self):
        self.set_speech_service(svc)

        title = Text("How This Video Differs From Similar Ones", font_size = 32)
        title.align_on_border(UP)
        with self.voiceover(text = (
            "You might be wondering, similar videos on this topic exist, what value does this video add?"
        )):
            self.play(Write(title))

        poly_approx = MathTex(r"f(x) = \sum\limits_{k = 0}^{\infty} {{a_k}} (x - x_1)^k", font_size = 48)
        poly_approx.next_to(title, DOWN)
        poly_approx.align_on_border(LEFT)

        qmark1 = Text("???", font_size = 32)
        qmark1.next_to(poly_approx, RIGHT)

        nth_term = MathTex(r"{{a_k}} = \cfrac{f^{(k)}(x_1) }{k!}", font_size = 48)
        poly_approx.set_color_by_tex('a_k', BLUE)
        nth_term.set_color_by_tex('a_k', BLUE)

        nth_term.next_to(poly_approx, DOWN)
        nth_term.align_on_border(LEFT)

        qmark2 = Text("???", font_size = 32)
        qmark2.move_to((qmark1.get_center()[0], nth_term.get_center()[1], 0.0))

        axes = Axes(
            x_range = [-PI-0.5, PI+0.5],
            y_range = [-1.5, 1.5],
            tips = False
        )
        sin_graph = axes.plot(lambda x: np.cos(x), color = GREEN)
        line_approx = axes.plot(lambda x: 1, color = BLUE)
        parab_approx = axes.plot(lambda x: 1 - x**2/2, color = BLUE)
        quartic_approx = axes.plot(lambda x: 1 - x**2/2 + x**4/24, color = BLUE)
        graph = VGroup(axes, sin_graph, line_approx, parab_approx, quartic_approx)
        graph.scale(0.75)
        graph.align_on_border(RIGHT)

        with self.voiceover(text = (
            "Most \"intuitive\" lines of reasoning jump straight into how a function can be <bookmark mark='A'/>"
            " approximated by an infinite polynomial and why we use <bookmark mark='B'/> the derivatives to find the coefficients"
            " - saying that it makes the <bookmark mark='C'/> polynomial match the <bookmark mark='D'/> slope,"
            " <bookmark mark='E'/> concavity, <bookmark mark='F'/> et cetera. with the original function. It has always"
            " left me with the question of how we arrived at using an <bookmark mark='G'/> infinite polynomial approximation and"
            " using <bookmark mark='H'/> repeated differentiation to find coefficients. And while these are brilliant ideas in"
            " themselves, they feel like two big leaps in reasoning to me. In this video, I hope to show you how you could've"
            " come up with <bookmark mark='I'/> these ideas yourself!"
        )):
            self.wait_until_bookmark("A")
            self.play(Write(poly_approx))
            self.wait_until_bookmark("B")
            self.play(Write(nth_term))
            self.wait_until_bookmark("C")
            self.play(Write(axes.x_axis), Write(axes.y_axis), Write(sin_graph))
            self.wait_until_bookmark("D")
            self.play(Write(line_approx))
            self.wait_until_bookmark("E")
            self.play(Transform(line_approx, parab_approx))
            self.wait_until_bookmark("F")
            self.play(Transform(line_approx, quartic_approx))
            self.wait_until_bookmark("G")
            self.play(Write(qmark1))
            self.wait_until_bookmark("H")
            self.play(Write(qmark2))
            self.wait_until_bookmark("I")
            self.play(Indicate(poly_approx), Indicate(nth_term))
