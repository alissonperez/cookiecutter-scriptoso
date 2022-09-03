
import data


def handler_quotation(verbose, dryrun):
    quotation = data.get_quotation(verbose, dryrun)
    print('Quotation:', quotation)
