#!/usr/bin/env python
# -*- coding: utf-8 -*

import sys
import os.path
from setuptools import find_packages, setup

try:
    import subprocess
    if os.path.exists(os.path.join(os.path.dirname(__file__), '.git')):
        git_ver = subprocess.check_output(['git', 'describe', '--tags',
                                           '--match', r'v[0-9]*\.[0-9]*'])
        git_ver = git_ver.decode()
        version = git_ver[1:].strip().split('-', 2)[0]
    else:
        version = '0.0.1'
except Exception as e:
    print("Could not get version: %s" % e)
    version = '0.0.1'

setup(
    name='pyhpy',
    version=version,
    description="Micro-framework for dynamic HTTP endpoints",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Panos Christeas",
    author_email="xrg@pefnos.com",
    url="http://github.com/xrg/pyhpy",
    provides = ["pyhpy"],
    #packages = ["pyhpy"],
    entry_points={
        'console_scripts': [
            ]
    },
    install_requires=[
        "werkzeug",
        "jinja2"
    ],
    cmdclass = {
    },
    extras_require={
        'develop': [
        ],
    },
    license="BSD-2-Clause",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: BSD License",
    ],
    zip_safe = True,
)


# eof
