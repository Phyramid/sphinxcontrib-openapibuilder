"""
    sphinxcontrib.writers.openapi
    ~~~~~~~~~~~~~~~~~~~

    OpenAPI writer for Sphinx.

    :copyright: Copyright 2012-2021 by Vlad-Stefan Harbuz, Ana-Maria-Adina Soare
    :license: BSD, see LICENSE.txt for details.
"""
import math
import os
import re
from typing import cast

from docutils import nodes, writers
from docutils.nodes import Element, Node, Text

from sphinx.util.docutils import SphinxTranslator

if False:
    # For type annotation
    from sphinx.builders.text import OpenAPIBuilder


class OpenAPIWriter(writers.Writer):
    supported = ('text',)
    settings_spec = ('No options here.', '', ())
    settings_defaults = {}

    output = None  # type: str

    def __init__(self, builder: "OpenAPIBuilder") -> None:
        super().__init__()
        self.builder = builder

    def translate(self) -> None:
        visitor = self.builder.create_translator(self.document, self.builder)
        self.document.walkabout(visitor)
        self.output = cast(OpenAPITranslator, visitor).body


class OpenAPITranslator(SphinxTranslator):
    builder = None  # type: OpenAPIBuilder

    def __init__(self, document: nodes.document, builder: "OpenAPIBuilder") -> None:
        super().__init__(document, builder)

        newlines = self.config.text_newlines
        if newlines == 'windows':
            self.nl = '\r\n'
        elif newlines == 'native':
            self.nl = os.linesep
        else:
            self.nl = '\n'
        self.body = ''

    def visit_document(self, node: Element) -> None:
        self.body += 'hello'

    def depart_document(self, node: Element) -> None:
        self.body += 'goodbye'

    def unknown_visit(self, node: Node) -> None:
        print('Unknown visit: ' + node.__class__.__name__)
        # raise NotImplementedError('Unknown node: ' + node.__class__.__name__)
    def unknown_departure(self, node: Node) -> None:
        print('Unknown departure: ' + node.__class__.__name__)
        # raise NotImplementedError('Unknown node: ' + node.__class__.__name__)
