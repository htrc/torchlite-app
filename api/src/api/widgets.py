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

    @property
    def workset(self):
        return self._workset

    @workset.setter
    def workset(self, ws):
        self._workset = ws


class MetadataWidget(Widget):
    @property
    def data(self):
        if self._data is None:
            self._data = self.workset.metadata
        return self._data


class WidgetFactory:
    def __init__(self):
        self._widget_classes = {}

    def make_widget(widget_class: str, workset):
        try:
            klass = globals()[widget_class]
            widget = klass(workset)
            return widget
        except KeyError:
            print(f"Widget class {widget_class} not defined")
            raise KeyError()
