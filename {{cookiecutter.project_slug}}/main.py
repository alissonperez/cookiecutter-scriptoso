import logging
import argparse
import pprint

from inspect import getmembers, isfunction

import handlers


handlers_list = getmembers(handlers, isfunction)
handlers_by_name = {name.removeprefix('handler_'):func for name, func in handlers_list if name.startswith('handler_')}

parser = argparse.ArgumentParser()
parser.add_argument("handler", help="Command name", choices=handlers_by_name.keys())
parser.add_argument("--dryrun", help="Do not perform any action", action="store_true")
parser.add_argument("-v", "--verbose", help="Show more invo", action="store_true")

args = parser.parse_args()

logging.basicConfig(level=logging.INFO)
if args.verbose:
    logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    handlers_by_name[args.handler](args.verbose, args.dryrun)
