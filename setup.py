import os
from setuptools import setup, find_packages


def get_install_requires():
    with open('requirements.txt', 'r') as requirements_file:
        res = requirements_file.readlines()
        return [req.split(' ', maxsplit=1)[0] for req in res if req]


def get_version():
    with open(os.path.join('amun', '__init__.py')) as f:
        content = f.readlines()

    for line in content:
        if line.startswith('__version__ ='):
            # dirty, remove trailing and leading chars
            return line.split(' = ')[1][1:-2]
    raise ValueError("No version identifier found")


setup(
    name='amun',
    entry_points={
        'console_scripts': ['amun=amun.cli:cli']
    },
    version=get_version(),
    description='A CLI tool and library for interacting with Amun',
    long_description='A CLI tool and library for interacting with Amun',
    author='Fridolin Pokorny',
    author_email='fridolin@redhat.com',
    license='GPLv3+',
    packages=find_packages(),
    install_requires=get_install_requires()
)
