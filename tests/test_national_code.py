from unittest import TestCase
from irtools import national_code


class TestNationalCode(TestCase):
    def test_validation_v(self):
        self.assertEqual(national_code("7731689951", "v"), False)
        self.assertEqual(national_code("7731689956", "v"), True)

    def test_city_c(self):
        self.assertEqual(
            national_code("1080576290", "c"), "استان اصفهان ، شهر نجف آباد"
        )
        self.assertEqual(
            national_code("1175411299", "c"), "استان اصفهان ، شهر لنجان(زرینشهر)"
        )

    def test_city_cc(self):
        self.assertEqual(national_code("1080576290", "cc"), "نجف آباد")
        self.assertEqual(national_code("1175411299", "cc"), "لنجان(زرینشهر)")

    def test_city_cp(self):
        self.assertEqual(national_code("1080576290", "cp"), "اصفهان")
        self.assertEqual(national_code("1175411299", "cp"), "اصفهان")
