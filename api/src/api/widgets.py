# widgets.py
import uuid


def compose(f, g):
    return lambda x: f(g(x))


class Widget(object):
    '''The base Widget class'''

    def __init__(self):
        self.id = uuid.uuid1()
        self.algorithm = lambda ws: ws
        self._cache = None

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id})"

    def add_step(self, fn):
        self.algorithm = compose(fn, self.algorithm)

    def reset(self):
        self._cache = None

    def apply_to(self, ws):
        if self._cache is None:
            self._cache = self.algorithm(ws)
        return self._cache

    @property
    def data(self):
        return self._cache


class MetadataWidget(Widget):
    '''Shows metadata for a workset'''

    def __init__(self):
        super().__init__()

        self.add_step(lambda ws: ws.metadata)


class WidgetFactory:
    def __init__(self):
        self._widget_classes = {}

    @classmethod
    def make_widget(cls, widget_class: str):
        try:
            klass = globals()[widget_class]
            widget = klass()
            return widget
        except KeyError:
            print(f"Widget class {widget_class} not defined")
            raise KeyError()
