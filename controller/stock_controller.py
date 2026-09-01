"""Controller for stock_search_ui"""

from models.financial_dto import FinancialData
from services.api.general_api_brapi import BrapiApi
from config import settings
from utils.dictonary import stock

class StockController:

    def __init__(self):
        self.dto = FinancialData()

    def store_data(self):
        """
        store data in dictionary

        :return:
        """

        stock['stock_name'] = self.dto.short_name

    def search_stock(self, ticker):
        """
        Search stock in brapi

        :return:
        """

        api_stock = BrapiApi(token=settings.brapi_api_token)

        self.dto = api_stock.get_personal_stock(tickers=ticker)

        self.store_data()

        return self.dto
