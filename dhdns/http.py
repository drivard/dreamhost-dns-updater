#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import requests
import ssl

class SSLAdapter(HTTPAdapter):
    '''An HTTPS Transport Adapter that uses an arbitrary SSL version.'''
    def __init__(self, ssl_version=ssl.PROTOCOL_TLSv1, **kwargs):
        self.ssl_version = ssl_version

        super(SSLAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                            maxsize=maxsize,
                            block=block,
                            ssl_version=self.ssl_version)
                            
class HttpRequest(object):
    """ This is a wrapper class arround the requests library because
    it requires TLSv1 protocole to open the HTTPS API url of Dreamhost.
    """
    
    def __init__(self):
        self.session = None
    
    def getSession(self):
        """ Create an HTTP session and mount our SSL adapter. """
        self.session = requests.Session()
        self.session.mount('https://', SSLAdapter())
        
        return self.session
