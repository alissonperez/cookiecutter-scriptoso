import logging

import data


def handler_quotation(verbose, dryrun):
    quotation = data.get_quotation(verbose, dryrun)

    logging.info('Quotation USD-BRL, ask for: R$ {}'.format(quotation['USDBRL']['ask']))
