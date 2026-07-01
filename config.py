#All settings in project is here example passwords, string connections, etc

import os


class AllSettings:
    """
    General settings from application

    """

    def __init__(self):

        #AI
        self.google_token = os.getenv('GOOGLE_GEMINI')

        #BRAPI_API
        self.brapi_api_token = os.getenv('BRAPI_API_TOKEN')

    def env_check(self) -> bool:
        """
        checks if environment variables are entered correctly.

        :return: A String value
        """

        if self.google_token and self.brapi_api_token:
            return True
        else:
            return False


settings = AllSettings()
