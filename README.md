# Eta
A small Python module for calculating eta, a measure to evaluate rankings in situations where multiple preference judgements are given for each item pair, but they may be noisy and/or incomplete.
See "Generalising Kendall's Tau for Noisy and Incomplete Preference Judgements" by R. Togashi and T. Sakai (2019), ICTIR 2019, http://dx.doi.org/10.1145/3341981.3344246.

## Installation

```sh
$ python setup.py sdist
$ pip install dist/eta-1.0.tar.gz
```

## Usage

The functions intended for external use are eta(), eta_p(), eta_dict(), and eta_p_dict(). eta() receives a list where each item corresponds to the index of the comparison matrix (array-like or list) as the second argument:

```python
>>> eta([0, 1, 2], [[1, 1, 1], [0, 1, 1], [0, 0, 1]])
    1.0
```
The function returns the value of eta measure for the ranking.

eta_p() is a utility to compute the eta_p measure for situations where multiple preference probabilities, rather than preference labels, are given for each document pair. eta_p() receives the same arguments as eta() except for the third argument, the variance matrix:

```python
>>> eta_p([0, 1, 2], [[1, 1, 1], [0, 1, 1], [0, 0, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    1.0
```
The function returns the value of eta_p measure for the ranking.

eta_dict() is a utility to compute the eta measure. eta_dict() receives a list where each item corresponds to the key of the sparse comparison matrix (dict) as the second arguments:

```python
>>> eta_dict(['a', 'b', 'c'], {('a', 'b'): 1, ('a', 'c'): 1, ('b', 'c'): 1})
    1.0
```

eta_p_dict() is a utility to compute the eta_p measure. eta_p_dict() receives the same arguments as eta_dict() except for the third argument, the sparse variance matrix (dict):

```python
>>> eta_p_dict(['a', 'b', 'c'], {('a', 'b'): 1, ('a', 'c'): 1, ('b', 'c'): 1}, {('a', 'b'): 0, ('a', 'c'): 0, ('b', 'c'): 0})
    1.0
```


### Committers
* Riku Togashi (@riktor)


## Contribution
Please read the CLA carefully before submitting your contribution to Mercari. Under any circumstances, by submitting your contribution, you are deemed to accept and agree to be bound by the terms and conditions of the CLA.

https://www.mercari.com/cla/

## License

Copyright 2019 Mercari, Inc.

eta is released under the MIT License.
