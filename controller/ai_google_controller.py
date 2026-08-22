"""Controller ai google"""

from config import settings
from services.ai.prompt import PromptIA
from services.ai.chat_google import AiGoogle
from models.financial_dto import FinancialData


class AiGoogleController:

    def __init__(self):
        self.prompt = PromptIA(data_text=FinancialData().short_name)
        self.dto = FinancialData()
        self.chat_google = AiGoogle(api_token=settings.google_token)


    def selic_information(self):
        """
        Search selic information in AI.

        :return:
        """

        self.dto.selic_rate = self.chat_google.chat_ai_google(self.prompt.prompt_google_selic)


    def dollar_euro_information(self):
        """
        Search dollar and euro information in AI.

        :return:
        """

        self.dto.dollar_euro = self.chat_google.chat_ai_google(self.prompt.prompt_google_currency)
