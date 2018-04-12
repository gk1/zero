# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='zero',
    version='0.0.1',
    description="Unlimited local storage",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='',
    author='Konstantin Schubert',
    packages=find_packages(),
    install_requires=[
        'fusepy',
    ],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'console_scripts': ['zero = zero.main:main',],
    }
)