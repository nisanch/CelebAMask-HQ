#!/usr/bin/env python

from setuptools import find_packages, setup

requirements = []

setup(
    author="Lightricks research team",
    author_email="nisan@lightricks.com",
    python_requires=">=3.7",
    install_requires=requirements,
    url="https://github.com/LightricksResearch/",
    zip_safe=False,
    name="face_parsing",
    version="0.0.1",
    description="facial part seg",
    packages=find_packages(),
    include_package_data=True,
    package_data={"": ["weights/*.pth"]},
)

