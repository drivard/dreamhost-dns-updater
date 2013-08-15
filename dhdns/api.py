#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import json

from .http import HttpRequest

class DHDnsManager(object):
    
    def __init__(self, key, format=None):

        # Dreamhost API settings
        self.key = key
        self.url = 'https://api.dreamhost.com/?' + 'key=' + self.key
        
        # HTTP Session
        h = HttpRequest()
        self.httpsession = h.getSession()

        # specify the output format
        if format is not None:
            self.url += '&format=' + format
            
    def add(self, record):
        """ Add a new Record. 
        
        Return true if the operation succeeded.
        """

        _cmd_ = 'dns-add_record'
        
        url = self.url + '&cmd=' + _cmd_ 
        url += '&record=' + record.record 
        url += '&type=' + record.type
        url += '&value=' + record.value        
        url += '&comment=' + record.comment
        
        result = self.httpsession.get(url)
        j = json.loads(result.content)
        
        return j.get('result') == 'success'

    def delete(self, record):
        """ Delete a new Record. 
        
        Return true if the operation succeeded.
        """

        _cmd_ = 'dns-remove_record'

        url = self.url + '&cmd=' + _cmd_ 
        url += '&record=' + record.record 
        url += '&type=' + record.type
        url += '&value=' + record.value
        
        result = self.httpsession.get(url)
        j = json.loads(result.content)
        
        return j.get('result') == 'success'

    def update(self, old_record, new_record):
        """
        This function is a two steps function.
        1) Add the new record with the new IP address.
        2) Delete the old record.
        """
        
        result_added = False
        result_deleted = False

        """ Let's add the new record. """
        result_deleted = self.delete(old_record)

        """ Let's delete the A record containing the old ip. """
        if result_deleted:
            result_added = self.add(new_record)
        
        return (result_deleted,result_added)

    def list(self, editable=1): 
        """ Does DH sees the update we just made? 
        Lets get the list of DNS records they have.
        
        Return the a JSON object of all the data returned by the API.
        """
        
        _cmd_ = 'dns-list_records'
        _editable_ = editable
        
        url = self.url + '&cmd=' + _cmd_
        url += '&editable=' + str(_editable_)
        
        result = self.httpsession.get(url)
        j = json.loads(result.content)
        
        return j.get('data')
