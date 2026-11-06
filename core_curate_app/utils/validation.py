"""Curate validation utils"""

from lxml import etree
import json
from core_curate_app.common.exceptions import CurateValidationError


def check_well_formed(value):
    """Check that the value is either well-formed XML or well-formed JSON."""

    if not value:
        return value

    # Check if well-formed JSON
    try:
        json.loads(value)
        return value
    except (ValueError, TypeError):
        pass

    # Check if well-formed XML
    try:
        etree.fromstring(value.encode("utf-8"))
        return value
    except etree.XMLSyntaxError:
        pass

    raise CurateValidationError("The document is not well-formed.")
