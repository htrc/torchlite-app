from collections import Counter
from extracted_features.volume import Volume
from extracted_features.page import Page


class WorkSet:
    def __init__(self, volume_list):
        self.volumes = [Volume(htid) for htid in volume_list]
        self._tokens = {}

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
