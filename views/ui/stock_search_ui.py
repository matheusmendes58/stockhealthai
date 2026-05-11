"""UI stock search or main interface"""

import dearpygui.dearpygui as dpg
from models.financial_dto import FinancialData

class SearchUi:
    """
    This class represents UI stock search
    """

    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.dto = FinancialData()

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


    def screen_stock_search(self):
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
            dpg.add_spacer(height=20)

            dpg.add_text(label='DIGITE O NOME DA AÇÃO:', pos=(-510,63), show_label=True)

            dpg.add_input_text(tag='input_texto', width=250, indent=180, callback='')

            dpg.add_spacer(height=10)
            dpg.add_separator()
            dpg.add_separator()
            dpg.add_separator()
            dpg.add_spacer(height=20)

            with dpg.table(
                    header_row=True,
                    height=250,
                    width=800,
                    borders_innerH=True,
                    borders_outerH=True,
                    borders_innerV=True,
                    borders_outerV=True
            ):

                dpg.add_table_column(label='INFORMAÇÕES')
                dpg.add_table_column(label='RESULTADO')

                with dpg.table_row():
                    dpg.add_text('Nome da ação: '.upper())
                    dpg.add_text(f'{self.dto.long_name}')

                with dpg.table_row():
                    dpg.add_text('Nome Abreviado: '.upper())
                    dpg.add_text(f'{self.dto.short_name}')

                with dpg.table_row():
                    dpg.add_text('Simbolo: '.upper())
                    dpg.add_text(f'{self.dto.symbol}')

                with dpg.table_row():
                    dpg.add_text('Preço da ação: '.upper())
                    dpg.add_text(f'{self.dto.regular_market_price}')

                with dpg.table_row():
                    dpg.add_text('Preço de abertura: '.upper().upper())
                    dpg.add_text(f'{self.dto.regular_market_open}')

                with dpg.table_row():
                    dpg.add_text('Preço de fechamento: '.upper())
                    dpg.add_text(f'{self.dto.regular_market_previous_close}')

                with dpg.table_row():
                    dpg.add_text('Preço do dia anterior: '.upper())
                    dpg.add_text(f'{self.dto.regular_market_day_range}')

                with dpg.table_row():
                    dpg.add_text('Alta de preço nas ultimas 2 semanas: '.upper())
                    dpg.add_text(f'{self.dto.fifty_two_week_high}')

                with dpg.table_row():
                    dpg.add_text('Baixa de preço nas ultimas 2 semanas: '.upper())
                    dpg.add_text(f'{self.dto.fifty_two_week_low}')

                with dpg.table_row():
                    dpg.add_text('Variação de preço nas ultimas 2 semanas (média): '.upper())
                    dpg.add_text(f'{self.dto.fifty_two_week_range}')
