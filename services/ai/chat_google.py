# All about Google Gemini API
#TODO Colocar Try Exception
from google import genai
from utils.software_log import LogStockHealthAI

class AiGoogle:

    def __init__(self, api_token: str = None):

        self.client_google = genai.Client(api_key=api_token)
        self.log = LogStockHealthAI().get_logger(__name__)

    def chat_ai_google(self, prompt: str) -> str:
        """
        This function call chat in AI from Google

        :param prompt: PROMPT used from AI

        :return: Response of AI
        """

        self.log.info("Obtendo resposta da GEMINI AI")

        try:

            response = self.client_google.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:
            self.log.error(str(e))
