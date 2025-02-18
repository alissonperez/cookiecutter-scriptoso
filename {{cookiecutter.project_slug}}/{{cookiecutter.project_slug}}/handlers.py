import logging

from icecream import ic

from {{cookiecutter.project_slug}} import consolecolor as ccolor, data
from {{cookiecutter.project_slug}}.tools import handler{%- if cookiecutter.kafka|lower == 'y' %}
from {{cookiecutter.project_slug}} import kafka
{%- endif %}


logger = logging.getLogger(__name__)


@handler
def handler_quotation(dryrun=False):
    '''Simple method to show current quotation of USD / BRL'''

    ic('getting quotation', dryrun)

    quotation = data.get_quotation(True, dryrun)

    logger.info('Quotation USD-BRL, ask for: {}'.format(ccolor.green('R$ {}'.format(quotation['USDBRL']['ask']))))
    logger.warn('Quotation USD-BRL, ask for: {}'.format(ccolor.green('R$ {}'.format(quotation['USDBRL']['ask']))))
    logger.error('Quotation USD-BRL, ask for: {}'.format(ccolor.green('R$ {}'.format(quotation['USDBRL']['ask']))))


def handler_read_csv(filename, verbose=True, dryrun=False):
    '''Read a CSV file and print its content'''

    ic('reading CSV file')

    for line in data.read_csv(filename):
        logger.info(f'Content: {ccolor.green(line)}')
{%- if cookiecutter.kafka|lower == 'y' %}

def handler_consume_topic(verbose=True, dryrun=False):
    '''Consume Kafka messages'''

    ic('reading messages from Kafka')

    for msg in kafka.consume('my-topic-name'):
        logger.info(f'Content: {ccolor.green(msg)}')
{%- endif %}
