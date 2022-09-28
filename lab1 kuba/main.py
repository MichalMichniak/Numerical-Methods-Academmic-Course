import math

import numpy as np
import scipy
import numpy.linalg as nl

def cylinder_area(r:float,h:float):
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
    try:
        float(r) and float(h)
        r=float(r)
        h=float(h)
        if (r>0 and h>0):
            return 2 * math.pi * r * r + 2 * math.pi * r * h
        else:
            return np.NaN
    except ValueError:
        return np.NaN
    
        
def fib(n:int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    
    fibo = np.array([1,1])
    if type(n)==int:
        if int(n) <= 0:
            return None
        elif n == 1:
            return np.array([1])
        elif n == 2:
            return fibo
        else: 
            for i in range(2,n):
                next_el=fibo[i-1]+fibo[i-2]
                fibo=np.append(fibo,[next_el])
            return np.array([list(fibo)])
    else:
        return None



    
    

def matrix_calculations(a:float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    M = np.array([[a,1,-a],[0,1,1],[-a,a,1]])
    Mt = np.transpose(M)
    Mdet = nl.det(M) 
    odp = ( nl.inv(M) if(Mdet!=0) else np.NaN,Mt,Mdet)
    return odp

def custom_matrix(m:int, n:int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 6.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 6.
    """
    if type(m) == int and type(n) == int:
        if m>0 and n>0:
            M = np.zeros([m,n])
            for i in range(0,m):
                for j in range(0,n):
                    if i>j:
                        M[i,j] = i
                    else:
                        M[i,j] = j
            return M
        else:
            return None
    else:
        return None

