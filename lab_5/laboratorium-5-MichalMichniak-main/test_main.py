# -*- coding: utf-8 -*-

import pytest
import main
import pickle
import math
import numpy as np

from typing import Union, List, Tuple

expected = pickle.load(open('expected','rb'))

results_first_spline = expected['first_spline']
results_cubic_spline = expected['cubic_spline']

@pytest.mark.parametrize("x, y ,result", results_first_spline)
def test_first_spline(x: np.ndarray, y: np.ndarray, result):
    if result is None:
        assert main.first_spline(x,y) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.first_spline(x,y))
    else:
        tresult = main.first_spline(x,y)
        assert tresult[0] == pytest.approx(result[0]) and tresult[1] == pytest.approx(result[1]),  'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.first_spline(x,y))

@pytest.mark.parametrize("x, y ,result", results_cubic_spline)
def test_cubic_spline(x: np.ndarray, y: np.ndarray, result):
    if result is None:
        assert main.cubic_spline(x,y) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.cubic_spline(x,y))
    else:
        tresult = main.cubic_spline(x,y)       
        assert tresult[0] == pytest.approx(result[0]) and tresult[1] == pytest.approx(result[1]) , 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.cubic_spline(x,y))