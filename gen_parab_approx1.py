from manim import *

from manim_voiceover import VoiceoverScene

from svc import svc



class GenParabApprox1(VoiceoverScene):
    def construct(self):
        self.set_speech_service(svc)

        label1 = MathTex(r"(x_1, y_1)")
        label2 = MathTex(r"(x_2, y_2)")
        label3 = MathTex(r"(x_3, y_3)")

        label1.align_on_border(UP + LEFT)
        label2.next_to(label1, RIGHT)
        label3.next_to(label2, RIGHT)

        parab = MathTex(r"\hat{f}(x) {{=}} a_0{{x}}^2 + a_1{{x}} + a_2")
        parab.next_to(label1, DOWN)
        parab.align_on_border(LEFT)

        self.add(label1, label2, label3, parab)

        label1_ys = MathTex(r"(x_1, {{y_1}})").set_color_by_tex(r"y", BLUE)
        label2_ys = MathTex(r"(x_2, {{y_2}})").set_color_by_tex(r"y", BLUE)
        label3_ys = MathTex(r"(x_3, {{y_3}})").set_color_by_tex(r"y", BLUE)

        label1_ys.align_on_border(UP + LEFT)
        label2_ys.next_to(label1_ys, RIGHT)
        label3_ys.next_to(label2_ys, RIGHT)

        fn = MathTex(r"y = f(x)", color = BLUE)
        fn.next_to(parab, DOWN)
        fn.align_on_border(LEFT)

        fn_white = MathTex(r"y = f(x)").move_to(fn)

        label1_fs = MathTex(r"(x_1, {{f(x_1)}})").set_color_by_tex(r"f", BLUE)
        label2_fs = MathTex(r"(x_2, {{f(x_2)}})").set_color_by_tex(r"f", BLUE)
        label3_fs = MathTex(r"(x_3, {{f(x_3)}})").set_color_by_tex(r"f", BLUE)

        label1_fs.align_on_border(UP + LEFT)
        label2_fs.next_to(label1_fs, RIGHT)
        label3_fs.next_to(label2_fs, RIGHT)

        label1_fs_white = MathTex(r"(x_1, f(x_1))").move_to(label1_fs)
        label2_fs_white = MathTex(r"(x_2, f(x_2))").move_to(label2_fs)
        label3_fs_white = MathTex(r"(x_3, f(x_3))").move_to(label3_fs)

        with self.voiceover(text = (
            "We'll follow a similar line of algebraic manipulation as before, rewriting all the <bookmark mark='A'/>"
            " ys in terms of f of x."
        )):
            self.wait_until_bookmark("A")
            self.play(
                Write(fn),
                TransformMatchingTex(label1, label1_ys),
                TransformMatchingTex(label2, label2_ys),
                TransformMatchingTex(label3, label3_ys),
            )
            self.wait(2)
            self.play(
                TransformMatchingTex(fn, fn_white),
                TransformMatchingTex(label1_ys, label1_fs),
                TransformMatchingTex(label2_ys, label2_fs),
                TransformMatchingTex(label3_ys, label3_fs),
            )

        label1_xns = MathTex(r"(x_1, f({{ {x_1} }}))").set_color_by_tex("{x_1}", BLUE).move_to(label1_fs)
        label2_xns = MathTex(r"(x_2, f({{ {x_2} }}))").set_color_by_tex("{x_2}", BLUE).move_to(label2_fs)
        label3_xns = MathTex(r"(x_3, f({{ {x_3} }}))").set_color_by_tex("{x_3}", BLUE).move_to(label3_fs)

        x2_as_x1 = MathTex(r"x_2 = x_1 + h", color = BLUE)
        x3_as_x1 = MathTex(r"x_3 = x_1 - h", color = BLUE)

        text = Tex(
            r"\begin{flushleft}"
            r"Note that you could've chosen $x_1 + h$ and $x_1 + 2h$, and\\"
            r"that'd would work too, this is just simpler for manipulation!"
            r"\end{flushleft}",
            font_size = 24,
            color = GRAY
        )

        x2_as_x1.next_to(fn, DOWN)
        x2_as_x1.align_on_border(LEFT)

        x3_as_x1.next_to(x2_as_x1, DOWN)
        x3_as_x1.align_on_border(LEFT)

        text.next_to(x2_as_x1, RIGHT)

        x2_as_x1_white = MathTex(r"x_2 = x_1 + h").move_to(x2_as_x1)
        x3_as_x1_white = MathTex(r"x_3 = x_1 - h").move_to(x3_as_x1)

        label1_x1s = MathTex(r"(x_1, f({{ {x_1} }}))").set_color_by_tex("{x_1}", BLUE)
        label2_x1s = MathTex(r"(x_2, f({{ {x_1 + h} }}))").set_color_by_tex("{x_1 + h}", BLUE)
        label3_x1s = MathTex(r"(x_3, f({{ {x_1 - h} }}))").set_color_by_tex("{x_1 - h}", BLUE)
        label1_x1s.align_on_border(UP + LEFT)
        label2_x1s.next_to(label1_x1s, RIGHT)
        label3_x1s.next_to(label2_x1s, RIGHT)

        label1_x1s_white = MathTex(r"(x_1, f(x_1))").move_to(label1_x1s)
        label2_x1s_white = MathTex(r"(x_2, f(x_1 + h))").move_to(label2_x1s)
        label3_x1s_white = MathTex(r"(x_3, f(x_1 - h))").move_to(label3_x1s)

        with self.voiceover(text = (
            "Next, we'll rewrite x2 and x3 in terms of x1"
        )):
            self.wait(1)
            self.play(
                TransformMatchingTex(label1_fs, label1_fs_white),
                TransformMatchingTex(label2_fs, label2_fs_white),
                TransformMatchingTex(label3_fs, label3_fs_white),
            )
            self.play(
                Write(x2_as_x1), Write(x3_as_x1), FadeIn(text),
                TransformMatchingTex(label1_fs_white, label1_xns),
                TransformMatchingTex(label2_fs_white, label2_xns),
                TransformMatchingTex(label3_fs_white, label3_xns),
            )
            self.wait(2)
            self.play(
                TransformMatchingTex(label1_xns, label1_x1s),
                TransformMatchingTex(label2_xns, label2_x1s),
                TransformMatchingTex(label3_xns, label3_x1s),
            )
            self.play(FadeOut(text))
            self.wait(1)
            self.play(
                TransformMatchingTex(x2_as_x1, x2_as_x1_white),
                TransformMatchingTex(x3_as_x1, x3_as_x1_white),
                TransformMatchingTex(label1_x1s, label1_x1s_white),
                TransformMatchingTex(label2_x1s, label2_x1s_white),
                TransformMatchingTex(label3_x1s, label3_x1s_white),
            )

        subc = MathTex(r"x \leftarrow x - x_1", color = BLUE)
        subc.next_to(x3_as_x1, DOWN)
        subc.align_on_border(LEFT)

        parab_xs = MathTex(r"\hat{f}(x) {{=}} a_0{{ {x} }}^2 + a_1{{ {x} }} + a_2").set_color_by_tex(r"{x}", BLUE)
        parab_xs.next_to(label1, DOWN)
        parab_xs.align_on_border(LEFT)

        parab_subc = MathTex(r"\hat{f}(x) {{=}} a_0{{(x - x_1)}}^2 + a_1{{(x - x_1)}} + a_2").set_color_by_tex(r"x - x_1", BLUE)
        parab_subc.next_to(label1, DOWN)
        parab_subc.align_on_border(LEFT)

        parab_subc_white = MathTex(r"\hat{f}(x) {{=}} a_0{{(x - x_1)}}^2 + a_1{{(x - x_1)}} + a_2").move_to(parab_subc)
        parab_subc_white.next_to(label1, DOWN)
        parab_subc_white.align_on_border(LEFT)

        with self.voiceover(text = (
            "I'll also substitute x - x1 for x in the equation of the parabola. This only affects the values of a0, a1,"
            " and a2, as our choice of x1 is arbitrary anyway, so there is no loss of generality, but this form will"
            " make solving for the coefficients much easier!"
        )):
            self.play(
                Write(subc),
                TransformMatchingTex(parab, parab_xs),
            )
            self.wait(2)
            self.play(
                TransformMatchingTex(parab_xs, parab_subc),
            )

        self.play(
            FadeOut(subc, fn_white, x2_as_x1_white, x3_as_x1_white),
            TransformMatchingTex(parab_subc, parab_subc_white),
        )

        return [parab_subc_white, label1_x1s_white, label2_x1s_white, label3_x1s_white]
