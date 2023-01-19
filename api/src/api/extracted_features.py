from collections import Counter
from urllib.parse import urlparse
import uuid
import requests
import logging


class Volume:
    base_url = "https://tools.htrc.illinois.edu/ef-api/volumes"

    def __init__(self, htid):
        self.id = htid
        self._data = {}
        self._pages = []
        self._tokens = {}
        self._title = None
        self._type = None

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

    def fetch_metadata(self, field):
        url = f"{self.base_url}/{self.id}/metadata?fields=metadata.{field}"
        r = requests.get(url)
        json = r.json()
        return json['data']['metadata'][field]

    @property
    def title(self):
        if not self._title:
            url = f"{self.base_url}/{self.id}/metadata?fields=metadata.title"
            r = requests.get(url)
            json = r.json()
            self._title = json['data']['metadata']['title']
        return self._title

    @property
    def type(self):
        if not self._type:
            self._type = self.fetch_metadata('type')
        return self._type

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
    def __init__(self, **kwargs):
        self.id = str(uuid.uuid1())
        self.type = None
        self.description = None
        self.created = None
        self.extent = None
        self.title = None
        self.visibility = None
        self.intent = None
        self.gathers = []
        self._volumes = {}
        self._tokens = {}

        if 'url' in kwargs:
            self.load_workset(kwargs['url'])

    def load_workset(self, url):
        try:
            r = requests.get(url)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

        self._json = r.json()
        self.id = self._json['id']
        self.description = self._json['description']
        self.type = self._json['type']
        self.created = self._json['created']
        self.extent = self._json['extent']
        self.title = self._json['title']
        self.visibility = self._json['visibility']
        self.intent = self._json['intent']
        self.gathers = self._json['gathers']

    @property
    def volumes(self):
        if not self._volumes:
            self._volumes = {}
            for gathered in self.gathers:
                v_id = urlparse(gathered['id']).path.split('/')[-1]
                self.add_volume(v_id)
        return self._volumes

    def add_volume(self, volume_id):
        self._volumes[volume_id] = Volume(volume_id)

    def get_volume(self, volume_id):
        return self.volumes[volume_id]

    def delete_volume(self, volume_id):
        del self.volumes[volume_id]
        return self.volumes

    @property
    def metadata(self):
        return [v.metadata for v in self.volumes.values()]

    @property
    def tokens(self):
        if not self._tokens:
            for volume in self.volumes.values():
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
