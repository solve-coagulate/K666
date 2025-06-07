#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="k666",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Django>=3.2",
        "django-allauth",
        "django-messages",
    ],
    python_requires=">=3.8",
)
