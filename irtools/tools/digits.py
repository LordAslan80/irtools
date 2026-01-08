from .constant_datas import NUM_WORDS, FARSI_DIGITS, ENGLISH_DIGITS


class Digits:
    _english_translation_table = str.maketrans(FARSI_DIGITS, ENGLISH_DIGITS)
    _farsi_translation_table = str.maketrans(ENGLISH_DIGITS, FARSI_DIGITS)

    def __init__(self, value: str, option: str):
        self._value = value
        self._option = option

        if self._option == "cw":
            self.run = self._currency()
        else:
            self.run = self._digit_converter()

    def _digit_converter(self):
        match self._option:
            case "ef":
                return self._value.translate(self._farsi_translation_table)
            case "fe":
                return self._value.translate(self._english_translation_table)
            case _:
                return False

    def _currency(self):
        self._option = "fe"
        data = self._digit_converter()
        output = []

        if data:
            data = [data[::-1][i : i + 3][::-1] for i in range(0, len(data), 3)]

            for index, item in enumerate(data):
                if item != "000":
                    result = self._words(item)
                    output.append(f"{result}{NUM_WORDS["UNITS"][index]}")

            return " و ".join(reversed(output))
        return False

    def _words(self, value):
        match len(value):
            case 1:
                return NUM_WORDS["NUMS"].get(value)[0]
            case 2:
                if value[1] == "0":
                    return NUM_WORDS["NUMS"].get(value[0])[2]
                elif value[0] == "1":
                    return NUM_WORDS["NUMS"].get(value[1])[1]
                else:
                    return f"{NUM_WORDS["NUMS"].get(value[0])[2]} و {NUM_WORDS["NUMS"].get(value[1])[0]}"
            case 3:
                if value[2] == "0" and value[1] == "0":
                    return NUM_WORDS["NUMS"].get(value[0])[3]
                elif value[0] == "0" and value[1] == "0":
                    return NUM_WORDS["NUMS"].get(value[2])[0]
                elif value[1] == "0":
                    return f"{NUM_WORDS["NUMS"].get(value[0])[3]} و {NUM_WORDS["NUMS"].get(value[2])[0]}"
                elif value[2] == "0":
                    return f"{NUM_WORDS["NUMS"].get(value[0])[3]} و {NUM_WORDS["NUMS"].get(value[1])[2]}"
                elif value[1] == "1":
                    return f"{NUM_WORDS["NUMS"].get(value[0])[3]} و {NUM_WORDS["NUMS"].get(value[2])[1]}"
                else:
                    return f"{NUM_WORDS["NUMS"].get(value[0])[3]} و {NUM_WORDS["NUMS"].get(value[1])[2]} و {NUM_WORDS["NUMS"].get(value[2])[0]}"
            case _:
                return False
