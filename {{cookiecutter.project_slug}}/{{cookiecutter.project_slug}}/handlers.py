import logging


from {{cookiecutter.project_slug}} import consolecolor as ccolor, data{%- if cookiecutter.kafka|lower == 'y' %}
from {{cookiecutter.project_slug}} import kafka
{%- endif %}


logger = logging.getLogger(__name__)


def handler_quotation(verbose, dryrun):
    '''Simple method to show current quotation of USD / BRL'''

    quotation = data.get_quotation(verbose, dryrun)

    logger.info('Quotation USD-BRL, ask for: {}'.format(ccolor.green('R$ {}'.format(quotation['USDBRL']['ask']))))
{%- if cookiecutter.kafka|lower == 'y' %}


def handler_consume_topic(verbose, dryrun):
    '''Consume Kafka messages'''

    for msg in kafka.consume('my-topic-name'):
        print('MSG:', msg)
{%- endif %}
