#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import syslog

def loggit(message):
    """ Use log('message') to log message in /var/log/syslog. """
    
    return syslog.syslog(str(message))