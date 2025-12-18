class Numbers:
    _english_digits = "0123456789"
    _farsi_digits = "۰۱۲۳۴۵۶۷۸۹"

    _english_translation_table = str.maketrans(_farsi_digits, _english_digits)
    _farsi_translation_table = str.maketrans(_english_digits, _farsi_digits)

    def __init__(self, value: str, option: str):
        self._value = value
        self._option = option

        self.run = self._digit_converter()

    def _digit_converter(self):
        match self._option:
            case "ef":
                return self._value.translate(self._farsi_translation_table)
            case "fe":
                return self._value.translate(self._english_translation_table)
            case _:
                return False
