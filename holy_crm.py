import argparse
import time
import logging
import os
from pprint import pformat

from holy_crm.config import Config
from holy_crm.crm_runner import CrmRunner

# init logging
if os.name == 'posix':
    # coloring on linux
    CYELLOW = '\033[93m'
    CBLUE = '\033[94m'
    COFF = '\033[0m'
    LOG_FORMAT = '[' + CBLUE + '%(asctime)s' + COFF + '|' + CBLUE + '%(filename)-18s' + COFF + \
             '|' + CYELLOW + '%(levelname)-8s' + COFF + ']: %(message)s'
else:
    # else without color
    LOG_FORMAT = '[%(asctime)s|%(filename)-18s|%(levelname)-8s]: %(message)s'

logging.basicConfig(
    format=LOG_FORMAT,
    datefmt='%Y/%m/%d %H:%M:%S',
    level=logging.INFO)

__log__ = logging.getLogger('holy_crm')

def launch_holy_crm(config):
    runner = CrmRunner(config)
    runner.start()

def main():
    print("""
| |__   ___ | |_   _        ___ _ __ _ __ ___  
| '_ \ / _ \| | | | |_____ / __| '__| '_ ` _ \ 
| | | | (_) | | |_| |_____| (__| |  | | | | | |
|_| |_|\___/|_|\__, |      \___|_|  |_| |_| |_|
               |___/                      alpha
        """)

    parser = argparse.ArgumentParser(description=\
             "Customer relationship mailer", epilog="Designed by dnberlin")
    parser.add_argument('--config', '-c',
                        type=argparse.FileType('r', encoding='UTF-8'),
                        default='%s/config.yaml' % os.path.dirname(os.path.abspath(__file__)),
                        help="Config file to use. If not set, try to use '%s/config.yaml' " %
                        os.path.dirname(os.path.abspath(__file__))
                        )
    args = parser.parse_args()

    # load config
    config_handle = args.config
    config = Config(config_handle.name)

    # check config
    if not config.get('mail', dict()).get('smtp_server') or not config.get('mail', dict()).get('smtp_port'):
        __log__.error("No mailserver configured. Starting like this would be pointless...")
        return
    if not config.get('mail', dict()).get('user_email') or not config.get('mail', dict()).get('user_pw'):
        __log__.error("No login for mailserver configured.")
        returncustomer
    if not config.get('mail', dict()).get('sender_name'):
        __log__.error("No name of sender defined.")
        return

    # adjust log level, if required
    if config.get('verbose'):
        __log__.setLevel(logging.DEBUG)
        __log__.debug("Settings from config %s", pformat(config))
    
    launch_holy_crm(config)

if __name__ == '__main__':
    main()
