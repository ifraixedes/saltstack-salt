"""
    :codeauthor: Jayesh Kariya <jayeshk@saltstack.com>
"""

import salt.states.layman as layman
from tests.support.mixins import LoaderModuleMockMixin
from tests.support.mock import MagicMock, patch
from tests.support.unit import TestCase


class LaymanTestCase(TestCase, LoaderModuleMockMixin):
    """
    Test cases for salt.states.layman
    """

    def setup_loader_modules(self):
        return {layman: {}}

    # 'present' function tests: 1

    def test_present(self):
        """
        Test to verify that the overlay is present.
        """
        name = "sunrise"

        ret = {"name": name, "result": True, "comment": "", "changes": {}}

        mock = MagicMock(side_effect=[[name], []])
        with patch.dict(layman.__salt__, {"layman.list_local": mock}):
            comt = "Overlay {} already present".format(name)
            ret.update({"comment": comt})
            self.assertDictEqual(layman.present(name), ret)

            with patch.dict(layman.__opts__, {"test": True}):
                comt = "Overlay {} is set to be added".format(name)
                ret.update({"comment": comt, "result": None})
                self.assertDictEqual(layman.present(name), ret)

    # 'absent' function tests: 1

    def test_absent(self):
        """
        Test to verify that the overlay is absent.
        """
        name = "sunrise"

        ret = {"name": name, "result": True, "comment": "", "changes": {}}

        mock = MagicMock(side_effect=[[], [name]])
        with patch.dict(layman.__salt__, {"layman.list_local": mock}):
            comt = "Overlay {} already absent".format(name)
            ret.update({"comment": comt})
            self.assertDictEqual(layman.absent(name), ret)

            with patch.dict(layman.__opts__, {"test": True}):
                comt = "Overlay {} is set to be deleted".format(name)
                ret.update({"comment": comt, "result": None})
                self.assertDictEqual(layman.absent(name), ret)
