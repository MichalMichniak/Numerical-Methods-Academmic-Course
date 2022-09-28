import math
import numpy as np
import numpy.linalg as linalg
#checking if obj can be represented as float:
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def cylinder_area(r:float,h:float):
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
    if is_number(r) and is_number(h):
        if (float(r)>0) and (float(h)>0):
            return 2*math.pi*(float(r)**2) +float(h)*2*math.pi*float(r)
    return math.nan
#checking if an object can be represented as int:
def is_an_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
def fib(n:int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    if (type(n) == int):
        if int(n)>0:
            tab = [1,1]
            if int(n) == 1:
                return np.array([1])  #np.ndarray((int(n),),buffer=np.array([1]))
            elif int(n) == 2:
                return np.array(tab)
            else:
               for i in range(2,int(n)):
                   tab.append(tab[i-2]+tab[i-1])
            return np.array([tab])      
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
    if is_number(a):
        temp = np.array([[float(a),1,-float(a)],[0,1,1],[-float(a),float(a),1]])
        det = linalg.det(temp)
        return tuple([linalg.inv(temp) if det!=0 else np.NaN,temp.T,det])
    return None

def custom_matrix(m:int, n:int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    if (type(m) ==int) and (type(n) == int):
        if (m>0) and (n>0):
            return np.array([[max(i,j) for i in range(n)] for j in range(m)])
        
    return None
