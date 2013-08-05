#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from dns.resolver import Resolver
from dns.resolver import Cache
from IPy import IP

from .log import loggit

class DnsResolver:

    def __init__(self):
        """
        Create an instance of a DNS resolver and assign a Cache
        to it, so it is possible to flush the cache if a record
        is stuck.
        """
        self.resolver = Resolver()
        self.resolver.cache = Cache()

    def setNameServers(self, servers=['8.8.8.8','8.8.4.4',]):
        """ 
        Set the nameservers to be used, to resolv the domain
        names. 
        """
        nameservers = []

        for s in servers:
            try:
                IP(s)
                nameservers.append(s)
            except:
                loggit('Invalide IP address: {0}'.format(s))

        if len(nameservers) == 0:
            nameservers = ['8.8.8.8','8.8.4.4',]
            loggit('Nameservers were all invalid.')

        self.resolver.nameservers = nameservers

    def getNameServers(self):
        """ Return the actual list of nameservers. """

        return self.resolver.nameservers

    def flushCache(self):
        """ Flush the DNS  cache of the current resolver. """

        return self.resolver.cache.flush()

    def getCacheData(self):
        """ Get the data that is in the cache. """

        return self.resolver.cache.data

    def resolv(self, name):
        """ Resolv the domain name and return the list of ip address.
        """
        try:
            answer = self.resolver.query(name)

            ips = []
            for ip in answer:
                ips.append(str(ip))

            loggit('dns:' + name + '    ips: {ips}' + str(ips))
        except:
            loggit('Unable to resolv the domain name using these nameservers.')

        return ips
    
    