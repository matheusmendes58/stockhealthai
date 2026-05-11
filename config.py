
# All settings in project is here example passwords, string connections, etc

import os
from dotenv import load_dotenv

load_dotenv()

class AllSettings:
    """
    General settings from application

    """

    def __init__(self):

        #AI
        self.google_token = None

        #BRAPI_API
        self.brapi_api_token = None

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
