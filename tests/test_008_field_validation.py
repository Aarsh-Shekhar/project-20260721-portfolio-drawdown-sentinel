import unittest

from portfolio_drawdown_sentinel.models import Record
from portfolio_drawdown_sentinel.scoring import score_record


class DepthCheck8(unittest.TestCase):
    def test_008_field_validation(self):
        record = Record(id="position-008", exposure=84289, signal=0.327, urgency=5)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
