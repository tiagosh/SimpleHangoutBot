# -*- coding: utf-8 -*-

import re

class Addon(object):
    def __init__(self, config, name):
        if name != None:
            self.name = name
        self._data = ()
        self._config = config

ADDON = { }

def all():
    return ADDON.keys()

def _init(label, config):
    return ADDON[label](config)

def addons(config):
    ret = [ _init(i, config) for i in config.getlist('Global', 'addons') ]
    if config.changed():
        config.write()
    return ret
