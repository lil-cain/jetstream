#!/usr/bin/env python
'''Python setup.py'''

import ast
import re
from setuptools import setup, find_packages

DEPENDENCIES = [
    'troposphere==1.9.0',
    'boto3==1.4.1',
    'awacs',
]

STYLE_REQUIRES = [
    'flak8>=2.5.4',
    'pylint>=1.5.5',
]

TESTS_REQUIRE = []


def package_meta():
    """Read __init__.py for global package metadata.
    Do this without importing the package.
    """
    _version_re = re.compile(r'__version__\s+=\s+(.*)')
    _url_re = re.compile(r'__url__\s+=\s+(.*)')
    _license_re = re.compile(r'__license__\s+=\s+(.*)')

    with open('jetstream/__init__.py', 'rb') as ffinit:
        initcontent = ffinit.read()
        version = str(ast.literal_eval(_version_re.search(
            initcontent.decode('utf-8')).group(1)))
        url = str(ast.literal_eval(_url_re.search(
            initcontent.decode('utf-8')).group(1)))
        licencia = str(ast.literal_eval(_license_re.search(
            initcontent.decode('utf-8')).group(1)))
    return {
        'version': version,
        'license': licencia,
        'url': url,
    }

_lu_meta = package_meta()

setup(
    name='jetstream',
    description='',
    keywords='',
    version=_lu_meta['version'],
    tests_require=TESTS_REQUIRE + STYLE_REQUIRES,
    install_requires=DEPENDENCIES,
    packages=find_packages(exclude=['tests']),
    classifiers=[
        "Programming Language :: Python :: 2.7",
    ],
    license=_lu_meta['license'],
    author="Rackers",
    maintainer_email="fps@rackspace.com",
    url=_lu_meta['url'],
    entry_points={
        'console_scripts': [
            'jetstream=jetstream.cli:main'
        ]
    },
)
