#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from ConfigParser import ConfigParser
import os

from .__init__ import __config_folder__ as CONFIG_FOLDER
from .__init__ import __config_file__ as CONFIG_FILE
from .__init__ import __home_folder__ as HOME

def load_config_file():
    '''This function load all the configuration from the file located
    in ~/.dhdm/dhdm.conf and return all the information.
    '''

    config = ConfigParser()
    config.read(HOME + CONFIG_FILE)

    sections = config.sections()

    options = []

    for s in sections:
        options.extend(config.items(s))

    configs = {}

    for opt in options:
        configs[opt[0]] = opt[1]

    return configs
