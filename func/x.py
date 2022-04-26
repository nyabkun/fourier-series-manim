from manim import *
import numpy as np

# Original Function
func_period_from, func_period_to = 0, 2*PI
func_discontinuities = np.arange(-PI * 6, PI * 6, 2*PI)


def func(x):
    return (x/PI) - 1


# Fourier series for the func above
def series(x, num_terms):
    sum_terms = 0

    # reverse order
    # adding up from small numbers
    for n in range(num_terms, 0, -1):
        sum_terms += (1 / n) * np.sin(n * x)

    return -(2/PI) * sum_terms


# Tex
# Web Tool : Hand writing math expression to Tex
#   https://webdemo.myscript.com/views/math/index.html#
tex_func = r"""
f(x) = \frac{x}{\pi} - 1 \hspace{2.1em} (0 \leq x < 2 \pi )
"""
tex_sim_or_equals = r"\sim"
tex_series = r"""
-\dfrac{2}{\pi}
\sum_{n=1}^{\infty}
    \dfrac{\sin nx}{n}
"""

# Number of terms
series_start, series_end, series_step = 1, 19, 1
series_run_time = 15

series_more_start, series_more_end, series_more_step = 20, 200, 10
series_more_run_time = 10

# Axes
x_min, x_max, x_step = -4.4 * PI, 4.4 * PI, PI
y_min, y_max, y_step = -1.4, 1.4, 1
y_length = 3
include_ticks = False
include_tip = False
is_pi_label = True
show_x_0_label = False

# Function plot
func_x_range_min, func_x_range_max = -4.3 * PI, 4.3 * PI
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
