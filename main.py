"""Here is where the software is executed."""

import dearpygui.dearpygui as dpg
from views.ui.stock_search_ui import SearchUi

def main():
    dpg.create_context()

    search_ui = SearchUi()

    search_ui.calculate_screen_position()

    search_ui.screen_stock_search()

    dpg.create_viewport(title="StockHealth AI", width=1280, height=720)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
