"""This module represent general config api and treatment response"""

from brapi import Brapi
from brapi.types import QuoteRetrieveResponse
from utils.custom_exceptions.brapi_exceptions import GetStockError

from config import settings


class BrapiApi:
    """
    This class represents Brapi API config and more.
    """

    def __init__(self, token: str):

        self.client = Brapi(api_key=token)
        self.stock = ''
        self.result_formated = None


    def get_stock(
            self,
            tickers: str,
            period: str = '3mo',
            dividends: bool = False,
            fundamental: bool = True) -> 'QuoteRetrieveResponse':

        """
        Retrieve stock data from the API.

        :param tickers: Stock ticker symbol (e.g., 'AAPL', 'PETR4.SA')
        :param period: Time range for the query (e.g., '1mo', '3mo', '1y')
        :param dividends: Whether to include dividends data
        :param fundamental: Whether to include fundamental data

        :return: QuoteRetrieveResponse object
        """

        try:
            response = self.client.quote.retrieve(
                tickers=tickers,
                range=period,
                dividends=dividends,
                fundamental=fundamental
            )
        except Exception as e:
            raise GetStockError(ticker=tickers, original_error=e)

        return response
