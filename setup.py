# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
Sphinx extension to build and write OpenAPI files.
'''

requires = ['Sphinx>=3.5', 'docutils']

setup(
    name='sphinxcontrib-openapibuilder',
    version='0.1.0',
    url='https://github.com/phyramid/sphinxcontrib-openapibuilder',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-openapibuilder',
    license='BSD 2-Clause',
    author='Vlad-Stefan Harbuz',
    author_email='vlad@vladh.net',
    description='Sphinx extension to output OpenAPI files.',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation',
    ],
    platforms='any',
    python_requires='>=3.5',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
