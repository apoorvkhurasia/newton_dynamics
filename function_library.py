"""
This file contains all the functions and derivatives
we have analysed as examples in this project.
"""
import numpy as np


def quad_newton_map(z, **kwargs):
    r"""
    This is the newton map for `f(z) = z^2 + alpha z + beta`
    :param \**kwargs:
        See below
    :Keyword arguments:
        * *alpha* (``float``)
        * *beta* (``float``)
    """
    alpha = kwargs.get('alpha')
    beta = kwargs.get('beta')
    return z - (z**2 + alpha*z + beta)/(2*z + alpha)


def quad_map_discontinuity(**kwargs):
    r"""
    Returns all discontinuities of `quad_newton_map`
    :param \**kwargs:
        See below
    :Keyword arguments:
        * *alpha* (``float``)
        * *beta* (``float``)
    :return:
        An array of all discontinuities of `quad_newton_map`
    """
    alpha = kwargs.get('alpha')
    return [-alpha/2]


def quad_map_deriv(z, **kwargs):
    r"""
    The derivative of the `quad_newton_map`
    :param \**kwargs:
        See below
    :Keyword arguments:
        * *alpha* (``float``)
        * *beta* (``float``)
    """
    alpha = kwargs.get('alpha')
    beta = kwargs.get('beta')
    return 2 * (z**2 + alpha*z + beta)/(2*z + alpha)**2


def cubic_newton_map(z, **kwargs):
    alpha = kwargs.get('alpha')
    return 2*z**3/(3*z**2 - alpha)


def cubic_map_discontinuity(**kwargs):
    alpha = kwargs.get('alpha')
    return [-np.sqrt(alpha/3), np.sqrt(alpha/3)]


def cubic_map_deriv(z, **kwargs):
    alpha = kwargs.get('alpha')
    return (6*z**4 - 6*alpha*z**2)/(3*z**2 - alpha)**2


def general_polynomial_map(z, **kwargs):
    alpha = kwargs.get('alpha')
    return (alpha/(alpha+1)) * (z + 1/z - ((alpha-1)/alpha))


def general_polynomial_map_discontinuity(**kwargs):
    return [0]


def general_polynomial_map_deriv(z, **kwargs):
    alpha = kwargs.get('alpha')
    return (alpha/(alpha+1)) * (1 - 1/(z**2))


def exp_map(z, **kwargs):
    return np.exp(z) * (z - 1)


def exp_map_discontinuity(**kwargs):
    return []


def exp_map_deriv(z, **kwargs):
    return np.exp(z) * z
