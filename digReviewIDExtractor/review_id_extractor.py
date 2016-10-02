# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-09-30 22:33:42
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-10-02 15:41:56


import copy 
import types
from digExtractor.extractor import Extractor
from digride import DIGRIDE


class ReviewIDExtractor(Extractor):

    def __init__(self):
        self.renamed_input_fields = ['text']

    def extract(self, doc):
        if 'text' in doc:
            return DIGRIDE.extract(doc['text'])
        return None

    def get_metadata(self):
        return copy.copy(self.metadata)

    def set_metadata(self, metadata):
        self.metadata = metadata
        return self

    def get_renamed_input_fields(self):
        return self.renamed_input_fields
