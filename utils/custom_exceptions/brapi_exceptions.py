

class GetStockError(Exception):
    """
    This exception is raised when a stock error occurs

    Attributes:
        ticker (str): stock name
        original_error (Exception): original error
        message (str): error message
    """

    def __init__(self, ticker: str, original_error: Exception):
        self.ticker = ticker
        self.original_error = original_error
        self.message = f'Error retrieving stock data for {ticker}: {str(original_error)}'

        super().__init__(self.message)

class GetCurrencyError(Exception):
    """
    This exception is raised when a currency error occurs

    Attributes:
        original_error (Exception): original error
        message (str): error message
    """

    def __init__(self, original_error: Exception):
        self.original_error = original_error
        self.message = f'Error retrieving currency data: {str(original_error)}'

        super().__init__(self.message)

class GetInflationError(Exception):
    """
    This exception is raised when as inflation error occurs

    Attributes:
        original_error (Exception): original error
        message (str): error message
    """

    def __init__(self, original_error: Exception):
        self.original_error = original_error
        self.message = f'Error retrieving inflation data: {str(original_error)}'

        super().__init__(self.message)

class GetSelicError(Exception):
    """
    This exception is raised when a selic error occurs

    Attributes:
        original_error (Exception): original error
        message (str): error message
    """

    def __init__(self, original_error: Exception):
        self.original_error = original_error
        self.message = f'Error retrieving Selic data: {str(original_error)}'

        super().__init__(self.message)
