from collections import Counter
import requests
import logging
from extracted_features.page import Page


class Volume:
    base_url = "https://tools.htrc.illinois.edu/ef-api/volumes"

    def __init__(self, htid):
        self.id = htid
        self._data = {}
        self._pages = []
        self._tokens = {}

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id})"

    @property
    def data(self):
        if not self._data:
            url = "/".join((self.base_url, self.id))
            r = requests.get(url)
            json = r.json()
            try:
                self._data = json["data"]
            except KeyError:
                logging.warning(r.json()["message"])
        return self._data

    @property
    def features(self):
        return self.data["features"]

    @property
    def pageCount(self):
        return self.features["pageCount"]

    @property
    def pages(self):
        if not self._pages:
            self._pages = [Page(page) for page in self.features["pages"]]
        return self._pages

    @property
    def tokens(self):
        if not self._tokens:
            for page in self.pages:
                for token in page.tokens.keys():
                    try:
                        tok = self._tokens[token]
                    except KeyError:
                        self._tokens[token] = {"pos": Counter()}
                        tok = self._tokens[token]
                    tok["pos"].update(page.tokens[token]["pos"])
        return self._tokens
