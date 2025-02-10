"""Unit-test suite for `python_docx.oxml.document` module."""

from __future__ import annotations

from typing import cast

from python_docx.oxml.document import CT_Body
from python_docx.oxml.table import CT_Tbl
from python_docx.oxml.text.paragraph import CT_P

from ..unitutil.cxml import element


class DescribeCT_Body:
    """Unit-test suite for selected units of `python_docx.oxml.document.CT_Body`."""

    def it_knows_its_inner_content_block_item_elements(self):
        body = cast(CT_Body, element("w:body/(w:tbl, w:p,w:p)"))
        assert [type(e) for e in body.inner_content_elements] == [CT_Tbl, CT_P, CT_P]
