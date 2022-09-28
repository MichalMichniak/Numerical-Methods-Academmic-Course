import numpy as np
import scipy as sp
import pickle

from typing import Union, List, Tuple, Optional


def diag_dominant_matrix_A_b(m: int) -> Tuple[np.ndarray, np.ndarray]:
    """Funkcja tworząca zestaw składający się z macierzy A (m,m), wektora b (m,) o losowych wartościach całkowitych z przedziału 0, 9
    Macierz A ma być diagonalnie zdominowana, tzn. wyrazy na przekątnej sa wieksze od pozostałych w danej kolumnie i wierszu
    Parameters:
    m int: wymiary macierzy i wektora
    
    Returns:
    Tuple[np.ndarray, np.ndarray]: macierz diagonalnie zdominowana o rozmiarze (m,m) i wektorem (m,)
                                   Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    try:
        if type(m) != int or m<1:
            raise ValueError
        arr = np.array([[np.random.randint(0,9) for i in range(m)] for j in range(m)])
        for i in range(len(arr)):
            arr[i,i] = np.sum(abs(arr[:,i]))+np.sum(abs(arr[i,:])) - 2*abs(arr[i,i])
        return arr , np.array([np.random.randint(0,9) for j in range(m)])
    except:
        return None


def is_diag_dominant(A: np.ndarray) -> bool:
    """Funkcja sprawdzająca czy macierzy A (m,m) jest diagonalnie zdominowana
    Parameters:
    A np.ndarray: macierz wejściowa
    
    Returns:
    bool: sprawdzenie warunku 
          Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    try:
        if A.shape[0] != A.shape[1]:
            raise ValueError
        for i in range(len(A)):
            if A[i,i] < max(np.sum(abs(A[:,i]))-abs(A[i,i]),np.sum(abs(A[i,:]))-abs(A[i,i])):
                return False
        return True
    except:
        return None

def symmetric_matrix_A_b(m: int) -> Tuple[np.ndarray, np.ndarray]:
    """Funkcja tworząca zestaw składający się z macierzy A (m,m), wektora b (m,) o losowych wartościach całkowitych z przedziału 0, 9
    Parameters:
    m int: wymiary macierzy i wektora
    
    Returns:
    Tuple[np.ndarray, np.ndarray]: symetryczną macierz o rozmiarze (m,m) i wektorem (m,)
                                   Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    try:
        if type(m) != int or m<1:
            raise ValueError
        arr = np.array([[np.random.randint(0,9) for i in range(m)] for j in range(m)])
        arr = (arr+np.transpose(arr))
        return arr , np.array([np.random.randint(0,9) for j in range(m)])
    except:
        return None
    return None


def is_symmetric(A: np.ndarray) -> bool:
    """Funkcja sprawdzająca czy macierzy A (m,m) jest symetryczna
    Parameters:
    A np.ndarray: macierz wejściowa
    
    Returns:
    bool: sprawdzenie warunku 
          Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    try:
        if A.shape[0] != A.shape[1]:
            raise ValueError
        for i in range(len(A)):
            for j in range(i):
                if A[i,j] != A[j,i]:
                    return False
        return True
    except:
        return None


def solve_jacobi(A: np.ndarray, b: np.ndarray, x_init: np.ndarray,
                 epsilon: Optional[float] = 1e-8, maxiter: Optional[int] = 100) -> Tuple[np.ndarray, int]:
    """Funkcja tworząca zestaw składający się z macierzy A (m,m), wektora b (m,) o losowych wartościach całkowitych
    Parameters:
    A np.ndarray: macierz współczynników
    b np.ndarray: wektor wartości prawej strony układu
    x_init np.ndarray: rozwiązanie początkowe
    epsilon Optional[float]: zadana dokładność
    maxiter Optional[int]: ograniczenie iteracji
    
    Returns:
    np.ndarray: przybliżone rozwiązanie (m,)
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    int: iteracja
    """
    try:
        if A.shape[0] != A.shape[1] or len(b) != A.shape[0] or maxiter<1:
            raise ValueError
        D = np.diag(np.diag(A))
        LU = A - D
        x = x_init
        D_inv = np.diag(1 / np.diag(D))
        resid=[]
        for i in range(maxiter):
            x_new = np.dot(D_inv, b - np.dot(LU, x))
            r_norm = np.linalg.norm(x_new - x)
            resid.append(r_norm)
            if  r_norm< epsilon:
                return x_new,resid
            x = x_new
        return x,resid
    except:
        return None