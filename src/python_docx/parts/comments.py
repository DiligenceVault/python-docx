"""|CommentsPart| and closely related objects."""

from typing import TYPE_CHECKING, cast

from python_docx.opc.constants import CONTENT_TYPE
from python_docx.opc.packuri import PackURI
from python_docx.oxml.parser import OxmlElement
from python_docx.opc.part import XmlPart
from python_docx.oxml.ns import nsmap

if TYPE_CHECKING:
    from python_docx.oxml.comments import (
        CT_Comments,
        CT_CommentsExtended,
    )
    from python_docx.package import Package


class CommentsPart(XmlPart):
    """Proxy for the comments.xml part containing comments definitions for a document
    or glossary."""

    @classmethod
    def new(cls, package: "Package"):
        """Return newly created empty comments part, containing only the root
        ``<w:comments>`` element."""
        partname = PackURI("/word/comments.xml")
        content_type = CONTENT_TYPE.WML_COMMENTS
        element = cast("CT_Comments", OxmlElement("w:comments", nsdecls=nsmap))
        return cls(partname, content_type, element, package)


class CommentsExtendedPart(XmlPart):
    """Proxy for the commentsExtended.xml part containing comments definitions for a document
    or glossary."""

    @classmethod
    def new(cls, package: "Package"):
        """Return newly created empty comments part, containing only the root
        ``<w15:commentsEx>`` element."""
        partname = PackURI("/word/commentsExtended.xml")
        content_type = CONTENT_TYPE.WML_COMMENTS_EXTENDED
        element = cast("CT_CommentsExtended", OxmlElement("w15:commentsEx"))
        return cls(partname, content_type, element, package)
