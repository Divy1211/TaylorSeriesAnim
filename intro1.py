from manim import *

from manim_voiceover import VoiceoverScene

from svc import svc


class Intro1(VoiceoverScene):
    def construct(self):
        self.set_speech_service(svc)

        taylor_formula = MathTex(r"f(x) = \sum\limits_{k = 0}^{\infty} \cfrac{f^{(k)}(x_1) (x - x_1)^k}{k!}", font_size = 72)
        with self.voiceover(text = "This is the formula for approximating a function with a taylor series"):
            self.play(Write(taylor_formula))

        text = Text("???", font_size = 32)
        text.next_to(taylor_formula, DOWN)
        with self.voiceover(text = "But where does it come from?"):
            self.play(Write(text))
