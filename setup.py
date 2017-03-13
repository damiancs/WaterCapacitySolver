# coding=utf-8
"""
Setup script for this module.
"""

import os
from setuptools import setup


def read_license():
    """
    Read the licence.
    :return: The text of the MIT license.
     :rtype: str
    """
    license_text = "MIT License"
    try:
        with open(os.path.join(os.path.dirname(__file__), 'LICENSE')) as license_file:
            license_text = license_file.read()
    except IOError:
        pass
    return license_text


def read_description():
    """
    Read the description.
    :return: The text of the description.
     :rtype: str
    """
    description_text = ""
    try:
        with open(os.path.join(os.path.dirname(__file__), 'README.md')) as description_file:
            description_text = description_file.read()
    except IOError:
        pass
    return description_text


setup(
    name='WaterCapacitySolver',
    version='0.1',
    packages=["WaterCapacitySolver"],
    url='https://github.com/damiancs/WaterCapacitySolver',
    license=read_license(),
    author='Sebastian Damian',
    author_email='develop@damiancs.ro',
    description=read_description()
)
