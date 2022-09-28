import numpy as np
import scipy
import pickle
import typing
import math
import types
import pickle
from inspect import isfunction


from typing import Union, List, Tuple


def fun(x):
    return np.exp(-2*x)+x**2-1


def dfun(x):
    return -2*np.exp(-2*x) + 2*x


def ddfun(x):
    return 4*np.exp(-2*x) + 2


def bisection(a: Union[int, float], b: Union[int, float], f: typing.Callable[[float], float], epsilon: float, iteration: int) -> Tuple[float, int]:
    '''funkcja aproksymująca rozwiązanie równania f(x) = 0 na przedziale [a,b] metodą bisekcji.

    Parametry:
    a - początek przedziału
    b - koniec przedziału
    f - funkcja dla której jest poszukiwane rozwiązanie
    epsilon - tolerancja zera maszynowego (warunek stopu)
    iteration - ilość iteracji

    Return:
    float: aproksymowane rozwiązanie
    int: ilość iteracji
    '''
    try:
        if f(a) * f(b) >= 0:
            raise ValueError
        if type(iteration) != int or epsilon < 0 or b < a:
            raise ValueError
        for i in range(iteration):
            if f(a)*f((a+b)/2) < 0:
                b = (a+b)/2
            elif f(a) == 0:
                return a, i-2
            else:
                a = (b+a)/2
            if abs(f(b)-f(a)) < epsilon:
                return a, i-2
        return a, iteration
    except:
        return None


def secant(a: Union[int, float], b: Union[int, float], f: typing.Callable[[float], float], epsilon: float, iteration: int) -> Tuple[float, int]:
    '''funkcja aproksymująca rozwiązanie równania f(x) = 0 na przedziale [a,b] metodą siecznych.

    Parametry:
    a - początek przedziału
    b - koniec przedziału
    f - funkcja dla której jest poszukiwane rozwiązanie
    epsilon - tolerancja zera maszynowego (warunek stopu)
    iteration - ilość iteracji

    Return:
    float: aproksymowane rozwiązanie
    int: ilość iteracji
    '''
    try:
        if f(a) * f(b) >= 0:
            raise ValueError
        if type(iteration) != int or epsilon < 0 or b < a:
            raise ValueError
        for i in range(iteration):
            x = (b*f(a)-a*f(b))/(f(a)-f(b))

            if f(x)*f(b) > 0:
                b = x
            if f(x)*f(a) > 0:
                a = x
            if abs(f(a)) < epsilon:
                return b - f(b)*(b-a)/(f(b)-f(a)), i
        return b - f(b)*(b-a)/(f(b)-f(a)), iteration
    except:
        return None


def newton(f: typing.Callable[[float], float], df: typing.Callable[[float], float], ddf: typing.Callable[[float], float], a: Union[int, float], b: Union[int, float], epsilon: float, iteration: int) -> Tuple[float, int]:
    ''' Funkcja aproksymująca rozwiązanie równania f(x) = 0 metodą Newtona.
    Parametry: 
    f - funkcja dla której jest poszukiwane rozwiązanie
    df - pochodna funkcji dla której jest poszukiwane rozwiązanie
    ddf - druga pochodna funkcji dla której jest poszukiwane rozwiązanie
    a - początek przedziału
    b - koniec przedziału
    epsilon - tolerancja zera maszynowego (warunek stopu)
    Return:
    float: aproksymowane rozwiązanie
    int: ilość iteracji
    '''
    try:
        if f(a) * f(b) >= 0:
            raise ValueError
        if type(iteration) != int or epsilon < 0 or b < a or df(a)*df(b) <= 0 or ddf(a)*ddf(b) <= 0 :
            raise ValueError
        for i in range(iteration):
            a = a - f(a)/df(a)
            if abs(f(a)) < epsilon:
                return a, i-1
        return a, iteration
    except:
        return None
