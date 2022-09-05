import argparse
from inspect import getmembers, isfunction

from dotenv import load_dotenv

from {{cookiecutter.project_slug}} import handlers, logger, consolecolor as ccolor


load_dotenv()  # take environment variables from .env.

handlers_list = getmembers(handlers, isfunction)
handlers_by_name = {name.removeprefix('handler_'): func for name, func in handlers_list if name.startswith('handler_')}

docs = '\n'.join([' {}: {}'.format(ccolor.blue(ccolor.bold(name)), func.__doc__ or 'No docstrings filled...')
                  for name, func in handlers_by_name.items()])

project_name = ccolor.green('{{ cookiecutter.project_name }}')

description = '\n'.join([
    f'Welcome to {project_name} script!',
    '',
    'Command descriptions:',
    '',
    docs
])

parser = argparse.ArgumentParser(prog='{{ cookiecutter.project_slug }}',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description=description)
parser.add_argument("handler", help="Command to be executed", choices=handlers_by_name.keys())
parser.add_argument("--dryrun", help="Do not perform any action", action="store_true")
parser.add_argument("--nocolors", help="Disable colors in output", action="store_true")
parser.add_argument("-v", "--verbose", help="Show more invo", action="store_true")

args = parser.parse_args()

if args.nocolors:
    ccolor.enabled = False

logger.setup(ccolor.enabled, args.verbose)

if __name__ == '__main__':
    handlers_by_name[args.handler](args.verbose, args.dryrun)
