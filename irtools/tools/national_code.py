class NationalCode:
    _get_types = ("pc", "c", "p")

    def __init__(self, value: str, option: str):
        self._value = value
        self._option = option

        if self._option == "v":
            self.run = self._validate()
        elif self._option in self._get_types:
            self.run = self._get_province_and_city()

    def _validate(self):
        if len(self._value) == 10 and self._value.isdigit():
            result = 0
            for index, item in enumerate(self._value[:9]):
                result += (10 - index) * int(item)

            result = result % 11

            if result < 2:
                return True if int(self._value[9]) == result else False
            else:
                return True if int(self._value[9]) == (11 - result) else False
        return False

    def _get_province_and_city(self):
        validation = self._validate()
        if validation:
            from .constant_datas import CITIES_LIST

            search = CITIES_LIST.get(self._value[:3])
            if search is not None:
                match self._option:
                    case "pc":
                        return f"استان {search['province']} ، شهر {search['city']}"
                    case "c":
                        return search["city"]
                    case "p":
                        return search["province"]
                    case _:
                        return False
            return False
        return False
