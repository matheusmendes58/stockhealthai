"""Controller AI google"""

from config import settings
from services.ai.prompt import PromptIA
from services.ai.chat_google import AiGoogle
from models.financial_dto import FinancialData


class AiGoogleController:

    def __init__(self):
        self.dto = FinancialData()
        self.prompt = PromptIA()
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

    def stock_information(self, stock_name: str):
        """
        Search stock information in AI.

        :return:
        """

        self.prompt.data_text = stock_name

        if not stock_name:
            self.dto.short_name = 'PESQUISE PRIMEIRO UMA AÇÃO NO CAMPO "DIGITE O NOME DA AÇÃO". '

            return

        self.dto.short_name = self.chat_google.chat_ai_google(self.prompt.data_text)
