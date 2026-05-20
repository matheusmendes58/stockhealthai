

class GetStockError(Exception):

    def __init__(self, ticker: str, original_error: Exception):
        self.ticker = ticker
        self.original_error = original_error
        self.message = f'Error retrieving stock data for {ticker}: {str(original_error)}'

        super().__init__(self.message)

class GetCurrencyError(Exception):

    def __init__(self, original_error: Exception):
        self.original_error = original_error
        self.message = f'Error retrieving currency data: {str(original_error)}'

        super().__init__(self.message)

class GetInflationError(Exception):

    def __init__(self, original_error: Exception):
        self.original_error = original_error
        self.message = f'Error retrieving inflation data: {str(original_error)}'

        super().__init__(self.message)

class GetSelicError(Exception):

    def __init__(self, original_error: Exception):
        self.original_error = original_error
        self.message = f'Error retrieving Selic data: {str(original_error)}'

        super().__init__(self.message)
