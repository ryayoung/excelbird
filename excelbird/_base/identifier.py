from excelbird._layout_references import Globals

class HasId:
    """
    Has an id property which, when set, inserts a reference to
    self in `Globals.ids`.
    """

    @property
    def id(self):
        if not hasattr(self, "_id"):
            self._id = None
        return self._id

    @id.setter
    def id(self, new):
        self._set_id(new)

    def _set_id(self, new):
        if new is not None:
            if not isinstance(new, str):
                raise ValueError(f"Invalid id, `{new}`. Ids must be strings.")
            Globals.ids[new] = self
            if new.startswith("G::"):
                Globals.global_ids[new] = self
        self._id = new
        return self


class HasHeader:
    """
    Has an header property which, when set, inserts a reference to
    self in `Globals.headers`.
    """

    @property
    def header(self):
        if not hasattr(self, "_header"):
            self._header = None
        return self._header

    @header.setter
    def header(self, new):
        self._set_header(new)

    def _set_header(self, new):
        if new is not None:
            if not isinstance(new, str):
                raise ValueError(f"Invalid header, `{new}`. Headers must be strings.")
            Globals.headers[new] = self
            if new.startswith("G::"):
                Globals.global_headers[new] = self
        self._header = new
        return self
