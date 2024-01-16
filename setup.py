# Комментарий от пользователя taharkham

#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='pycipher',
    version='0.5.1',
    description='Several simple cipher algorithms',
    author='James Lyons',
    author_email='james.lyons0@gmail.com',

    packages=find_packages(exclude=['tests','tests.*']),
    include_package_data=True,  # declarations in MANIFEST.in
    url='https://github.com/jameslyons/pycipher',
    test_suite='tests',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    long_description=open('README.rst', 'rt').read()
)
