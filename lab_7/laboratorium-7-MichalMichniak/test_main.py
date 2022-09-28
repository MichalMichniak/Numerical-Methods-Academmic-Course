# -*- coding: utf-8 -*-

import pytest
import main
import pickle
import math
import numpy as np

from typing import Union, List, Tuple

expected = pickle.load(open('expected','rb'))

result_spare_matrix_Abt = expected['spare_matrix_Abt']
result_square_from_rectan = expected['square_from_rectan'] 
result_residual_norm =expected['residual_norm'] 

@pytest.mark.parametrize("m,n,result", result_spare_matrix_Abt)
def test_spare_matrix_Abt(m:int,n:int, result):
    if result is None:
        assert main.spare_matrix_Abt(m,n) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.spare_matrix_Abt(m,n))
    else:
        A, b = main.spare_matrix_Abt(int(m),int(n))
        assert A == pytest.approx(result[0]) and b == pytest.approx(result[1]), 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.spare_matrix_Abt(m,n))

@pytest.mark.parametrize("A,x, b,result", result_residual_norm)
def test_residual_norm(A: np.ndarray, x: np.ndarray,b: np.ndarray, result):
    if result is None:
        assert main.residual_norm(A,x,b) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.residual_norm(A,x,b))
    else:    
        assert main.residual_norm(A,x,b) == pytest.approx(result), 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.residual_norm(A,x,b))

@pytest.mark.parametrize("A,b,result", result_square_from_rectan)
def test_square_from_rectan(A: np.ndarray, b: np.ndarray, result):
    if result is None:
        assert main.square_from_rectan(A,b) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.square_from_rectan(A,b))
    else:
        At, bt = main.square_from_rectan(A,b)
        assert At == pytest.approx(result[0]) and bt == pytest.approx(result[1]), 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.square_from_rectan(A,b))
