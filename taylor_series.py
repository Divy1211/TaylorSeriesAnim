from manim import *

from manim_voiceover import VoiceoverScene

from src.taylor_series.first_order_approx import FirstOrderApprox
from src.taylor_series.gen_linear_approx import GenLinearApprox
from src.taylor_series.gen_parab_approx1 import GenParabApprox1
from src.taylor_series.gen_parab_approx2 import GenParabApprox2
from src.taylor_series.generalization import Generalization
from src.taylor_series.intro1 import Intro1
from src.taylor_series.intro2 import Intro2
from src.taylor_series.linear_approx import LinearApprox
from src.taylor_series.parab_approx import ParabApprox
from src.taylor_series.preface import Preface
from src.taylor_series.second_order_approx import SecondOrderApprox


class TaylorSeries(VoiceoverScene):
    def construct(self):
        for cls in [
            Intro1,
            Intro2,
            Preface,
            LinearApprox,
            GenLinearApprox,
            FirstOrderApprox,
            ParabApprox,
            GenParabApprox1,
            GenParabApprox2,
            SecondOrderApprox,
            Generalization,
        ]:
            exclude = cls.construct(self) or []
            ls = [FadeOut(obj) for obj in self.mobjects if obj not in exclude]
            if len(ls) > 0:
                self.play(*ls)
            if len(exclude) > 0:
                self.remove(*exclude)
