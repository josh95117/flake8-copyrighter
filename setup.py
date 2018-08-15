#
# setup.py
#
# Copyright (c) 2018 Joshua Hadley
#

from setuptools import setup

setup(
    name='flake8-copyrighter',
    version='1.0.0',
    description='Flake8 extension to check copyright date '
                'against file modification date',
    author='Joshua Hadley',
    author_email='joshua.hadley@gmail.com',
    url='https://github.com/josh95117/flake8-copyrighter',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Framework :: Flake8',
    ],

    entry_points={
        'flake8.extension': [
            'CRC000 = flake8_copyrighter:CopyrightDateChecker',
        ],
    },

    install_requires=['flake8'],
    provides=['flake8_copyrighter'],
    py_modules=['flake8_copyrighter'],

)
