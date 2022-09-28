import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg
from numpy.core._multiarray_umath import ndarray
from numpy.polynomial import polynomial as P
import pickle

# zad1
def polly_A(x: np.ndarray):
    """Funkcja wyznaczajaca współczynniki wielomianu przy znanym wektorze pierwiastków.
    Parameters:
    x: wektor pierwiastków
    Results:
    (np.ndarray): wektor współczynników
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    try:
        if len(x) == 0 or type(x) != ndarray:
            raise ValueError
        return P.polyfromroots(x)
    except:
        return None

def roots_20(a: np.ndarray):
    """Funkcja zaburzająca lekko współczynniki wielomianu na postawie wyznaczonych współczynników wielomianu
        oraz zwracająca dla danych współczynników, miejsca zerowe wielomianu funkcją polyroots.
    Parameters:
    a: wektor współczynników
    Results:
    (np.ndarray, np. ndarray): wektor współczynników i miejsc zerowych w danej pętli
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    try:
        if type(a) != ndarray:
            raise ValueError
        err = np.random.random_sample(size = len(a)) * 10**-10
        return a+err ,P.polyroots(a + err)
    except:
        return None


# zad 2

def frob_a(wsp: np.ndarray):
    """Funkcja zaburzająca lekko współczynniki wielomianu na postawie wyznaczonych współczynników wielomianu
        oraz zwracająca dla danych współczynników, miejsca zerowe wielomianu funkcją polyroots.
    Parameters:
    a: wektor współczynników
    Results:
    (np.ndarray, np. ndarray, np.ndarray, np. ndarray,): macierz Frobenusa o rozmiarze nxn, gdzie n-1 stopień wielomianu,
    wektor własności własnych, wektor wartości z rozkładu schura, wektor miejsc zerowych otrzymanych za pomocą funkcji polyroots

                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    try:
        frob = np.array([np.array([1 if i+1 == j else 0 for j in range(len(wsp))]) if i != len(wsp)-1 else -1*wsp for i in range(len(wsp))])
        return frob, np.linalg.eigvals(frob), scipy.linalg.schur(frob, output='complex') , P.polyroots(wsp)
    except:
        return None

## poprawna:
def frob_a_vol2(wsp: np.ndarray):
    """Funkcja zaburzająca lekko współczynniki wielomianu na postawie wyznaczonych współczynników wielomianu
        oraz zwracająca dla danych współczynników, miejsca zerowe wielomianu funkcją polyroots.
    Parameters:
    a: wektor współczynników
    Results:
    (np.ndarray, np. ndarray, np.ndarray, np. ndarray,): macierz Frobenusa o rozmiarze nxn, gdzie n-1 stopień wielomianu,
    wektor własności własnych, wektor wartości z rozkładu schura, wektor miejsc zerowych otrzymanych za pomocą funkcji polyroots

                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    try:
        wsp_t = wsp
        wsp = wsp/wsp[0]
        frob = np.array([np.array([1 if i+1 == j else 0 for j in range(len(wsp)-1)]) if i != len(wsp)-2 else -1*wsp[1:][::-1] for i in range(len(wsp)-1)])
        return frob, np.linalg.eigvals(frob), np.array([scipy.linalg.schur(frob, output='complex')[0][i,i] for i in range(len(wsp)-1)]) , P.polyroots(wsp_t[::-1])
    except:
        return None
