"""
A normal setup.py module.
"""
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='NanStats',
    version='1.0.0',
    description='A Python adapter for the Nanigans Reporting API.',
    long_description=long_description,
    url='https://github.com/unique-influence-tech/nanigans-reporting-api',
    author='Sean Kennedy',
    author_email='',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers/Analysts',
        'Topic :: Advertising :: Data Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='advertising, facebook, data',
    packages=['nanigans', 'nanigans.api','nanigans.tests'],
    install_requires=['requests','mock'],
)
