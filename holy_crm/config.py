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

    def database_location(self):
        """Return the location of the database folder"""
        if "database_location" in self.config:
            return self.config["database_location"]
        return os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/..")

    def get_filter(self):
        """Read the configured filter"""
        builder = Filter.builder()
        builder.read_config(self.config)
        return builder.build()

    def captcha_enabled(self):
        return ("captcha" in self.config)

    def use_proxy(self):
        return ("use_proxy_list" in self.config and self.config["use_proxy_list"])
