import uuid


class Dashboard:
    def __init__(self):
        self._id = uuid.uuid1()
        self._widgets = {}
        self._workset = None

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id})"

    @property
    def id(self):
        return str(self._id)

    @property
    def widgets(self):
        return self._widgets

    def add_widget(self, widget):
        widget.workset = self.workset
        self.widgets[str(widget.id)] = widget
        return self.widgets

    def get_widget(self, widget_id):
        return self.widgets[widget_id]

    def delete_widget(self, widget_id):
        del self.widgets[widget_id]
        return self.widgets

    @property
    def workset(self):
        return self._workset

    @workset.setter
    def workset(self, workset):
        self._workset = workset
