from unittest import TestCase
from irtools import digits


class Testdigits(TestCase):
    def test_english_to_farsi_no_option(self):
        self.assertEqual(digits("0123456789"), "۰۱۲۳۴۵۶۷۸۹")
        self.assertEqual(digits("agent 007"), "agent ۰۰۷")
        self.assertEqual(digits("مامور 007"), "مامور ۰۰۷")
        self.assertEqual(digits("dr460nized"), "dr۴۶۰nized")
        self.assertEqual(digits("سل1م د9ست من"), "سل۱م د۹ست من")

    def test_english_to_farsi(self):
        self.assertEqual(digits("0123456789", "ef"), "۰۱۲۳۴۵۶۷۸۹")
        self.assertEqual(digits("agent 007", "ef"), "agent ۰۰۷")
        self.assertEqual(digits("مامور 007", "ef"), "مامور ۰۰۷")
        self.assertEqual(digits("dr460nized", "ef"), "dr۴۶۰nized")
        self.assertEqual(digits("سل1م د9ست من", "ef"), "سل۱م د۹ست من")

    def test_farsi_to_english(self):
        self.assertEqual(digits("۰۱۲۳۴۵۶۷۸۹", "fe"), "0123456789")
        self.assertEqual(digits("agent ۰۰۷", "fe"), "agent 007")
        self.assertEqual(digits("مامور ۰۰۷", "fe"), "مامور 007")
        self.assertEqual(digits("dr۴۶۰nized", "fe"), "dr460nized")
        self.assertEqual(digits("سل۱م د۹ست من", "fe"), "سل1م د9ست من")
