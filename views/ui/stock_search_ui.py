"""UI stock search or main interface"""

import dearpygui.dearpygui as dpg

class SearchUi:
    """
    This class represents UI stock search
    """

    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0

    def calculate_screen_position(
            self,
            viewport_width: int = 1280,
            viewport_height: int = 720,
            window_width: int = 800,
            window_height: int = 600
    ):
        """
        This method calculate a screen position

        :param viewport_width: width size viewport
        :param viewport_height: height size viewport
        :param window_width: width size window
        :param window_height: height size window

        :return:
        """

        self.pos_x = int((viewport_width - window_width) / 2)
        self.pos_y = int((viewport_height - window_height) / 2)


    def screen_stock_search(self,):
        """
        This method create a screen

        :return:
        """

        with dpg.window(
                label='Pesquisar ação',
                width=800, height=600,
                no_close=True,
                pos=(self.pos_x, self.pos_y),
                no_move=True
        ):
            dpg.add_separator()
            dpg.add_separator()
            dpg.add_separator()

            dpg.add_text(label='DIGITE O NOME DA AÇÃO:',pos=(-510,38),show_label=True)

            dpg.add_input_text(tag='input_texto', width=250, indent=180, callback='')

            dpg.add_separator()
            dpg.add_separator()
            dpg.add_separator()
            dpg.add_separator()
            dpg.add_separator()