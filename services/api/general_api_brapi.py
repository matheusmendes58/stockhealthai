"""This module represent general config api and treatment response, Some functions of this API do not work in free mode."""

from brapi import Brapi
from brapi.types import QuoteRetrieveResponse
from brapi.types.v2 import CurrencyRetrieveResponse, InflationRetrieveResponse, PrimeRateRetrieveResponse
from models.financial_dto import FinancialData
from utils.custom_exceptions.brapi_exceptions import (
    GetStockError,
    GetCurrencyError,
    GetInflationError,
    GetSelicError
)

class BrapiApi:
    """
    This class represents Brapi API config and more.
    """

    def __init__(self, token: str):

        self.client = Brapi(api_key=token)

    def get_stock(
            self,
            tickers: str,
            period: str = '3mo',
            dividends: bool = False,
            fundamental: bool = True) -> QuoteRetrieveResponse:

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

            return response

        except Exception as e:
            raise GetStockError(ticker=tickers, original_error=e)

    def get_personal_stock(
            self,
            tickers: str,
            period: str = '3mo',
            dividends: bool = False,
            fundamental: bool = True) -> FinancialData:

        """
        Retrieve personal stock data from the API.

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
            ).results[0]

            return FinancialData(
                currency=response.currency,
                fifty_two_week_low=response.fifty_two_week_low,
                fifty_two_week_high=response.fifty_two_week_high,
                fifty_two_week_range=response.fifty_two_week_range,
                logo_url=response.logourl,
                long_name=response.long_name,
                short_name=response.short_name,
                symbol=response.symbol,
                regular_market_open=response.regular_market_open,
                regular_market_previous_close=response.regular_market_previous_close,
                regular_market_price=response.regular_market_price,
                regular_market_day_range=response.regular_market_day_range
            )

        except Exception as e:
            raise GetStockError(ticker=tickers, original_error=e)

    def get_currency(self, currency: str = 'USD-BRL,EUR-BRL') -> CurrencyRetrieveResponse:
        """
        Retrieve currency values (USD - Dolar americano, EUR - Euro) - NO WORK FREE SIGNATURE API

        :param currency: currency information to be returned
        :return: CurrencyRetrieveResponse object
        """

        try:
            response = self.client.v2.currency.retrieve(currency=currency)

            return  response

        except Exception as e:
            raise GetCurrencyError(original_error=e)

    def get_inflation(self, date: str) -> InflationRetrieveResponse:
        """
        Retrieve inflation country - NO WORK FREE SIGNATURE API

        :param date: date from historical inflation country (format utilized -> 2026-01-01)

        :return: InflationRetrieveResponse object
        """

        try:
            response = self.client.v2.inflation.retrieve(
                country='brazil',
                historical=True,
                start=date
            )

            return response

        except Exception as e:
            raise GetInflationError(original_error=e)

    def get_selic(self) -> PrimeRateRetrieveResponse:
        """
        Retrieve basic interest rate country - NO WORK FREE SIGNATURE API

        :return: PrimeRateRetrieveResponse object
        """

        try:
            response = self.client.v2.prime_rate.retrieve(
                country='brazil',
                historical=False,
            )

            return response

        except Exception as e:
            raise GetSelicError(original_error=e)
