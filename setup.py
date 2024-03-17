#!/usr/bin/env python
import os
from setuptools import setup, find_packages

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='enhanced-cnab',
    version='0.0.9',
    description='Enhanced way to generate brazil banks CNAB files in python.',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Eduardo Oliveira',
    author_email='eduardo_y05@outlook.com',
    url='https://github.com/EduardoJM/enhanced-cnab',
    license='MIT',
    packages=find_packages(
        exclude = ("tests.*", "tests", )
    ),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    keywords='cnab,banks,boletos,remessa,lote,cnab240,cnab400',
)