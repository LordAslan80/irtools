class Tel:
    _validate_type = ("v", "v0", "v9", "v+")
    _convert_type = ("c0", "c9", "c+")

    def __init__(self, value: str, option: str):
        self._value = value
        self._option = option

        if self._option in self._validate_type:
            self.run = self._validate(self._option)
        elif self._option in self._convert_type:
            self.run = self._convert()

    def _validate(self, type):
        if self._value[1:].isdigit():
            if (
                self._value.startswith("09")
                and len(self._value) == 11
                and type in ("v", "v0")
            ):
                return "0" if self._option in self._convert_type else True
            elif (
                self._value.startswith("989")
                and len(self._value) == 12
                and type in ("v", "v9")
            ):
                return "9" if self._option in self._convert_type else True
            elif (
                self._value.startswith("+989")
                and len(self._value) == 13
                and type in ("v", "v+")
            ):
                return "+" if self._option in self._convert_type else True
        return False

    def _convert(self):
        validation = self._validate("v")
        if validation:
            match self._option:
                case "c0":
                    return (
                        f"0{self._value[2:]}"
                        if validation == "9"
                        else (
                            f"0{self._value[3:]}" if validation == "+" else self._value
                        )
                    )
                case "c9":
                    return (
                        f"98{self._value[1:]}"
                        if validation == "0"
                        else self._value[1:] if validation == "+" else self._value
                    )
                case "c+":
                    return (
                        f"+98{self._value[1:]}"
                        if validation == "0"
                        else f"+{self._value}" if validation == "9" else self._value
                    )
                case _:
                    return False
        return False
