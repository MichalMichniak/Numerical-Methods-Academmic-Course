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
results_polly_A = expected['polly_A']
results_roots_20 = expected['roots_20']
results_frob_a = expected['frob_a']

@pytest.mark.parametrize("x, result", results_polly_A)
def test_polly_A(x: np.ndarray, result):
    if result is None:
        assert main.polly_A(x) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.polly_A(x))
    else:
        tresult = main.polly_A(x)
        assert tresult[0] == pytest.approx(result[0]) and tresult[1] == pytest.approx(result[1]),  'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.polly_A(x))


@pytest.mark.parametrize("a, result", results_roots_20)
def test_roots_20(a: np.ndarray, result):
    if result is None:
        assert main.roots_20(a) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result,
                                                                                                      main.roots_20(a))
    else:
        tresult = main.roots_20(a)
        assert tresult[0] == pytest.approx(result[0]) and tresult[1] == pytest.approx(
            result[1]), 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.roots_20(a))


@pytest.mark.parametrize("wsp, result", results_frob_a)
def test_frob_a(wsp: np.ndarray, result):
    if result is None:
        assert main.frob_a(wsp) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result,
                                                                                                      main.frob_a(wsp))
    else:
        tresult = main.frob_a(wsp)
        assert tresult[0] == pytest.approx(result[0]) and tresult[1] == pytest.approx(
            result[1]), 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.frob_a(wsp))


        