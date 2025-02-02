from manim import *

from manim_voiceover import VoiceoverScene

from svc import svc


class GenLinearApprox(VoiceoverScene):
    def construct(self):
        self.set_speech_service(svc)

        # tpf = two point form
        tpf = MathTex(r"\hat{f}(x) {{=}} y_1 {{+}} {y_2 - y_1 \over x_2 - x_1} {{(x - x_1)}}")
        tpf.align_on_border(LEFT + UP)

        self.add(tpf)

        tpf_ys = MathTex(r"\hat{f}(x) {{=}} y_1 {{+}} { {{y_2}} - {{y_1}} \over x_2 - x_1} {{(x - x_1)}}")
        tpf_ys.set_color_by_tex(r"y", BLUE)
        tpf_ys.align_on_border(LEFT + UP)

        fn = MathTex(r"y = f(x)", color = BLUE)
        fn.next_to(tpf, DOWN)
        fn.align_on_border(LEFT)

        fn_white = MathTex(r"y = f(x)")
        fn_white.next_to(tpf, DOWN)
        fn_white.align_on_border(LEFT)

        tpf_fs = MathTex(r"\hat{f}(x) {{=}} f(x_1) {{+}} { {{f(x_2)}} - {{f(x_1)}} \over x_2 - x_1} {{(x - x_1)}}")
        tpf_fs.set_color_by_tex(r"f(", BLUE)
        tpf_fs.align_on_border(LEFT + UP)

        text = Text("Is it starting to look familiar?\nThink Newton!", font_size = 24, color = GRAY)
        text.next_to(tpf_fs, RIGHT)

        tpf2 = MathTex(r"\hat{f}(x) {{=}} f(x_1) {{+}} {f(x_2) - f(x_1) \over x_2 - x_1} {{(x - x_1)}}")
        tpf2.align_on_border(LEFT + UP)

        x2_as_x1 = MathTex(r"x_2 = x_1 + h", color = BLUE)
        x2_as_x1.align_on_border(LEFT)
        x2_as_x1.next_to(fn, DOWN)

        x2_as_x1_white = MathTex(r"x_2 = x_1 + h")
        x2_as_x1_white.align_on_border(LEFT)
        x2_as_x1_white.next_to(fn, DOWN)

        tpf_x2s = MathTex(r"\hat{f}(x) {{=}} f(x_1) {{+}} {f({{x_2}}) - f(x_1) \over {{x_2}} - x_1}(x - x_1)")
        tpf_x2s.set_color_by_tex(r"x_2", BLUE)
        tpf_x2s.align_on_border(LEFT + UP)

        tpf_x1s = MathTex(r"\hat{f}(x) {{=}} f(x_1) {{+}} {f({{x_1 + h}}) - f(x_1) \over {{x_1 + h}} - x_1}(x - x_1)")
        tpf_x1s.set_color_by_tex(r"x_1 + h", BLUE)
        tpf_x1s.align_on_border(LEFT + UP)

        tpf_x1s_white = MathTex(r"\hat{f}(x) = f(x_1) + {f(x_1 + h) - f(x_1) \over x_1 + h - x_1}(x - x_1)")
        tpf_x1s_white.align_on_border(LEFT + UP)

        tpf_h = MathTex(r"\hat{f}(x) = f(x_1) + {f(x_1 + h) - f(x_1) \over {{x_1 + h - x_1}} }(x - x_1)")
        tpf_h.set_color_by_tex(r"x_1 + h - x_1", BLUE)
        tpf_h.align_on_border(LEFT + UP)

        tpf_h2 = MathTex(r"\hat{f}(x) = f(x_1) + {f(x_1 + h) - f(x_1) \over {{ {h} }} }(x - x_1)")
        tpf_h2.set_color_by_tex(r"{h}", BLUE)
        tpf_h2.align_on_border(LEFT + UP)

        tpf_simplified = MathTex(r"\hat{f}(x) = f(x_1) + {f(x_1 + h) - f(x_1) \over h}(x - x_1)")
        tpf_simplified.align_on_border(LEFT + UP)

        with self.voiceover(text = (
            "Let's start by substituting f of x for y <bookmark mark='A'/> in the two point form. Now, it'd be nice if"
            " we had some way to reason about how good <bookmark mark='B'/> our approximation is"
            " depending on our choice of x1 and x2. <bookmark mark='C'/> But thinking about changing two values at the"
            " same time is kind of complicated, it'd be nice if we could somehow get rid of x2. What if we rewrote it"
            " in terms of x1? Let's say <bookmark mark='D'/> x2 = x1 + h where h is some distance. We are still thinking"
            " in terms of two values, it's just x1 and h now."
        )):
            self.play(Write(fn), TransformMatchingTex(tpf, tpf_ys))
            self.wait_until_bookmark("A")
            self.play(TransformMatchingTex(tpf_ys, tpf_fs))
            self.wait_until_bookmark("B")
            self.play(Indicate(tpf_fs))
            self.play(FadeIn(text))
            self.wait_until_bookmark("C")
            self.play(FadeOut(text))
            self.play(TransformMatchingTex(fn, fn_white), TransformMatchingTex(tpf_fs, tpf2))
            self.wait_until_bookmark("D")
            self.play(Write(x2_as_x1), TransformMatchingTex(tpf2, tpf_x2s))
            self.wait(1)
            self.play(TransformMatchingTex(tpf_x2s, tpf_x1s))
            self.wait(1)
            self.play(TransformMatchingTex(x2_as_x1, x2_as_x1_white), TransformMatchingTex(tpf_x1s, tpf_x1s_white))
            self.play(TransformMatchingTex(tpf_x1s_white, tpf_h))
            self.wait(1)
            self.play(TransformMatchingTex(tpf_h, tpf_h2))
            self.wait(1)
            self.play(TransformMatchingTex(tpf_h2, tpf_simplified))
            self.wait(1)
            self.play(FadeOut(fn_white), FadeOut(x2_as_x1_white))

        return [tpf_simplified]
