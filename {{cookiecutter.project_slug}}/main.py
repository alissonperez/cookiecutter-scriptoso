from inspect import getmembers, isfunction

import fire
from dotenv import load_dotenv

from {{cookiecutter.project_slug}} import handlers, logger, consolecolor as ccolor


load_dotenv()  # take environment variables from .env.

handlers_list = getmembers(handlers, isfunction)
handlers_by_name = {name.removeprefix('handler_'): func for name, func in handlers_list if name.startswith('handler_')}

if __name__ == '__main__':
    fire.Fire(handlers_by_name)
