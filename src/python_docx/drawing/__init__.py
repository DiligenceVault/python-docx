"""DrawingML-related objects are in this subpackage."""

from __future__ import annotations

from typing import TYPE_CHECKING

from python_docx.oxml.drawing import CT_Drawing
from python_docx.shared import Parented

if TYPE_CHECKING:
    import python_docx.types as t


class Drawing(Parented):
    """Container for a DrawingML object."""

    def __init__(self, drawing: CT_Drawing, parent: t.ProvidesStoryPart):
        super().__init__(parent)
        self._parent = parent
        self._drawing = self._element = drawing
