from unittest import TestCase
from irtools import national_code


class TestNationalCode(TestCase):
    def test_validation_no_option(self):
        self.assertEqual(national_code("7731689951"), False)
        self.assertEqual(national_code("7731689956"), True)

    def test_validation_v(self):
        self.assertEqual(national_code("7731689951", "v"), False)
        self.assertEqual(national_code("7731689956", "v"), True)

    def test_city_c(self):
        self.assertEqual(
            national_code("1080576290", "c"), "استان اصفهان - شهر نجف آباد"
        )
        self.assertEqual(
            national_code("1175411299", "c"), "استان اصفهان - شهر لنجان(زرینشهر)"
        )
