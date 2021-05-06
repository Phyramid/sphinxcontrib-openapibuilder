.. -*- restructuredtext -*-

=================================
README for Sphinx OpenAPI Builder
=================================

This is a Sphinx extension to build and write OpenAPI files.

It's meant to be used together with `autohttp` from `sphinxcontrib.httpdomain`.

Requirements
============

* Sphinx 3.5
* Python 3.5

Installing
==========

Using pip
---------

::

    pip install sphinxcontrib-openapibuilder

Manual
------

::

    git clone https://github.com/phyramid/sphinxcontrib-openapibuilder.git
    cd sphinxcontrib-openapibuilder
    python setup.py install

Usage
=====

- Set the builder as a extension in ``conf.py``::

    extensions = ['sphinxcontrib.openapibuilder']

- Run sphinx-build with target ``openapi``::

    sphinx-build -b openapi -c . build/openapi

Configuration
=============

There are no configuration options yet, but adding an option to indicate
whether to output YAML or JSON would probably be a good idea.

Acknowledgements
================

Built at Phyramid by:

* Vlad-Stefan Harbuz <vlad@vladh.net>
* Ana-Maria-Adina Soare <ana-maria@phyramid.com>

Partly based on builder and writer code by the Sphinx contributors.
