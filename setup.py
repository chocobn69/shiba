#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# setup.py setup script

from setuptools import setup

setup(name="Shiba",
      packages=["shiba"],
      version="1.1.5-dev",
      description="A Python API for PriceMinister WebServices",
      author="Maxime Boguta",
      author_email="maxime.boguta@epitech.eu",
      url="https://github.com/ShibaAPI/shiba",
      download_url="https://github.com/Phylante/shiba/tarball/1.1.5-dev",
      keywords=["api", "priceminister", "python", "webservices"],
      install_requires=["requests", "xmltodict", "lxml", "nose"],)
