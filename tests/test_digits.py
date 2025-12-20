from unittest import TestCase
from irtools import num


class TestNum(TestCase):
    def test_english_to_farsi_no_option(self):
        self.assertEqual(num("0123456789"), "۰۱۲۳۴۵۶۷۸۹")
        self.assertEqual(num("agent 007"), "agent ۰۰۷")
        self.assertEqual(num("مامور 007"), "مامور ۰۰۷")
        self.assertEqual(num("dr460nized"), "dr۴۶۰nized")
        self.assertEqual(num("سل1م د9ست من"), "سل۱م د۹ست من")

    def test_english_to_farsi(self):
        self.assertEqual(num("0123456789", "ef"), "۰۱۲۳۴۵۶۷۸۹")
        self.assertEqual(num("agent 007", "ef"), "agent ۰۰۷")
        self.assertEqual(num("مامور 007", "ef"), "مامور ۰۰۷")
        self.assertEqual(num("dr460nized", "ef"), "dr۴۶۰nized")
        self.assertEqual(num("سل1م د9ست من", "ef"), "سل۱م د۹ست من")

    def test_farsi_to_english(self):
        self.assertEqual(num("۰۱۲۳۴۵۶۷۸۹", "fe"), "0123456789")
        self.assertEqual(num("agent ۰۰۷", "fe"), "agent 007")
        self.assertEqual(num("مامور ۰۰۷", "fe"), "مامور 007")
        self.assertEqual(num("dr۴۶۰nized", "fe"), "dr460nized")
        self.assertEqual(num("سل۱م د۹ست من", "fe"), "سل1م د9ست من")
