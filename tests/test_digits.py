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

    def test_currency_words_less_than_10(self):
        self.assertEqual(digits("7", "cw"), "هفت")

    def test_currency_words_less_than_100(self):
        self.assertEqual(digits("70", "cw"), "هفتاد")
        self.assertEqual(digits("99", "cw"), "نود و نه")
        self.assertEqual(digits("15", "cw"), "پانزده")

    def test_currency_words_less_than_1000(self):
        self.assertEqual(digits("005", "cw"), "پنج")
        self.assertEqual(digits("300", "cw"), "سیصد")
        self.assertEqual(digits("370", "cw"), "سیصد و هفتاد")
        self.assertEqual(digits("372", "cw"), "سیصد و هفتاد و دو")
        self.assertEqual(digits("312", "cw"), "سیصد و دوازده")
        self.assertEqual(digits("905", "cw"), "نهصد و پنج")

    def test_currency_words_less_than_10000(self):
        self.assertEqual(digits("1000", "cw"), "یک هزار")
        self.assertEqual(digits("1300", "cw"), "یک هزار و سیصد")
        self.assertEqual(digits("5370", "cw"), "پنج هزار و سیصد و هفتاد")
        self.assertEqual(digits("2372", "cw"), "دو هزار و سیصد و هفتاد و دو")
        self.assertEqual(digits("7312", "cw"), "هفت هزار و سیصد و دوازده")
        self.assertEqual(digits("8003", "cw"), "هشت هزار و سه")

    def test_currency_words_less_than_100000(self):
        self.assertEqual(digits("13295", "cw"), "سیزده هزار و دویست و نود و پنج")
        self.assertEqual(digits("549817", "cw"), "پانصد و چهل و نه هزار و هشتصد و هفده")
        self.assertEqual(digits("900001", "cw"), "نهصد هزار و یک")

    def test_currency_words_less_than_1000000(self):
        self.assertEqual(digits("1000000", "cw"), "یک میلیون")
        self.assertEqual(digits("7002005", "cw"), "هفت میلیون و دو هزار و پنج")
