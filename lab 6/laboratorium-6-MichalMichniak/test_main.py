# -*- coding: utf-8 -*-

import pytest
import main
import pickle
import math
import numpy as np

from typing import Union, List, Tuple

expected = pickle.load(open('expected','rb'))

results_random_matrix_Ab = expected['random_matrix_Ab'] 
result_residual_norm = expected['residual_norm'] 
results_log_sing_value = expected['log_sing_value'] 
results_order_sing_value = expected['order_sing_value']    
results_create_matrix_from_A = expected['create_matrix_from_A'] 

@pytest.mark.parametrize("m,result", results_random_matrix_Ab)
def test_random_matrix_Ab(m:int, result):
    if result is None:
        assert main.random_matrix_Ab(m) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.random_matrix_Ab(m))
    else:
        A,b = main.random_matrix_Ab(m)
        assert isinstance(A, np.ndarray), 'Wynik nie jest odpowiedniego typu. Spodziewany wynik: np.ndarray, aktualny {0}. '.format(type(A))
        assert len(A.shape) == 2 , 'Wynik nie jest macierzą dwuwymiarową. Spodziewany wynik: 2, aktualny {0}. '.format(len(A.shape))
        assert A.shape[0] == m and A.shape[1] == m, 'Wynik nie jest macierzą kwadratową. Spodziewany wynik: ({0},{0}), aktualny ({1},{2}). '.format(m,A.shape[0],A.shape[1])
        assert isinstance(b, np.ndarray), 'Wynik nie jest odpowiedniego typu. Spodziewany wynik: np.ndarray, aktualny {0}. '.format(type(b))
        assert len(b.shape) == 1 , 'Wynik nie jest wektorem (m,). Spodziewany wynik: 1, aktualny ({1},). '.format(m,len(A.shape))
        assert b.shape[0] == m , 'Wynik nie jest wektorem długości m.. Spodziewany wynik: ({0},), aktualny ({1},). '.format(m,A.shape[0])
        

@pytest.mark.parametrize("A,x, b,result", result_residual_norm)
def test_residual_norm(A: np.ndarray, x: np.ndarray,b: np.ndarray, result):
    if result is None:
        assert main.residual_norm(A,x,b) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.residual_norm(A,x,b))
    else:    
        assert main.residual_norm(A,x,b) == pytest.approx(result), 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.residual_norm(A,x,b))

@pytest.mark.parametrize("n,min_order, max_order,result", results_log_sing_value)
def test_log_sing_value(n:int, min_order:Union[int,float], max_order:Union[int,float], result):
    if result is None:
        assert main.log_sing_value(n,min_order,max_order) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.log_sing_value(n,min_order,max_order))
    else:    
        assert main.log_sing_value(n,min_order,max_order) == pytest.approx(result), 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.log_sing_value(n,min_order,max_order))

@pytest.mark.parametrize("n,order,site,result", results_order_sing_value)
def test_order_sing_value(n:int, order:Union[int,float], site:str, result):
    if result is None:
        assert main.order_sing_value(n,order,site) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.order_sing_value(n,order,site))
    else:
        b = main.order_sing_value(n,order,site)
        assert isinstance(b, np.ndarray), 'Wynik nie jest odpowiedniego typu. Spodziewany wynik: np.ndarray, aktualny {0}. '.format(type(b))
        assert len(b.shape) == 1 , 'Wynik nie jest wektorem (m,). Spodziewany wynik: 1, aktualny ({1},). '.format(n,len(b.shape))
        assert b.shape[0] == n , 'Wynik nie jest wektorem długości m. Spodziewany wynik: ({0},), aktualny ({1},). '.format(n,b.shape[0])
        assert  np.sort(b)[::-1] == pytest.approx(b), 'Wynik nie jest postortowany w odpowiedni sposób. Spodziewany wynik: ({0},), aktualny ({1},).'.format(np.sort(b)[::-1],b)
        
@pytest.mark.parametrize("A,sing_value,result", results_create_matrix_from_A)
def test_create_matrix_from_A(A:np.ndarray, sing_value:np.ndarray, result):
    if result is None:
        assert main.create_matrix_from_A(A,sing_value) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.create_matrix_from_A(A,sing_value))
    else:    
        assert main.create_matrix_from_A(A,sing_value) == pytest.approx(result), 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.create_matrix_from_A(A,sing_value))
