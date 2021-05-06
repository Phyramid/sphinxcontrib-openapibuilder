"""
    sphinxcontrib.builders.openapi
    ~~~~~~~~~~~~~~~~~~~~

    OpenAPI builder for Sphinx.

    :copyright: Copyright 2012-2021 by Vlad-Stefan Harbuz, Ana-Maria-Adina Soare
    :license: BSD, see LICENSE.txt for details.
"""

from os import path
from typing import Any, Dict, Iterator, Set, Tuple

from docutils.io import StringOutput
from docutils.nodes import Node

from sphinx.application import Sphinx
from sphinx.builders import Builder
from sphinx.locale import __
from sphinx.util import logging
from sphinx.util.osutil import ensuredir, os_path
from ..writers.openapi import OpenAPITranslator, OpenAPIWriter

logger = logging.getLogger(__name__)


class OpenAPIBuilder(Builder):
    name = 'openapi'
    format = 'yaml'
    epilog = __('The OpenAPI files are in %(outdir)s.')

    out_suffix = '.yaml'
    allow_parallel = True
    default_translator_class = OpenAPITranslator

    current_docname = None  # type: str

    def init(self) -> None:
        # section numbers for headings in the currently visited document
        self.secnumbers = {}  # type: Dict[str, Tuple[int, ...]]

    def get_outdated_docs(self) -> Iterator[str]:
        for docname in self.env.found_docs:
            if docname not in self.env.all_docs:
                yield docname
                continue
            targetname = path.join(self.outdir, docname + self.out_suffix)
            try:
                targetmtime = path.getmtime(targetname)
            except Exception:
                targetmtime = 0
            try:
                srcmtime = path.getmtime(self.env.doc2path(docname))
                if srcmtime > targetmtime:
                    yield docname
            except OSError:
                # source doesn't exist anymore
                pass

    def get_target_uri(self, docname: str, typ: str = None) -> str:
        return ''

    def prepare_writing(self, docnames: Set[str]) -> None:
        self.writer = OpenAPIWriter(self)

    def write_doc(self, docname: str, doctree: Node) -> None:
        self.current_docname = docname
        self.secnumbers = self.env.toc_secnumbers.get(docname, {})
        destination = StringOutput(encoding='utf-8')
        self.writer.write(doctree, destination)
        outfilename = path.join(self.outdir, os_path(docname) + self.out_suffix)
        ensuredir(path.dirname(outfilename))
        try:
            with open(outfilename, 'w', encoding='utf-8') as f:
                f.write(self.writer.output)
        except OSError as err:
            logger.warning(__("error writing file %s: %s"), outfilename, err)

    def finish(self) -> None:
        pass


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_builder(OpenAPIBuilder)

    return {
        'version': 'builtin',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
