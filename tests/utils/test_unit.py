"""Utils test case"""

from unittest import TestCase

from core_curate_app.utils.validation import check_well_formed
from core_curate_app.common.exceptions import CurateValidationError


class TestCheckWellFormed(TestCase):
    """Test check_well_formed"""

    def test_check_well_formed_with_well_formed_xml(self):
        """test_check_well_formed_with_well_formed_xml

        Returns:

        """
        check_well_formed("<root></root>")

    def test_check_well_formed_with_not_well_formed_xml_raises_error(self):
        """test_check_well_formed_with_not_well_formed_xml_raises_error

        Returns:

        """
        with self.assertRaises(CurateValidationError):
            check_well_formed("<root>")

    def test_check_well_formed_with_well_formed_json(self):
        """test_check_well_formed_with_well_formed_json

        Returns:

        """
        check_well_formed('{"value": "test"}')

    def test_check_well_formed_with_not_well_formed_json_raises_error(self):
        """test_check_well_formed_with_not_well_formed_json_raises_error

        Returns:

        """
        with self.assertRaises(CurateValidationError):
            check_well_formed('{"value": "test"},')

    def test_check_well_formed_with_txt_file_raises_error(self):
        """test_check_well_formed_with_txt_file_raises_error

        Returns:

        """
        with self.assertRaises(CurateValidationError):
            check_well_formed("test")
