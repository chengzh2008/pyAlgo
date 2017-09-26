# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pyAlgo',
    version='0.1.0',
    description='Algorithm through Python',
    long_description=readme,
    author='Your Name',
    author_email='your@email.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
