import unittest

from portfolio_drawdown_sentinel.models import Record
from portfolio_drawdown_sentinel.scoring import score_record


class DepthCheck2(unittest.TestCase):
    def test_002_operator_handoff(self):
        record = Record(id="position-002", exposure=4923, signal=0.254, urgency=6)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
