# -*- coding: utf-8 -*-

import pytest
import main
import pickle
import math
import numpy as np

from typing import Union, List, Tuple, Optional

expected = pickle.load(open('expected','rb'))

result_diag_dominant_matrix_A_b = expected['result_diag_dominant_matrix_A_b']
result_is_diag_dominant = expected['result_is_diag_dominant']
result_symmetric_matrix_A_b = expected['result_symmetric_matrix_A_b']
result_is_symmetric = expected['result_is_symmetric']
result_solve_jacobi = expected['result_solve_jacobi']

@pytest.mark.parametrize("m, result", result_diag_dominant_matrix_A_b)
def test_diag_dominant_matrix_A_b(m:int, result):
    test = main.diag_dominant_matrix_A_b(m)
    if result is None:
        assert test is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, test)
    else:
        A, b = test
        assert len(A.shape) == 2 , 'Wynik nie jest macierzą dwuwymiarową. Spodziewany wynik: 2, aktualny {0}. '.format(len(A.shape))
        assert A.shape[0] == A.shape[1] , 'Wynik nie jest macierzą kwadratową. Spodziewany wynik: {0}, aktualny {1}. '.format((m , m), A.shape)
        assert main.is_diag_dominant(A) , 'Wynik nie jest macierzą zdominowana diagonalnie.'

@pytest.mark.parametrize("A, result", result_is_diag_dominant)
def test_is_diag_dominant(A: np.ndarray, result):
    test = main.is_diag_dominant(A)
    if result is None:
        assert test is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, test)
    else:
        assert test == result, 'Spodziewany wynik: {0}, aktualny {1}.'.format(result, test)

@pytest.mark.parametrize("m, result", result_symmetric_matrix_A_b)
def test_symmetric_matrix_A_b(m:int, result):
    test = main.symmetric_matrix_A_b(m)
    if result is None:
        assert test is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, test)
    else:
        A, b = test
        assert len(A.shape) == 2 , 'Wynik nie jest macierzą dwuwymiarową. Spodziewany wynik: 2, aktualny {0}. '.format(len(A.shape))
        assert A.shape[0] == A.shape[1] , 'Wynik nie jest macierzą kwadratową. Spodziewany wynik: {0}, aktualny {1}. '.format((m , m), A.shape)
        assert main.is_symmetric(A) , 'Wynik nie jest macierzą symetryczna.'

@pytest.mark.parametrize("A, result", result_is_symmetric)
def test_is_symmetric(A: np.ndarray, result):
    test = main.is_symmetric(A)
    if result is None:
        assert test is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, test)
    else:
        assert test == result, 'Spodziewany wynik: {0}, aktualny {1}.'.format(result, test)

@pytest.mark.parametrize("A,b,x_init,epsilon,maxiter,result", result_solve_jacobi)
def test_solve_jacobi(A: np.ndarray, b: np.ndarray, x_init: np.ndarray,
                      epsilon: Optional[float], maxiter: Optional[int], result):
    test = main.solve_jacobi(A, b, x_init, epsilon=epsilon, maxiter=maxiter)
    if result is None:
        assert test is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, test)
    else:    
        assert test[0] == pytest.approx(result[0]), 'Spodziewany wynik: {0}, aktualny {1}.'.format(result, test)
