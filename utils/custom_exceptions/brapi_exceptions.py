from brapi import APIError

class GetStockError(APIError):

    def __init__(self, ticker: str, original_error: Exception):
        self.ticker = ticker
        self.original_error = original_error
        self.message = f'Error retrieving stock data for {ticker}: {str(original_error)}'

        super().__init__(self.message)
