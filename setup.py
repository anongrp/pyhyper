# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pyhyper',
    version='0.1.0',
    description='driver for hyperlite database',
    long_description=readme,
    author= "Anongrp"
    author_email='anongrpindia@gmail.com',
    url='https://github.com/Anongrp/pyhyper',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

