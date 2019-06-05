#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name = "Gandharvas",
    version = "1.0",
    author = "Joachim Etienne",
    author_email = "joachim.etienne@yahoo.fr",
    description = ("Musical Player"),
    license = "GPL-3.0",
    long_description = open("README.md").read(),
    download_url = "https://github.com/J04CH/Gandharvas",
    install_requires = open("requirements.txt").read(),
    python_requires = ">=3.7",
    packages = find_packages(),
)
