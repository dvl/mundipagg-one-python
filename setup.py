# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='mundipagg_one_python',
    version='2.0.0',
    url='https://github.com/mundipagg/mundipagg-one-python',
    license='Apache',
    author='Newton Rocha',
    author_email='nrocha@mundipagg.com',
    description='Sdk for integration with mundipagg payment api',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Apache 2 License',
        'Programming Language :: Python :: 2.7'
        'Programming Language :: Python :: 3.5'
        'Topic :: Gateway Integration :: SDK',
    ],
    install_requires=[
        'requests>=2.0.0',
        'enum34>=1.0.0',
        'xmltodict>=0.9.2'
    ],
    keywords=[
        'mundipagg',
        'rest',
        'sdk',
        'payments',
    ]
)
