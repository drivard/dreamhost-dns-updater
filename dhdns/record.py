#!/usr/bin/env python
# -*- coding: utf-8 -*- 

class Record():
    """ A simple DNS record representation. """
    
    def __init__(self, record, type, value, comment):
        self.record = record
        self.type = type
        self.value = value
        self.comment = comment