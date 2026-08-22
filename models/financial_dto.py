"""This Module is a general DTO data"""

class FinancialData:
    """
    This class is a general DTO data from project
    """

    def __init__(
            self,
            currency: str = None,
            fifty_two_week_high: float = None,
            fifty_two_week_low: float = None,
            fifty_two_week_range: str = None,
            logo_url: str = None,
            long_name: str = None,
            short_name: str = None,
            symbol: str = None,
            regular_market_open: float = None,
            regular_market_previous_close: float = None,
            regular_market_price: float = None,
            regular_market_day_range: str = None,
            inflation_country: str = None,
            selic_rate: str = None,
            dollar_euro: str = None
    ):
        """
        DTO params

        :param currency: currency country
        :param fifty_two_week_high: the highest price in the last two weeks
        :param fifty_two_week_low: the lowest price in the last two weeks
        :param fifty_two_week_range: the price ranged over the last two weeks
        :param logo_url: url from logotype stock
        :param long_name: long name from stock e.g - Maxi Renda Fundo de Investimento Imobiliario Cotas
        :param short_name: short name from stock e.g - MXRF11
        :param symbol: symbol name from stock e.g - MXRF11
        :param regular_market_open: the stock's opening price.
        :param regular_market_previous_close: the stock's closing price.
        :param regular_market_price: price of stock
        :param regular_market_day_range: the price ranged over the day
        :param inflation_country: the country's inflation rate.
        :param selic_rate: the country's selic  rate.
        :param dollar_euro: dollar and euro exchange rate.
        """

        self.currency = currency
        self.fifty_two_week_high = fifty_two_week_high
        self.fifty_two_week_low = fifty_two_week_low
        self.fifty_two_week_range = fifty_two_week_range
        self.logo_url = logo_url
        self.long_name = long_name
        self.short_name = short_name
        self.symbol = symbol
        self.regular_market_open = regular_market_open
        self.regular_market_previous_close = regular_market_previous_close
        self.regular_market_price = regular_market_price
        self.regular_market_day_range = regular_market_day_range
        self.inflation_country = inflation_country
        self.selic_rate = selic_rate
        self.dollar_euro = dollar_euro
