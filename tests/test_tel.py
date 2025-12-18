from unittest import TestCase
from irtools import tel


class TestTel(TestCase):
    def test_validate_type_v(self):
        self.assertEqual(tel("09135689472"), True)
        self.assertEqual(tel("989135689472"), True)
        self.assertEqual(tel("+989135689472"), True)
        self.assertEqual(tel("091356894721"), False)
        self.assertEqual(tel("9891356894721"), False)
        self.assertEqual(tel("+9891356894721"), False)

    def test_validate_type_v_zero(self):
        self.assertEqual(tel("09135689472", "v0"), True)
        self.assertEqual(tel("989135689472", "v0"), False)
        self.assertEqual(tel("+989135689472", "v0"), False)
        self.assertEqual(tel("091356894721", "v0"), False)
        self.assertEqual(tel("0913568947", "v0"), False)

    def test_validate_type_v_nine(self):
        self.assertEqual(tel("989135689472", "v9"), True)
        self.assertEqual(tel("09135689472", "v9"), False)
        self.assertEqual(tel("+989135689472", "v9"), False)
        self.assertEqual(tel("9891356894721", "v9"), False)
        self.assertEqual(tel("98913568947", "v9"), False)

    def test_validate_type_v_plus(self):
        self.assertEqual(tel("+989135689472", "v+"), True)
        self.assertEqual(tel("09135689472", "v+"), False)
        self.assertEqual(tel("989135689472", "v+"), False)
        self.assertEqual(tel("+9891356894721"), False)
        self.assertEqual(tel("+98913568947"), False)

    def test_convert_type_c_zero(self):
        self.assertEqual(tel("09135689472", "c0"), "09135689472")
        self.assertEqual(tel("989135689472", "c0"), "09135689472")
        self.assertEqual(tel("+989135689472", "c0"), "09135689472")

    def test_convert_type_c_nine(self):
        self.assertEqual(tel("09135689472", "c9"), "989135689472")
        self.assertEqual(tel("989135689472", "c9"), "989135689472")
        self.assertEqual(tel("+989135689472", "c9"), "989135689472")

    def test_convert_type_c_plus(self):
        self.assertEqual(tel("09135689472", "c+"), "+989135689472")
        self.assertEqual(tel("989135689472", "c+"), "+989135689472")
        self.assertEqual(tel("+989135689472", "c+"), "+989135689472")
