# widgets.py
import uuid
from api.extracted_features import WorkSet


class Widget:
    def __init__(self, workset):
        self.id = uuid.uuid1()
        self._workset = workset
        self._data = None

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id})"

    # Override in subclasses
    @property
    def data(self):
        return []


class MetadataWidget(Widget):
    @property
    def data(self):
        if self._data is None:
            self._data = self._workset.volumes
        return self._data
