"""This Module is a general DTO data"""

class FinancialData:
    """
    This class is a general DTO data from project

    Attributes:
        currency (str): currency country
        fifty_two_week_high (float): highest price in the last two weeks
        fifty_two_week_low (float): lowest price in the last two weeks
        fifty_two_week_range (str): highest price in the last two weeks
        logo_url (str): url from logotype stock
        long_name (str): long name from stock
        short_name (str): short name from stock
        symbol (str): symbol name from stock
        regular_market_open (float): highest price in the last two weeks
        regular_market_previous_close (float): highest price in the last two weeks
        regular_market_price (float): price of stock
        regular_market_day_range (str): highest price in the last two weeks
        inflation_country (str): country's inflation rate
        selic_rate (str): country's selic rate
        dollar_euro (str): dollar and euro exchange rate
        stock (str): stock name e.g - MXRF11

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
            dollar_euro: str = None,
            stock: str = None
    ):

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
        self.stock = stock
