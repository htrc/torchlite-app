from collections import Counter


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
