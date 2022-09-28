import numpy as np
import numpy.linalg as linalg
import scipy
import pickle
import math
from typing import Union, List, Tuple


def absolut_error(v: Union[int, float, List, np.ndarray], v_aprox: Union[int, float, List, np.ndarray]) -> Union[int, float, np.ndarray]:
    """Obliczenie błędu bezwzględnego. 
    Funkcja powinna działać zarówno na wartościach skalarnych, listach jak i wektorach/macierzach biblioteki numpy.
    
    Parameters:
    v (Union[int, float, List, np.ndarray]): wartość dokładna 
    v_aprox (Union[int, float, List, np.ndarray]): wartość przybliżona
    
    Returns:
    err Union[int, float, np.ndarray]: wartość błędu bezwzględnego,
                                       NaN w przypadku błędnych danych wejściowych
    """
    try:
        return abs(np.array(v_aprox)-np.array(v))
    except:
        return np.NaN

def relative_error(v: Union[int, float, List, np.ndarray], v_aprox: Union[int, float, List, np.ndarray]) -> Union[int, float, np.ndarray]:
    """Obliczenie błędu względnego.
    Funkcja powinna działać zarówno na wartościach skalarnych, listach jak i wektorach/macierzach biblioteki numpy.
    
    Parameters:
    v (Union[int, float, List, np.ndarray]): wartość dokładna 
    v_aprox (Union[int, float, List, np.ndarray]): wartość przybliżona
    
    Returns:
    err Union[int, float, np.ndarray]: wartość błędu względnego,
                                       NaN w przypadku błędnych danych wejściowych
    """
    # błędy robią BRRRRRRRRRRRRRRRRR
    try:
        if np.array(v).all() == 0:
            raise ValueError
        return abs((np.array(v_aprox)-np.array(v))/np.array(v))
    except:
        return np.NaN


def p_diff(n: int, c: float) -> float:
    """Funkcja wylicza wartości wyrażeń P1 i P2 w zależności od n i c.
    Następnie zwraca wartość bezwzględną z ich różnicy.
    Szczegóły w Zadaniu 2.
    
    Parameters:
    n Union[int]: 
    c Union[int, float]: 
    
    Returns:
    diff float: różnica P1-P2
                NaN w przypadku błędnych danych wejściowych
    """
    try:
        if(type(n) != int):
            raise ValueError
        P1 = c-c+pow(2,n)
        P2 = c+pow(2,n)-c
        return abs(P1 - P2)
    except:
        return np.NaN


def exponential(x: Union[int, float], n: int) -> float:
    """Funkcja znajdująca przybliżenie funkcji exp(x).
    Do obliczania silni można użyć funkcji scipy.math.factorial(x)
    Szczegóły w Zadaniu 3.
    
    Parameters:
    x Union[int, float]: wykładnik funkcji ekspotencjalnej 
    n Union[int]: liczba wyrazów w ciągu
    
    Returns:
    exp_aprox float: aproksymowana wartość funkcji,
                     NaN w przypadku błędnych danych wejściowych
    """
    def wyraz(j: int, value : Union[int, float]):
            return value**j/(scipy.math.factorial(j))
    try:
        if (type(n) != int) or (n<0):
            raise ValueError
        sum : float = 0
        for i in range(n):
            sum+=wyraz(i,x)
        return sum
    except:
        return np.NaN
    


def coskx1(k: int, x: Union[int, float]) -> float:
    """Funkcja znajdująca przybliżenie funkcji cos(kx). Metoda 1.
    Szczegóły w Zadaniu 4.
    
    Parameters:
    x Union[int, float]:  
    k Union[int]: 
    
    Returns:
    coskx float: aproksymowana wartość funkcji,
                 NaN w przypadku błędnych danych wejściowych
    """

    t = {}
    def coskx1_rekursja(k1 : int, x1 : Union[int,float]):
        if(k1==1):
            return np.cos(x1)
        if(k1 == 0):
            return 1.0
        if k1 in t.keys():
            return t[k1]
        temp = 2*np.cos(x1)*coskx1_rekursja(k1-1 , x1) - coskx1_rekursja(k1-2 , x1)
        t[k1] = temp
        return temp
    try:
        if type(k) != int or k<0:
                return np.NaN
        return coskx1_rekursja(k,x)
    except:
        return np.NaN


def coskx2(k: int, x: Union[int, float]) -> Tuple[float, float]:
    """Funkcja znajdująca przybliżenie funkcji cos(kx). Metoda 2.
    Szczegóły w Zadaniu 4.
    
    Parameters:
    x Union[int, float]:  
    k Union[int]: 
    
    Returns:
    coskx, sinkx float: aproksymowana wartość funkcji,
                        NaN w przypadku błędnych danych wejściowych
    """
    tsin = {}
    tcos = {}
    def sinkx_recursion(k1: int, x1: Union[int , float]):
        if(k1 == 0):
            return np.sin(0)
        if k1 in tsin.keys():
            return tsin[k1]
        temp = np.sin(x1)*coskx_recursion(k1-1,x1) + np.cos(x1)*sinkx_recursion(k1-1,x1)
        tsin[k1] = temp
        return temp
    def coskx_recursion(k1: int, x1: Union[int , float]):
        if(k1 == 0):
            return np.cos(0)
        if k1 in tcos.keys():
            return tcos[k1]
        temp = np.cos(x1)*coskx_recursion(k1-1,x1) - np.sin(x1)*sinkx_recursion(k1-1,x1)
        tcos[k1] = temp
        return temp    
    try:
        if (type(k) != int) or k<0:
            raise ValueError
        return tuple([coskx_recursion(k,x),sinkx_recursion(k,x)])
    except:
        return np.NaN
    


def pi(n: int) -> float:
    """Funkcja znajdująca przybliżenie wartości stałej pi.
    Szczegóły w Zadaniu 5.
    
    Parameters:
    n Union[int, List[int], np.ndarray[int]]: liczba wyrazów w ciągu
    
    Returns:
    pi_aprox float: przybliżenie stałej pi,
                    NaN w przypadku błędnych danych wejściowych
    """
    try:
        if type(n) != int or n<1:
            raise ValueError
        sum = 0
        for i in range(1,n+1):
            sum+=6/pow(i,2)
        return math.sqrt(sum)
    except:
        return np.NaN
x = 0   