import sys
from unittest import TestCase
try:
    from unittest import mock
except ImportError:
    from mock import mock
sys.modules['helga.plugins'] = mock.Mock()

from helga_roll.plugin import roll_dice


class TestResults(TestCase):
    def test_roll(self):
        with mock.patch('helga_roll.plugin.random.randint', TestResults.random_int):
            self.assertEqual('7 = 7', roll_dice())
            self.assertEqual('7 + 7 = 14', roll_dice(count=2))
            self.assertEqual('7 + 7 + 1 = 15', roll_dice(count=2, modifier=1))

    @classmethod
    def random_int(cls, *args, **kwargs):
        return 7
