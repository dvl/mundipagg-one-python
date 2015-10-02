from mundipaggOnePython.resource_clients import SaleResource, CreditCardResource


class GatewayServiceClient(object):
    def __init__(self, merchant_key=None, environment=None, http_content_type=None, host_uri=None):
        self.sale = SaleResource(merchant_key, environment, http_content_type, host_uri)
        self.credit_card = CreditCardResource(merchant_key, environment, http_content_type, host_uri)

    @property
    def sale(self):
        return self.__sale

    @sale.setter
    def sale(self, sale_resource):
        if type(sale_resource) is SaleResource:
            self.__sale = sale_resource
        else:
            self.__sale = None

    @property
    def credit_card(self):
        return self.__credit_card

    @credit_card.setter
    def credit_card(self, credit_card_resource):
        if type(credit_card_resource) is CreditCardResource:
            self.__credit_card = credit_card_resource
        else:
            self.__credit_card = None

