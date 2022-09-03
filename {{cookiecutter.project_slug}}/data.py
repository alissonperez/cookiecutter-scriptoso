import logging

import requests


def get_quotation(verbose, dryrun):
    endpoint = 'http://economia.awesomeapi.com.br/json/last/USD-BRL'
    response = requests.get(endpoint)

    if response.status_code // 100 != 2:
        raise Exception(f'Error calling api, response status code {response.status_code}')

    if verbose:
        logging.debug(f'Endpoint "{endpoint}" answered with status code {response.status_code}')

    return response.json()
