class ValidationComment:

    def __init__(self, field_name, comment):
        self._field_name = field_name
        self._comment = comment

    @property
    def field_name(self):
        return self._field_name

    @property
    def comment(self):
        return self._comment
