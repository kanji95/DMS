# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Edgar Andrés Margffoy-Tuay, Emilio Botero and Juan Camilo Pérez
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""Setup script for LangVisNet."""

# Standard library imports
import ast
import os
import sys
import shutil
import os.path as osp

# Third party imports
from setuptools import setup, find_packages

PACKAGE = 'langvisnet'
HERE = os.path.abspath(os.path.dirname(__file__))


def get_version(module=PACKAGE):
    """Get version."""
    with open(os.path.join(HERE, module, '__init__.py'), 'r') as f:
        data = f.read()
    lines = data.split('\n')
    for line in lines:
        if line.startswith('VERSION_INFO'):
            version_tuple = ast.literal_eval(line.split('=')[-1].strip())
            version = '.'.join(map(str, version_tuple))
            break
    return version


def get_description():
    """Get long description."""
    with open(os.path.join(HERE, 'README.md'), 'r') as f:
        data = f.read()
    return data


REQUIREMENTS = ['pytorch', 'sru', 'torchvision']

os.rename('models', PACKAGE)
shutil.copy('referit_loader.py', PACKAGE)
shutil.copytree('utils', osp.join(PACKAGE, 'utils'))
os.rename(
    osp.join(PACKAGE, "__init__.py"), osp.join(PACKAGE, "__init__.py.bak"))

lines = ''
with open(osp.join(PACKAGE, "__init__.py.bak"), 'r') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]

lines.append('from .referit_loader import ReferDataset')
lines = '\n'.join(lines)
with open(osp.join(PACKAGE, "__init__.py"), 'w') as f:
    f.write(lines)

with open(osp.join(PACKAGE, 'referit_loader.py'), 'r') as f:
    text = f.read()

text = text.replace('from utils import Corpus',
                    'from {0}.utils import Corpus'.format(PACKAGE))

with open(osp.join(PACKAGE, 'referit_loader.py'), 'w') as f:
    f.write(text)

try:
    setup(
        name=PACKAGE,
        version=get_version(),
        keywords=['Compputer Vision', 'Segmentation', 'NLP'],
        url='https://github.com/andfoy/query-objseg',
        license='MIT',
        author='Edgar Andrés Margffoy Tuay',
        author_email='andfoy@gmail.com',
        description='Semantic Segmentation based on Natural Language Queries',
        long_description=get_description(),
        packages=find_packages(exclude=['utils', 'contrib', 'docs', 'tests*']),
        install_requires=REQUIREMENTS,
        include_package_data=True,
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Operating System :: MacOS',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6'])
finally:
    shutil.rmtree(osp.join(PACKAGE, 'utils'))
    os.remove(osp.join(PACKAGE, 'referit_loader.py'))
    os.remove(osp.join(PACKAGE, '__init__.py'))
    os.rename(
        osp.join(PACKAGE, '__init__.py.bak'), osp.join(PACKAGE, '__init__.py'))
    os.rename(PACKAGE, 'models')
