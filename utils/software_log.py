"""This module create a log in project """

import logging
import os


class LogStockHealthAI:
    """
    This class create a log in your project.
    """

    def __init__(self):
        self.log_path = "C:\\LOGS\\"
        self.log_file = os.path.join(self.log_path, "stockhealthai.txt")
        self._create_dir()
        self._loggin_basic_config()

    def _create_dir(self):
        """
        This method creates log folder.
        """
        if not os.path.isdir(self.log_path):
            os.mkdir(self.log_path)

    def _loggin_basic_config(self):
        """
        Basic logging configuration.

        :return:
        """

        logging.basicConfig(
            filename=self.log_file,
            filemode="a",
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
            encoding='utf-8'
        )

    @staticmethod
    def get_logger(name: str):
        """
        Returns a logger for the specified module.
        """
        return logging.getLogger(name)
