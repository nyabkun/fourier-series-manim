from manim import *
import numpy as np

# Original Function
func_period_from, func_period_to = -PI, PI
func_discontinuities = np.arange(-PI * 4, PI * 4, PI)


def func(x):
    return 0 if x >= 0 else 1


# Fourier series for the func above
def series(x, num_terms):
    sum_terms = 1 / 2

    # reverse order
    # adding up from small numbers
    for n in range(num_terms, 0, -1):
        if (n % 2) == 0:
            continue
        sum_terms += -(2 / (n * PI)) * np.sin(n * x)

    return sum_terms


# Tex
# Web Tool : Hand writing math expression to Tex
#   https://webdemo.myscript.com/views/math/index.html#
tex_func = r"""
f(x) =
\begin{cases}
    \hspace{.4em}
    1 \quad ( \, -\pi \leq x < 0 \, ) \\
    \hspace{.4em}
    0 \quad ( \, 0 \leq x < \pi \, )
\end{cases}
"""
tex_sim_or_equals = r"\sim"
tex_series = r"""
\dfrac{1}{2} +
\sum_{n=1}^{\infty}
    \dfrac{1}{n\pi}
    \Big\{ (-1) ^{n}-1 \Big\} \sin nx
"""

# Number of terms
series_start, series_end, series_step = 1, 19, 2
series_run_time = 15

series_more_start, series_more_end, series_more_step = 21, 201, 10
series_more_run_time = 10

# Axes
x_min, x_max, x_step = -3.4 * PI, 3.4 * PI, PI
y_min, y_max, y_step = -0.1, 1.5, 1
y_length = 3
include_ticks = False
include_tip = False
is_pi_label = True

# Function plot
func_x_range_min, func_x_range_max = -3.3 * PI, 3.3 * PI
plot_x_delta = 5e-3

# Color
COLOR_MESSAGE = WHITE
COLOR_FUNC = GREEN
COLOR_PERIODIC = YELLOW
COLOR_SERIES = BLUE
COLOR_TILDE = WHITE
COLOR_N_TERM_COUNT = WHITE

# Message displayed before the formula
message = "Fourier Series for"
