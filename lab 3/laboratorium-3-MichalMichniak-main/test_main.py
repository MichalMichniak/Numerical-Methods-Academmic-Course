# -*- coding: utf-8 -*-

import pytest
import main
import pickle
import math
import numpy as np

from typing import Union, List, Tuple

expected = pickle.load(open('expected','rb'))

results_absolut_error = expected['absolut_error']
results_relative_error = expected['relative_error']
results_p_diff = expected['p_diff']
results_exponential = expected['exponential']
results_coskx1 = expected['coskx1']
results_coskx2 = expected['coskx2']
results_pi = expected['pi']


@pytest.mark.parametrize("v,v_aprox,result", results_absolut_error)
def test_absolut_error(v: Union[int, float, List, np.ndarray], v_aprox: Union[int, float, List, np.ndarray], result):
    if np.any(np.isnan(result)):
        assert np.isnan(main.absolut_error(v, v_aprox)), 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.absolut_error(v, v_aprox))
    else:
        assert main.absolut_error(v, v_aprox) == pytest.approx(result), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.absolut_error(v, v_aprox))


@pytest.mark.parametrize("v,v_aprox,result", results_relative_error)
def test_relative_error(v: Union[int, float, List, np.ndarray], v_aprox: Union[int, float, List, np.ndarray], result):
    if np.any(np.isnan(result)):
        assert np.isnan(main.relative_error(v, v_aprox)), 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.relative_error(v, v_aprox))
    else:
        assert main.relative_error(v, v_aprox) == pytest.approx(result), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.relative_error(v, v_aprox))


@pytest.mark.parametrize("n,c,result", results_p_diff)
def test_p_diff(n: int, c: Union[int, float], result):
    if np.any(np.isnan(result)):
        assert math.isnan(main.p_diff(n, c)), 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.p_diff(n, c))
    else:
        assert main.p_diff(n, c) == pytest.approx(result), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.p_diff(n, c))


@pytest.mark.parametrize("x,n,result", results_exponential)
def test_exponential(x: Union[int, float], n: int, result):
    if np.any(np.isnan(result)):
        assert np.isnan(main.exponential(x, n)), 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.exponential(x, n))
    else:
        assert main.exponential(x, n) == pytest.approx(result), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.exponential(x, n))


@pytest.mark.parametrize("k,x,result", results_coskx1)
def test_coskx1(k: int, x: Union[int, float], result):
    if np.any(np.isnan(result)):
        assert np.isnan(main.coskx1(k, x)), 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.coskx1(k, x))
    else:
        assert main.coskx1(k, x) == pytest.approx(result), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.coskx1(k, x))


@pytest.mark.parametrize("k,x,result", results_coskx2)
def test_coskx2(k: int, x: Union[int, float], result):
    if np.any(np.isnan(result)):
        assert np.isnan(main.coskx2(k, x)), 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.coskx2(k, x))
    else:
        assert main.coskx2(k, x) == pytest.approx(result), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.coskx2(k, x))


@pytest.mark.parametrize("n,result", results_pi)
def test_pi(n: int, result):
    if np.any(np.isnan(result)):
        assert math.isnan(main.pi(n)), 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.pi(n))
    else:
        assert main.pi(n) == pytest.approx(result), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.pi(n))

