import pdb
import unittest
from unittest.mock import patch
from webrecon import gcse, constants

class TestGCSE(unittest.TestCase):
    # @patch('webrecon.gcse_api_factory.requests.get')
    def test__ff_flattens(self): # , mock_get):
        """Test that _ff flattens the results it sends back"""
        doc = {"things0": {"things1": "stuff1"}, "and": "stuff0"}
        # mock_get.return_value.ok = True
        pdb.set_trace()
        result = gcse._ff(doc, "things1")

        self.assertIn("things1", result)

if __name__ == '__main__':
    unittest.main()
