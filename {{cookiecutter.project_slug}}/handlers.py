import logging

import data
import consolecolor as ccolor


logger = logging.getLogger(__name__)


def handler_quotation(verbose, dryrun):
    '''Simple method to show current quotation of USD / BRL'''

    quotation = data.get_quotation(verbose, dryrun)

    logger.info('Quotation USD-BRL, ask for: {}'.format(ccolor.green('R$ {}'.format(quotation['USDBRL']['ask']))))
