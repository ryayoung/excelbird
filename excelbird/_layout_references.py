class Globals:
    ids = dict()
    headers = dict()
    global_ids = dict()
    global_headers = dict()
    force_valid_references = True
    expression_sign_spacing = 2

    @classmethod
    def clear_references(cls, sheet_title: str | None = None) -> None:
        if sheet_title is None:
            cls.ids = dict()
            cls.headers = dict()
            return

        ids_to_pop = []
        headers_to_pop = []

        for id, elem in cls.ids.items():
            if hasattr(elem, "loc"):
                if elem._loc is not None:
                    if elem._loc.ws.title == sheet_title:
                        ids_to_pop.append(id)

        for header, elem in cls.headers.items():
            if hasattr(elem, "_loc"):
                if elem._loc is not None:
                    if elem._loc.ws.title == sheet_title:
                        headers_to_pop.append(header)

        for header in headers_to_pop:
            cls.headers.pop(header)
        for id in ids_to_pop:
            cls.ids.pop(id)

    @classmethod
    def clear_global_references(cls) -> None:
        cls.global_ids = dict()
        cls.global_headers = dict()
