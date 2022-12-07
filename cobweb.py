import numpy as np
import numpy.ma as M


def draw_cobweb(map_func,
                map_discontinuity,
                steps,
                ax,
                xlim,
                ylim,
                z0,
                **map_args):
    r"""
    Draws the cobweb plot for a given 1 parameter map.

    :param map_func: The map function.
    :param map_discontinuity: The function which returns
                              an array of all discontinuities
                              of `map_func`.
    :param steps: The number of steps to take for the map.
    :param ax: The figure axis object on which to plot this cobweb.
    :param xlim: The x-axis limits (array of two ```float```s).
    :param ylim: The y-axis limits (array of two ```float```s).
    :param z0: The starting point.
    :param \**map_args: The keyword args to `map_func` and `map_discontinuity`.
    """
    t = np.linspace(start=xlim[0], stop=xlim[1], num=10000)
    y = M.array(map_func(z=t, **map_args))

    # Remove that annoying auto-connected line between discontinuities
    for d in map_discontinuity(**map_args):
        y = M.masked_where(abs(t - d) < 0.01, y)

    # This is the plot of the map
    ax.plot(t, y, '-k', linewidth=0.8)

    # This is the line y = x
    ax.plot([min(xlim[0], ylim[0]), max(xlim[1], ylim[1])],
            [min(xlim[0], ylim[0]), max(xlim[1], ylim[1])],
            'k:',)

    # Now we iteratively draw the cobweb
    z_curr = z0
    for i in range(steps):
        z_next = map_func(z=z_curr, **map_args)
        ax.plot([z_curr, z_next], [z_next, z_next],
                'b', alpha=0.6, linewidth=0.5)
        if i >= 1:
            ax.plot([z_curr, z_curr], [z_curr, z_next],
                    'b', alpha=0.6, linewidth=0.5)
            ax.plot([z_curr], [z_next], 'ob', ms=5,
                    alpha=(i + 1) / steps)  # Assign a shade
        else:
            ax.plot([z_curr], [z_next], 'or', ms=5)

        z_curr = z_next

    # Set viewport and title on the plot
    ax.set_xlim(xlim[0], xlim[1])
    ax.set_ylim(ylim[0], ylim[1])
    ax.set_xlabel("$z_n$", fontsize=16)
    ax.set_ylabel("$z_{n+1}$", fontsize=16, labelpad=20, rotation=0)
