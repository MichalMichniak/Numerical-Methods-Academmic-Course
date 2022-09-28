import pytest
import main
import pickle
import math
import numpy as np

expected = pickle.load(open('expected','rb'))

results_cylinder_area = expected['cylinder_area']
results_fib = expected['fib']
results_matrix_calculations = expected['matrix_calculations']
results_custom_matrix = expected['custom_matrix']

@pytest.mark.parametrize("r,h,result", results_cylinder_area)
def test_cylinder_area(r:float,h:float,result):
    if math.isnan(result):
        assert math.isnan(main.cylinder_area(r,h)), 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.cylinder_area(r,h))
    else:
        assert main.cylinder_area(r,h) == pytest.approx(result), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.cylinder_area(r,h))

@pytest.mark.parametrize("n,result", results_fib)
def test_fib(n:int,result):
    if result is None:
        assert main.fib(n) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.fib(n))
    else:
        assert main.fib(n) == pytest.approx(result), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.fib(n))

@pytest.mark.parametrize("a,result", results_matrix_calculations)
def test_matrix_calculations(a:float,result):
    test_result = main.matrix_calculations(a)
    if not isinstance(result[0], np.ndarray):
        assert math.isnan(test_result[0]) and test_result[1] == pytest.approx(result[1]) and test_result[2] == pytest.approx(result[2])
    else:
        assert test_result[0] == pytest.approx(result[0]) and test_result[1] == pytest.approx(result[1]) and test_result[2] == pytest.approx(result[2])

@pytest.mark.parametrize("m,n,result", results_custom_matrix)
def test_custom_matrix(m:int, n:int,result):
        if result is None:
            assert main.custom_matrix(m,n) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.custom_matrix(m,n))
        else:
            assert main.custom_matrix(m,n) == pytest.approx(result), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.custom_matrix(m,n))
