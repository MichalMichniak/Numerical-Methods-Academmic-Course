# -*- coding: utf-8 -*-

import pytest
import main
import pickle
import math
import numpy as np

from typing import Union, List, Tuple

expected = pickle.load(open('expected','rb'))

results_chebyshev_nodes = expected['chebyshev_nodes']
results_bar_czeb_weights = expected['bar_czeb_weights']
results_L_inf = expected['L_inf']
results_barycentric_inte = expected['barycentric_inte']
# results_coskx1 = expected['coskx1']
# results_coskx2 = expected['coskx2']
# results_pi = expected['pi']


@pytest.mark.parametrize("n,result", results_chebyshev_nodes)
def test_chebyshev_nodes(n:int, result):
    if result is None:
        assert main.chebyshev_nodes(n) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.chebyshev_nodes(n))
    else:
        assert main.chebyshev_nodes(n) == pytest.approx(result), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.chebyshev_nodes(n))

@pytest.mark.parametrize("n,result", results_bar_czeb_weights)
def test_bar_czeb_weights(n:int, result):
    if result is None:
        assert main.bar_czeb_weights(n) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.bar_czeb_weights(n))
    else:
        assert main.bar_czeb_weights(n) == pytest.approx(result), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.bar_czeb_weights(n))
        
@pytest.mark.parametrize("xr, x ,result", results_L_inf)
def test_bar_L_inf(xr:Union[int, float, List, np.ndarray], x: Union[int, float, List, np.ndarray], result):
    if np.isnan(result):
        assert np.isnan(main.L_inf(xr,x)), 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.L_inf(xr,x))
    else:
        assert main.L_inf(xr,x) == pytest.approx(result), 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.L_inf(xr,x))
        
@pytest.mark.parametrize("xi,yi,wi,x,result", results_barycentric_inte)
def test_barycentric_inte(xi:np.ndarray,yi:np.ndarray,wi:np.ndarray,x:np.ndarray, result):
    if result is None:
        assert main.barycentric_inte(xi,yi, wi,x) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.barycentric_inte(xi,yi, wi,x))
    else:
        assert main.barycentric_inte(xi,yi, wi,x) == pytest.approx(result), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.barycentric_inte(xi,yi, wi,x))
