import sys
import os
from os import path
from setuptools import setup


ROOT_DIR = path.abspath(path.dirname(__file__))
sys.path.insert(0, ROOT_DIR)

LONG_DESCRIPTION = open(path.join(ROOT_DIR, 'README.md')).read()

here = os.path.dirname(os.path.abspath(__file__))
version = 1.0


setup(
    name='eta',
    version=version,
    description='eta: Eta measure, Generalising Kendall\'s Tau for Noisy and Incomplete Judgements',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/kouzoh/eta/',
    author='Riku Togashi',
    author_email='riktor@mercari.com',
    license='MIT License',
    classifiers=[
	'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='eta IR evaluation',
    install_requires=[
    ],
    platforms='any',
)
