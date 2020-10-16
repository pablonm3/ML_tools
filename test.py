import unittest
from ML_tools import SlackNotifier
import os

TOKEN = os.environ['SLACK_BOT_TOKEN']

class MyTestCase(unittest.TestCase):
    def test_msg(self):
        SlackNotifier(TOKEN).message("testing baby")
    def test_error(self):
        try:
            smart = 1/0
        except Exception as e:
            SlackNotifier(TOKEN).error(e)


if __name__ == '__main__':
    unittest.main()
