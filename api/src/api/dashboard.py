import uuid


class Dashboard:
    def __init__(self):
        self._id = uuid.uuid1()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id})"

    @property
    def id(self):
        return str(self._id)
