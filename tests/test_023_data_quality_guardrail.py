import unittest

from portfolio_drawdown_sentinel.models import Record
from portfolio_drawdown_sentinel.scoring import score_record


class DepthCheck23(unittest.TestCase):
    def test_023_data_quality_guardrail(self):
        record = Record(id="position-023", exposure=69204, signal=0.710, urgency=9)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
