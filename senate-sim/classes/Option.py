import logging


class Option:
    options = [True, False, None]

    def __init__(self, value=0, conviction=0):
        if value in self.options:
            if value in self.options:
                self.value = value
                self.conviction = conviction