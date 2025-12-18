class Numbers:
    _english_digits = "0123456789"
    _farsi_digits = "۰۱۲۳۴۵۶۷۸۹"

    _english_translation_table = str.maketrans(_farsi_digits, _english_digits)
    _farsi_translation_table = str.maketrans(_english_digits, _farsi_digits)

    def __init__(self, value: str, option: str):
        self._value = value
        self._option = option

        if self._option == "ef":
            self.run = self._convert_english_digit_to_farsi_digit()
        elif self._option == "fe":
            self.run = self._convert_farsi_digit_to_english_digit()

    def _convert_english_digit_to_farsi_digit(self):
        return self._value.translate(self._farsi_translation_table)

    def _convert_farsi_digit_to_english_digit(self):
        return self._value.translate(self._english_translation_table)
