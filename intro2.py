from manim import *

from manim_voiceover import VoiceoverScene

from svc import svc


class Intro2(VoiceoverScene):

    @staticmethod
    def scale_obj(rect: Rectangle, content: Mobject):
        # Scale the content to fit inside the box
        content_width, content_height = content.width, content.height
        scale_factor = min((rect.width - 0.1) / content_width, (rect.height - 0.1) / content_height)
        content.scale(scale_factor).move_to(rect.get_center())

    def construct(self):
        self.set_speech_service(svc)

        title = Text("The Three Step Journey", font_size = 32)
        title.align_on_border(UP)

        axes1 = Axes(
            x_range = [-PI-0.5, PI+0.5],
            y_range = [-1.5, 1.5],
            tips = False
        )
        sin_graph1 = axes1.plot(lambda x: np.sin(x), color = GREEN)
        line_approx = axes1.plot(lambda x: 2/PI * x, x_range = [-PI/2-0.5, PI/2+0.5], color = BLUE)
        graph1 = VGroup(axes1, sin_graph1, line_approx)

        axes2 = Axes(
            x_range = [-PI-0.5, PI+0.5],
            y_range = [-1.5, 1.5],
            tips = False
        )
        sin_graph2 = axes1.plot(lambda x: np.sin(x), color = GREEN)
        parab_approx = axes1.plot(lambda x: -4/PI**2 * x*x + 4/PI * x, x_range = [-0.75, PI+0.5], color = BLUE)
        graph2 = VGroup(axes2, sin_graph2, parab_approx)

        poly_approx = MathTex(r"f(x) = \sum\limits_{k = 0}^{\infty} a_k x^k")

        size_m = 2.5

        step1 = Rectangle(width = 1.6 * size_m, height = 0.9 * size_m)
        step2 = Rectangle(width = 1.6 * size_m, height = 0.9 * size_m)
        step3 = Rectangle(width = 1.6 * size_m, height = 0.9 * size_m)

        VGroup(step1, step2, step3).arrange(RIGHT)

        Intro2.scale_obj(step1, graph1)
        Intro2.scale_obj(step2, graph2)
        Intro2.scale_obj(step3, poly_approx)

        subtitle1 = Text("Initial Approximation", font_size = 24)
        subtitle2 = Text("Trying to Improve", font_size = 24)
        subtitle3 = Text("Generalizing", font_size = 24)

        subtitle1.next_to(step1, UP)
        subtitle2.next_to(step2, UP)
        subtitle3.next_to(step3, UP)

        with (self.voiceover(text = (
            "My goal with this video is to take you on a three step journey, to hopefully show you that following a"
            " mathematical line of reasoning, you too could've discovered Taylor series for yourselves!"
        ))):
            self.play(FadeIn(title))

            self.play(FadeIn(subtitle1), Write(step1))
            self.play(Write(axes1.x_axis), Write(axes1.y_axis), Write(sin_graph1))
            self.play(Write(line_approx))

            self.play(FadeIn(subtitle2), Write(step2))
            self.play(Write(axes2.x_axis), Write(axes2.y_axis), Write(sin_graph2))
            self.play(Write(parab_approx))

            self.play(FadeIn(subtitle3), Write(step3))
            self.play(Write(poly_approx))
