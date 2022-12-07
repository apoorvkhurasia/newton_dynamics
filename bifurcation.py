import numpy as np


def draw_bifurcation(map_func,
                     map_deriv_func,
                     steps,
                     burn_in,
                     bifurcation_ax,
                     lyapunov_ax,
                     z0_vals,
                     variable_arg_name,
                     variable_arg_tex_name,
                     **map_args):
    r"""
    Draws the bifurcation and Lyapunov exponent
    diagrams as shown in the project presentation.

    :param map_func: The map function
    :param map_deriv_func: The derivative of the map function.
    :param steps: The total number of steps to take.
    :param burn_in: The number of first steps to discard.
    :param bifurcation_ax: The figure axis on which the bifurcation
                           diagram is to be plotted.
    :param lyapunov_ax: The figure axis on which the Lyapunov exponent
                        is to be plotted.
    :param z0_vals: The initial guesses for root.
    :param variable_arg_name: The name of the variable argument (must be
                              one of the keyword arguments to the map
                              function and its derivative). ```str```
    :param variable_arg_tex_name: The TeX syntax to display the variable
                                  argument (x-axis of this plot).
    :param \**map_args: The keyword args to ```map_func``` and 
                        ```map_deriv_func```.
    """
    variable_arg = map_args[variable_arg_name]
    z = z0_vals
    lyapunov_exp = np.zeros(len(z))

    np.seterr(divide='ignore')  # To avoid warnings for log(0) = -Inf
    for i in range(steps):
        z = map_func(z, **map_args)
        if i >= burn_in:
            lyapunov_exp += np.log(abs(map_deriv_func(z, **map_args)))
            bifurcation_ax.plot(variable_arg, z, ',g', alpha=.01)

    np.seterr(divide='warn')  # Switch warnings back on
    lyapunov_exp = lyapunov_exp / (steps - burn_in)

    bifurcation_ax.set_ylabel("$z$", fontsize=16, labelpad=10, rotation=0)
    bifurcation_ax.set_title("Bifurcation diagram", fontsize=20)

    lyapunov_ax.axhline(0, color='k', lw=.5, alpha=.5)
    lyapunov_ax.plot(variable_arg[lyapunov_exp <= 0],
                     lyapunov_exp[lyapunov_exp <= 0],
                     '.k', alpha=.5, ms=.5)
    lyapunov_ax.plot(variable_arg[lyapunov_exp > 0],
                     lyapunov_exp[lyapunov_exp > 0],
                     '.r', alpha=.5, ms=.5)
    lyapunov_ax.set_title("Lyapunov exponent", fontsize=18)
    lyapunov_ax.set_xlabel(variable_arg_tex_name, fontsize=16)
    lyapunov_ax.set_ylabel("$\\lambda$", fontsize=16, labelpad=10, rotation=0)


def draw_bifurcation_cmplx(map_func,
                           steps,
                           burn_in,
                           real_ax,
                           img_ax,
                           z0_vals,
                           variable_arg_name,
                           variable_arg_tex_name,
                           **map_args):
    r"""
    Draws the bifurcation diagrams for complex values 
    as shown in the project presentation.

    :param map_func: The map function
    :param steps: The total number of steps to take.
    :param burn_in: The number of first steps to discard.
    :param real_ax: The figure axis on which the bifurcation
                    diagram for the real part of reached states is
                    to be plotted.
    :param img_ax: The figure axis on which the bifurcation
                   diagram for the imaginary part of reached states is
                   to be plotted.
    :param z0_vals: The initial guesses for root.
    :param variable_arg_name: The name of the variable argument (must be
                              one of the keyword arguments to the map
                              function). ```str```
    :param variable_arg_tex_name: The TeX syntax to display the variable
                                  argument (x-axis of this plot).
    :param \**map_args: The keyword args to ```map_func```.
    """
    variable_arg = map_args[variable_arg_name]
    z = z0_vals + 1j
    for i in range(steps):
        z = map_func(z, **map_args)
        if i >= burn_in:
            real_ax.plot(variable_arg, z.real, ',g')
            img_ax.plot(variable_arg, z.imag, ',g')
            img_ax.plot(variable_arg, -z.imag, ',g')

    real_ax.set_ylabel("$\\mathrm{Re}(z)$",
                       fontsize=16, labelpad=20, rotation=0)
    img_ax.set_ylabel("$\\mathrm{Im}(z)$",
                      fontsize=16, labelpad=20, rotation=0)
    img_ax.set_xlabel(variable_arg_tex_name, fontsize=16)
