"""Wrap configuration options as an object"""
import os
import logging
import yaml

class Config:
    """Class to represent flathunter configuration"""

    __log__ = logging.getLogger('holy-crm')

    def __init__(self, filename=None, string=None):
        if filename is None:
            filename = os.path.dirname(os.path.abspath(__file__)) + "/../config.yaml"
        self.__log__.info("Using config %s", filename)
        with open(filename) as file:
            self.config = yaml.safe_load(file)

    def __iter__(self):
        """Emulate dictionary"""
        return self.config.__iter__()

    def __getitem__(self, value):
        """Emulate dictionary"""
        return self.config[value]

    def get(self, key, value=None):
        """Emulate dictionary"""
        return self.config.get(key, value)
