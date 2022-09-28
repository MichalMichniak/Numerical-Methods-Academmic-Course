# -*- coding: utf-8 -*-

import pytest
import main
import pickle
import math
import numpy as np
import pickle
from typing import Callable


from typing import Union, List, Tuple

expected = pickle.load(open('expected','rb'))
results_bisection = expected['bisection']
results_secant = expected['secant']
results_newton= expected['newton']

@pytest.mark.parametrize("a, b, epsilon, iteration, result", results_bisection)
def test_bisection(a: float, b: float, epsilon: float, iteration: int, result):
    if result is None:
        assert main.bisection(a, b, main.fun, epsilon, iteration) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.bisection(a, b, main.fun, epsilon, iteration))
    else:
        tresult = main.bisection(a, b, main.fun, epsilon, iteration)
        assert tresult[0] == pytest.approx(result[0]) and tresult[1] == pytest.approx(result[1]),  'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.bisection(a, b, main.fun, epsilon, iteration))
        
        
@pytest.mark.parametrize("a, b, epsilon, iteration, result", results_secant)
def test_secant(a: float, b: float, epsilon: float, iteration: int, result):
    if result is None:
        assert main.secant(a, b, main.fun, epsilon, iteration) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.secant(a, b, main.fun, epsilon, iteration))
    else:
        tresult = main.secant(a, b, main.fun, epsilon, iteration)
        assert tresult[0] == pytest.approx(result[0]) and tresult[1] == pytest.approx(result[1]),  'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.secant(a, b, main.fun, epsilon, iteration))
        
        
        
@pytest.mark.parametrize("a, b, epsilon, iteration, result", results_newton)
def test_newton(a: float, b: float, epsilon: float, iteration: int, result):
    if result is None:
        assert main.newton(main.fun, main.dfun, main.ddfun, a, b, epsilon, iteration) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.newton(main.fun, main.dfun, main.ddfun, a, b, epsilon, iteration))
    else:
        tresult = main.newton(main.fun, main.dfun, main.ddfun, a, b, epsilon, iteration)
        assert tresult[0] == pytest.approx(result[0]) and tresult[1] == pytest.approx(result[1]),  'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.newton(main.fun, main.dfun, main.ddfun, a, b, epsilon, iteration))