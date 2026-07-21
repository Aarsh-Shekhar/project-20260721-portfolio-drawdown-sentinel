import unittest

from portfolio_drawdown_sentinel.models import Record
from portfolio_drawdown_sentinel.scoring import score_record


class DepthCheck14(unittest.TestCase):
    def test_014_scenario_analysis(self):
        record = Record(id="position-014", exposure=35171, signal=0.318, urgency=4)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
