"""
Eta measure, a generalised Kendall's tau for noisy and incomplete judgements.
See http://doi.acm.org/10.1145/3341981.3344246 for details.
"""

def eta(ranking, pref):
    """Return the (normalised) eta measure.

    Parameters
    ----------
    ranking : list or array-like
        ranking that stores id. Each id corresponds to the index of the comparison matrix.
    pref : list or array-like
        comparison matrix. Ensure that it satisfies pref[x][y] == 1 - pref[y][x] and 0 <= pref[x][y] <= 1. 

    Returns
    -------
    eta_mesure : float
        the value of eta measure for the ranking under the preference

    >>> eta([0, 1, 2], [[1, 1, 1], [0, 1, 1], [0, 0, 1]])
    1.0
    >>> eta([2, 1, 0], [[1, 1, 1], [0, 1, 1], [0, 0, 1]])
    -1.0
    >>> eta([2, 1, 3, 0], [[0.5, 0.2, 0.4, 0.3], [0.8, 0.5, 0.1, 0.4], [0.6, 0.9, 0.5, 0.4], [0.7, 0.6, 0.6, 0.5]])
    0.6666666666666667
    """

    N = len(ranking)
    ideal = 0
    _eta = 0
    for i in range(N):
        for j in range(i+1, N):
            x = ranking[i]
            y = ranking[j]
            p_ij = pref[x][y]
            delta_ij = 1 if i < j else -1
            true_delta_ij = 1 if p_ij > 0.5 else -1
            label = (2 * p_ij - 1)
            _eta += label * delta_ij
            ideal += label * true_delta_ij
    eta_measure = _eta / ideal
    return eta_measure


def eta_p(ranking, Ep, Vp):
    """Return the (normalised) eta_p measure.

    Parameters
    ----------
    ranking : list or array-like
        ranking
    Ep : list or array-like
        comparison matrix. Ensure that it satisfies Ep[x][y] == 1 - Ep[y][x] and 0 <= Ep[x][y] <= 1.   
    Vp : list or array-like
        variance matrix with the shape of (n, n).
        Ensure that it satisfies Vp[x][y] == Vp[y][x] and 0 <= Vp[x][y].  

    Returns
    -------
    eta_p_mesure : float
        the value of eta_p measure for the ranking under the preference
    
    >>> eta_p([0, 1, 2], [[1, 1, 1], [0, 1, 1], [0, 0, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    1.0
    >>> eta_p([2, 1, 0], [[1, 1, 1], [0, 1, 1], [0, 0, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    -1.0
    >>> eta_p([2, 1, 3, 0], [[0.5, 0.2, 0.4, 0.3], [0.8, 0.5, 0.1, 0.4], [0.6, 0.9, 0.5, 0.4], [0.7, 0.6, 0.6, 0.5]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    0.6666666666666667
    """
    
    N = len(ranking)
    ideal = 0 
    _eta = 0
    for i in range(N):
        for j in range(i+1, N):
            x = ranking[i]
            y = ranking[j]
            ep = Ep[x][y]
            vp = Vp[x][y]
            delta_ij = 1 if i < j else -1
            true_delta_ij = 1 if ep > 0.5 else -1
            label = (2 * ep - 1) / (1 + vp)
            _eta += label * delta_ij 
            ideal += label * true_delta_ij
    eta_p_measure = _eta / ideal
    return eta_p_measure


def eta_dict(ranking, pref):
    """Return the (normalised) eta measure from sparse comparison matrix (as dict).
    
    Parameters
    ----------
    ranking : list or array-like
        ranking that stores id. Each id corresponds to the key of the comparison matrix (dict).
    pref : dict
        comparison matrix. Ensure that it satisfies pref[(x, y)] == 1 - pref[(y, x)] and 0 <= pref[(x, y)] <= 1.
        If you set the pref[(x, y)], you can omit pref[(y, x)] by assuming pref[(y, x)] = 1 - pref[(x, y)].

    Returns
    -------
    eta_mesure : float
        the value of eta_p measure for the ranking under the preference

    >>> eta_dict(['a', 'b', 'c'], {('a', 'b'): 1, ('a', 'c'): 1, ('b', 'c'): 1})
    1.0
    >>> eta_dict(['c', 'b', 'a'], {('a', 'b'): 1, ('a', 'c'): 1, ('b', 'c'): 1})
    -1.0
    >>> eta_dict(['c', 'b', 'd', 'a'], {('a', 'b'): 0.2, ('a', 'c'): 0.4, ('a', 'd'): 0.3, ('b', 'c'): 0.1, ('b', 'd'): 0.4, ('c', 'd'): 0.4})
    0.6666666666666667
    >>> eta_dict(['c', 'b', 'd', 'a'], {('b', 'a'): 0.8, ('a', 'c'): 0.4, ('a', 'd'): 0.3, ('b', 'c'): 0.1, ('b', 'd'): 0.4, ('c', 'd'): 0.4})
    0.6666666666666667
    >>> eta_dict(['c', 'b', 'd', 'a'], {('b', 'a'): 0.8, ('c', 'a'): 0.6, ('d', 'a'): 0.7, ('c', 'b'): 0.9, ('b', 'd'): 0.4, ('c', 'd'): 0.4}) 
    0.6666666666666667
    """

    N = len(ranking)
    ideal = 0 
    _eta = 0
    for i in range(N):
        for j in range(i+1, N):
            x = ranking[i]
            y = ranking[j]
            if (x, y) in pref:
                p_ij = pref[(x, y)]
                delta_ij = 1 if i < j else -1
                true_delta_ij = 1 if p_ij  > 0.5 else -1
                label = (2 * p_ij - 1)
                _eta += label * delta_ij
                ideal += label * true_delta_ij
            elif (y, x) in pref:
                p_ji = pref[(y, x)]
                delta_ji = 1 if j < i else -1
                true_delta_ji = 1 if p_ji  > 0.5 else -1
                label = (2 * p_ji - 1)
                _eta += label * delta_ji
                ideal += label * true_delta_ji
    eta_measure = _eta / ideal
    return eta_measure


def eta_p_dict(ranking, Ep, Vp):
    """Return the (normalised) eta measure from sparse comparison matrix and its sparse variance matrix.

    Parameters
    ----------
    ranking : list or array-like
        ranking that stores id. Each id corresponds to the key of the comparison matrix (dict).
    Ep : dict
        sparse comparison matrix. Ensure that it satisfies Ep[(x, y)] == 1 - Ep[(y, x)] and 0 <= Ep[(x, y)] <= 1.
        If you set the Ep[(x, y)], you can omit Ep[(y, x)] by assuming Ep[(y, x)] = 1 - Ep[(x, y)].
    Vp : dict
        sparse variance matrix. Ensure that it satisfies Vp[(x, y)] == Vp[(y, x)] and 0 <= Vp[(x, y)].
        If you set the Vp[(x, y)], you can omit Vp[(y, x)] by assuming Vp[(y, x)] = Vp[(x, y)].

    Returns
    -------
    eta_p_mesure : float
        the value of eta_p measure for the ranking under the preference

    >>> eta_p_dict(['a', 'b', 'c'], {('a', 'b') : 1, ('a', 'c'): 1, ('b', 'c'): 1}, {('a', 'b') : 0, ('a', 'c'): 0, ('b', 'c'): 0})
    1.0
    >>> eta_p_dict(['c', 'b', 'a'], {('a', 'b') : 1, ('a', 'c'): 1, ('b', 'c'): 1}, {('a', 'b') : 0, ('a', 'c'): 0, ('b', 'c'): 0})
    -1.0
    >>> eta_p_dict(['c', 'b', 'd', 'a'], {('a', 'b'): 0.2, ('a', 'c'): 0.4, ('a', 'd'): 0.3, ('b', 'c'): 0.1, ('b', 'd'): 0.4, ('c', 'd'): 0.4}, {('a', 'b'): 0, ('a', 'c'): 0, ('a', 'd'): 0, ('b', 'c'): 0, ('b', 'd'): 0, ('c', 'd'): 0})
    0.6666666666666667
    >>> eta_p_dict(['c', 'b', 'd', 'a'], {('b', 'a'): 0.8, ('a', 'c'): 0.4, ('a', 'd'): 0.3, ('b', 'c'): 0.1, ('b', 'd'): 0.4, ('c', 'd'): 0.4}, {('b', 'a'): 0, ('a', 'c'): 0, ('a', 'd'): 0, ('b', 'c'): 0, ('b', 'd'): 0, ('c', 'd'): 0})
    0.6666666666666667
    >>> eta_p_dict(['c', 'b', 'd', 'a'], {('b', 'a'): 0.8, ('c', 'a'): 0.6, ('d', 'a'): 0.7, ('c', 'b'): 0.9, ('b', 'd'): 0.4, ('c', 'd'): 0.4}, {('b', 'a'): 0, ('c', 'a'): 0, ('d', 'a'): 0, ('c', 'b'): 0, ('b', 'd'): 0, ('c', 'd'): 0})
    0.6666666666666667
    """

    N = len(ranking)
    ideal = 0
    _eta = 0
    for i in range(N):
        for j in range(i+1, N):
            x = ranking[i]
            y = ranking[j]
            if (x, y) in Ep:
                ep_ij = Ep[(x, y)]
                vp_ij = Vp[(x, y)]
                delta_ij = 1 if i < j else -1
                true_delta_ij = 1 if ep_ij > 0.5 else -1
                label = (2 * ep_ij - 1) / (1 + vp_ij)
                _eta += label * delta_ij
                ideal += label * true_delta_ij
            elif (y, x) in Ep:
                ep_ji = Ep[(y, x)]
                vp_ji = Vp[(y, x)]
                delta_ji = 1 if j < i else -1
                true_delta_ji = 1 if ep_ji > 0.5 else -1
                label = (2 * ep_ji - 1) / (1 + vp_ji)
                _eta += label * delta_ji
                ideal += label * true_delta_ji
    eta_p_measure = _eta / ideal
    return eta_p_measure


if __name__ == "__main__":
    import doctest
    doctest.testmod()
