from collections import Counter
from urllib.parse import urlparse
import requests
import logging


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
    def metadata(self):
        return self.data["metadata"]

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


class WorkSet:
    def __init__(self, volume_list=[]):
        self.volumes = [Volume(htid) for htid in volume_list]
        self._tokens = {}
        self._description = ""

    def import_ws(self, ws_id):
        try:
            r = requests.get(ws_id)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

        json = r.json()
        self._description = json['description']
        for gathered in json['gathers']:
            v_id = urlparse(gathered['id']).path.split('/')[-1]
            self.volumes.append(Volume(v_id))

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, v):
        self._description = v

    @property
    def metadata(self):
        return [v.metadata for v in self.volumes]

    @property
    def tokens(self):
        if not self._tokens:
            for volume in self.volumes:
                for token in volume.tokens.keys():
                    try:
                        tok = self._tokens[token]
                    except KeyError:
                        self._tokens[token] = {"pos": Counter()}
                        tok = self._tokens[token]
                    tok["pos"].update(volume.tokens[token]["pos"])
        return self._tokens


class Page:
    def __init__(self, kwargs):
        self._kwargs = kwargs
        self._tokens = {}

    def __repr__(self):
        return f"{self.__class__.__name__}({self.seq})"

    @property
    def seq(self):
        return self._kwargs["seq"]

    @property
    def tokenCount(self):
        return self._kwargs["tokenCount"]

    @property
    def lineCount(self):
        return self._kwargs["lineCount"]

    @property
    def emptyLineCount(self):
        return self._kwargs["emptyLineCount"]

    @property
    def sentenceCount(self):
        return self._kwargs["sentenceCount"]

    @property
    def header(self):
        return self._kwargs["header"]

    @property
    def body(self):
        return self._kwargs["body"]

    @property
    def footer(self):
        return self._kwargs["footer"]

    @property
    def calculatedLanguage(self):
        return self._kwargs["calculatedLanguage"]

    # The following values are hoisted from the body section;
    # TODO make them the sum of values from header, body, and footer

    @property
    def capAlphaSeq(self):
        try:
            return self.body["capAlphaSeq"]
        except TypeError:
            return 0

    @property
    def beginCharCount(self):
        try:
            return self.body["beginCharCount"]
        except TypeError:
            return {}

    @property
    def endCharCount(self):
        try:
            return self.body["endCharCount"]
        except TypeError:
            return {}

    @property
    def tokenPosCount(self):
        try:
            return self.body["tokenPosCount"]
        except TypeError:
            return {}

    @property
    def tokens(self):
        if not self._tokens:
            for k in self.tokenPosCount.keys():
                token = k.lower()
                pos = list(self.tokenPosCount[k])[0]
                count = self.tokenPosCount[k][pos]
                try:
                    self._tokens[token]["pos"].update({pos: count})
                except KeyError:
                    self._tokens[token] = {"pos": Counter({pos: count})}
        return self._tokens
