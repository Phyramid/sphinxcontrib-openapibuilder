"""
    sphinxcontrib.openapibuilder
    =========================

    Sphinx extension to output OpenAPI files.

    .. moduleauthor:: Vlad-Stefan Harbuz <vlad@vladh.net>, Ana-Maria-Adina Soare <ana-maria@phyramid.com>

    :copyright: Copyright 2012-2021 by Vlad-Stefan Harbuz, Ana-Maria-Adina Soare
    :license: BSD, see LICENSE.txt for details.
"""

__version__ = '0.1.0'
__author__ = 'Vlad-Stefan Harbuz <vlad@vladh.net>, Ana-Maria-Adina Soare <ana-maria@phyramid.com>'

def setup(app):
    # imports defined inside setup function, so that the __version__ can be loaded,
    # even if Sphinx is not yet installed.
    from .builders.openapi import OpenAPIBuilder

    app.require_sphinx('3.5')
    app.add_builder(OpenAPIBuilder)

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
