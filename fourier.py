from manim import *

# Config file with specific Fourier series functions
from func.triangle import *
# from func.square import *

# compile command
#    manim -pqm fourier.py Fourier
# command line args
#    https://docs.manim.community/en/stable/tutorials/configuration.html

# *** References
#
# Manim Community
#    https://docs.manim.community/en/stable/tutorials/quickstart.html
# Learn Manim - Full Course for Beginners [Tutorial]
#    https://www.youtube.com/watch?v=KHGoFDB-raE
# The Beauty of Fourier Series
#    https://www.youtube.com/watch?v=u-JFPNJ2eCc
# Animation with Manim, Plot 2D
#    https://github.com/Elteoremadebeethoven/AnimationsWithManim/blob/master/English/6a_plots_2D/scenes.md
# HeatEq
#    https://github.com/rpw199912j/matsci_animation/blob/abd757dfa1102ef70086e845b759f468843ca97a/kinetics/heat_equation.py#L115


# How to define periodic functions?
#    https://stackoverflow.com/a/32669296/5570400
def periodic(offset, period):
    return lambda f: lambda x: f(((x - offset) % period) + offset)


func_period = func_period_to - func_period_from


@periodic(func_period_from, func_period)
def func_periodic(x):
    return func(x)


def func_series(n):
    @periodic(func_period_from, func_period)
    def func_series_periodic(x):
        return series(x, n)
    return func_series_periodic


class Fourier(Scene):
    def construct(self):
        self.create_axes()

        # define the original function
        graph_func = self.axes.plot(
            func_periodic,
            x_range=(func_x_range_min, func_x_range_max, plot_x_delta),
            discontinuities=func_discontinuities,
            use_smoothing=True,
            color=COLOR_FUNC
        )

        # message displayed before the formula
        txt_message = Text(message, font_size=40)
        txt_message.set_color(COLOR_MESSAGE)

        math_func = MathTex(tex_func, font_size=40)
        math_func.set_color(COLOR_FUNC)

        math_tilde = MathTex(tex_sim_or_equals, font_size=60)
        math_tilde.set_color(COLOR_TILDE)

        math_series = MathTex(tex_series, font_size=40)
        math_series.set_color(COLOR_SERIES)

        top_labels = VGroup(txt_message, math_tilde, math_series).arrange(RIGHT, buff=1)
        top_labels.to_edge(UP, buff=1)
        math_func.move_to(txt_message)

        txt_periodic = Text("periodic", font_size=22, color=COLOR_PERIODIC).next_to(math_func, DOWN, buff=0.2)

        # Animation Tutorial
        #     https://azarzadavila-manim.readthedocs.io/en/latest/animation.html
        # Animation Transform Src
        #     https://github.com/ManimCommunity/manim/blob/main/manim/animation/transform.py
        self.play(Write(txt_message), DrawBorderThenFill(self.axes))
        self.play(ReplacementTransform(txt_message, math_func), Write(txt_periodic), Create(graph_func))
        self.play(Write(math_series))
        self.play(Write(math_tilde))

        self.prepare_fourier_animation()
        self.animate_fourier_series(series_start, series_end, series_step)
        self.animate_fourier_series(series_more_start, series_more_end, series_more_step)

        self.wait()

    def prepare_fourier_animation(self):
        self.math_n_equals = MathTex(r"n = ", font_size=60, color=COLOR_N_TERM_COUNT)
        self.math_n_equals.align_to(self.axes, UR).shift(LEFT)
        self.play(FadeIn(self.math_n_equals))

        self.graph_series = None
        self.n_series = None

    def animate_fourier_series(self, start, end, step):
        each_run_time = series_run_time / (end - start)

        fade_animation_on = each_run_time >= 0.4

        # transform the graph while increasing the number of terms
        for n in range(start, end + 1, step):
            # MEMO : I could use Variable class too.
            # Variable class = ValueTracker with label
            #     https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Variable.html

            n_series_new = Integer(n).scale(1.1).next_to(self.math_n_equals, RIGHT, buff=0.2).shift(UP * 0.03)
            n_series_new.set_color(COLOR_N_TERM_COUNT)

            # ParametricFunction
            #     https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.ParametricFunction.html
            graph_series_new = self.axes.plot(
                func_series(n),
                x_range=[func_x_range_min, func_x_range_max, plot_x_delta],
                use_smoothing=True, color=COLOR_SERIES, stroke_width=3, stroke_opacity=0.9)
            if self.graph_series is not None:
                self.play(
                    ReplacementTransform(self.graph_series, graph_series_new, run_time=each_run_time),
                    FadeTransform(self.n_series, n_series_new, run_time=each_run_time if fade_animation_on else 0))
            else:
                self.play(Create(graph_series_new), Write(n_series_new))

            self.graph_series = graph_series_new
            self.n_series = n_series_new

    def create_axes(self):
        self.axes = (Axes(
            x_range=(x_min, x_max, x_step),
            y_range=(y_min, y_max, y_step), y_length=y_length,
            # axis_config keys available
            #   https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine
            axis_config={
                "include_ticks": include_ticks,
                "include_tip": include_tip
            }
        )).to_corner(DOWN, buff=1.8)

        labels = self.axes.get_axis_labels(x_label="x", y_label="").set_color(WHITE)
        self.axes.add(labels)

        if(is_pi_label):
            self.add_pi_x_labels()

    def add_pi_x_labels(self, scale=0.8, buff=0.4, buff_adjust=0.09, aligned_edge=DOWN):
        x_min = self.axes.x_range[0]
        x_max = self.axes.x_range[1]

        if x_min <= 0 and 0 <= x_max:
            self.axes.add(
                MathTex(r"0").next_to(
                    self.axes.c2p(0, 0),
                    aligned_edge, buff=buff
                ).scale(scale)
            )
        if x_min <= -PI and -PI <= x_max:
            self.axes.add(
                MathTex(r"-\pi").next_to(
                    self.axes.c2p(-PI, 0),
                    aligned_edge,
                    buff=buff + buff_adjust
                ).scale(scale)
            )
        if x_min <= PI and PI <= x_max:
            self.axes.add(
                MathTex(r"\pi").next_to(
                    self.axes.c2p(PI, 0),
                    aligned_edge,
                    buff=buff + buff_adjust
                ).scale(scale)
            )

        for n in range(-10, 10):
            if n in (-1, 0, 1):
                continue
            npi = n * PI
            if x_min <= npi and npi <= x_max:
                self.axes.add(
                    MathTex(str(n) + r"\pi").next_to(
                        self.axes.c2p(npi, 0),
                        aligned_edge,
                        buff=buff
                    ).scale(scale)
                )
