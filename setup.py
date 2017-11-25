#! /usr/bin/env python
# -*- coding: iso-8859-1 -*-

"""
Copyright (C) 2014-2017 Armin Straub, http://arminstraub.com
"""

"""
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.
"""

import sys
if not sys.version_info[0] == 3:
    sys.exit("Sorry, Python 2.x is not supported anymore")


# from distutils.core import setup
from setuptools import setup

# Automatically determine version from first line of ChangeLog file
import re
with open('ChangeLog') as f:
    s = f.readline()
    version = re.search('\((.*)\)', s).group(1)

# Update version in version.py
with open('krop/version.py', 'w') as f:
    f.write("__version__ = '%s'\n" % (version,))

# For reading long_description from README file (stolen from setup.py documentation)
import os
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
        name = 'krop',
        version = version,
        author = 'Armin Straub',
        author_email = 'mail@arminstraub.com',
        url = 'http://arminstraub.com/software/krop',
        description = 'A tool to crop PDF files',
        long_description = read('README.md'),
        keywords = 'pdf crop ereader',
        packages = ['krop'],
        scripts = ['bin/krop'],
        python_requires=">=3.3",
        classifiers = [
            'Development Status :: 3 - Beta',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Topic :: Utilities',
            'Intended Audience :: End Users/Desktop',
            'Programming Language :: Python :: 3',
            'Environment :: X11 Applications :: Qt',
        ],
)
