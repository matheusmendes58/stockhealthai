"""Controller viewport """

import dearpygui.dearpygui as dpg
from views.ui.stock_search_ui import SearchUi
from views.ui.viewport_ui import ViewportUi

class ViewportController:

    @staticmethod
    def viewport_screen():
        dpg.create_context()

        search_ui = SearchUi()

        search_ui.calculate_screen_position()

        search_ui.screen_stock_search()

        viewport_ui = ViewportUi()

        viewport_ui.screen_viewport()
