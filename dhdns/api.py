#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import requests

class DHDnsManager(object):
    
    def __init__(self, key, format=None):

        self.key = key
        self.url = 'https://api.dreamhost.com/?' + 'key=' + self.key

        if format is not None:
            self.url += '&format=' + format
            
    def add(self, record):
        """ Add a new Record. """

        _cmd_ = 'dns-add_record'
        
        self.url += '&cmd=' + _cmd_ 
        self.url += '&=record' + record.record 
        self.url += '&=type' + record.type
        self.url += '&=value' + record.value

        return True

    def delete(self, record):
        """ Delete a new Record. """

        _cmd_ = 'dns-remove_record'

        self.url += '&cmd=' + _cmd_ 
        self.url += '&=record' + record.record 
        self.url += '&=type' + record.type
        self.url += '&=value' + record.value

        return True

    def update(self, old_record):
        """
        This function is a two steps function.
        1) Add the new record with the new IP address.
        2) Delete the old record.
        """

        """ Let's add the new record. """

        """ Let's delete the A record containing the old ip. """


    def list(self): 
        """ Does DH sees the update we just made? """
        _cmd_ = 'dns-list_records'

        self.url += '&cmd=' + _cmd_

    def callApi(self):
        """
        Use the requests library to call the Dreamhost API.
        
        For the present we will disable the verification of
        the SSL certificate because there is a problem not
        recognizing the CA certificate.
        """
    
        return requests.get(self.url, verify=False)
