"""Initialize `docx` package.

Export the `Document` constructor function and establish the mapping of part-type to
the part-classe that implements that type.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Type

from python_docx.api import Document
from python_docx.parts.comments import CommentsExtendedPart, CommentsPart

if TYPE_CHECKING:
    from python_docx.opc.part import Part

__version__ = "1.1.2"


__all__ = ["Document"]


# -- register custom Part classes with opc package reader --

from python_docx.opc.constants import CONTENT_TYPE as CT
from python_docx.opc.constants import RELATIONSHIP_TYPE as RT
from python_docx.opc.part import PartFactory
from python_docx.opc.parts.coreprops import CorePropertiesPart
from python_docx.parts.document import DocumentPart
from python_docx.parts.hdrftr import FooterPart, HeaderPart
from python_docx.parts.image import ImagePart
from python_docx.parts.numbering import NumberingPart
from python_docx.parts.settings import SettingsPart
from python_docx.parts.styles import StylesPart


def part_class_selector(content_type: str, reltype: str) -> Type[Part] | None:
    if reltype == RT.IMAGE:
        return ImagePart
    return None


PartFactory.part_class_selector = part_class_selector
PartFactory.part_type_for[CT.OPC_CORE_PROPERTIES] = CorePropertiesPart
PartFactory.part_type_for[CT.WML_DOCUMENT_MAIN] = DocumentPart
PartFactory.part_type_for[CT.WML_FOOTER] = FooterPart
PartFactory.part_type_for[CT.WML_HEADER] = HeaderPart
PartFactory.part_type_for[CT.WML_NUMBERING] = NumberingPart
PartFactory.part_type_for[CT.WML_SETTINGS] = SettingsPart
PartFactory.part_type_for[CT.WML_STYLES] = StylesPart
PartFactory.part_type_for[CT.WML_COMMENTS] = CommentsPart
PartFactory.part_type_for[CT.WML_COMMENTS_EXTENDED] = CommentsExtendedPart

del (
    CT,
    CorePropertiesPart,
    DocumentPart,
    FooterPart,
    HeaderPart,
    NumberingPart,
    PartFactory,
    SettingsPart,
    StylesPart,
    CommentsPart,
    CommentsExtendedPart,
    part_class_selector,
)
