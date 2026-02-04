# Utils for issue #3

class Handler3:
    def __init__(self, data=None):
        self.data = data or {}
        self._validate()

    def _validate(self):
        if not self.data:
            raise ValueError("No data provided")

    def process(self):
        # Processing logic for issue #3
        return list(self.data.keys())
