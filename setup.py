# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='mundipagg_one',
    version='2.0.0',
    url='https://github.com/dvl/mundipagg-one-python',
    license='Apache',
    author='André Luiz',
    author_email='contato@xdvl.info',
    description='Sdk for integration with mundipagg payment api',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Apache 2 License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',       
        'Programming Language :: Python :: 3.5',    
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
