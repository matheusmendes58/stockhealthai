"""Controller viewport """

import dearpygui.dearpygui as dpg
from models.financial_dto import FinancialData
from views.ui.stock_search_ui import SearchUi
from views.ui.viewport_ui import ViewportUi

class ViewportController:

    def __init__(self):

        self.dto = FinancialData()

        self.search_ui = SearchUi()

        self.viewport_ui = ViewportUi()

    def viewport_screen(self):

        dpg.create_context()

        self.search_ui.calculate_screen_position()

        self.search_ui.screen_stock_search()

        self.viewport_ui.screen_viewport()
