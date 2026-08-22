"""UI stock search or main interface"""
#TODO Mostrar erro na UI quando não achar ação especifica
import dearpygui.dearpygui as dpg
from config import settings
from models.financial_dto import FinancialData
from services.api.general_api_brapi import BrapiApi


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

    def set_value_in_table(self):
        """
        Get value in DTO and update.

        :return:
        """

        dpg.set_value(item='long_name_text', value=self.dto.long_name)
        dpg.set_value(item='short_name_text', value=self.dto.short_name)
        dpg.set_value(item='symbol_text', value=self.dto.symbol)
        dpg.set_value(item='regular_market_price_text', value=self.dto.regular_market_price)
        dpg.set_value(item='regular_market_open_text', value=self.dto.regular_market_open)
        dpg.set_value(item='regular_market_previous_close_text', value=self.dto.regular_market_previous_close)
        dpg.set_value(item='regular_market_day_range_text', value=self.dto.regular_market_day_range)
        dpg.set_value(item='fifty_two_week_high_text', value=self.dto.fifty_two_week_high)
        dpg.set_value(item='fifty_two_week_low_text', value=self.dto.fifty_two_week_low)
        dpg.set_value(item='fifty_two_week_range_text', value=self.dto.fifty_two_week_range)

    def search_stock(self):
        """
        Search stock in brapi

        :return:
        """

        api_stock = BrapiApi(token=settings.brapi_api_token)

        stock = dpg.get_value('input_acao')

        self.dto = api_stock.get_personal_stock(tickers=stock)

        self.set_value_in_table()

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

            dpg.add_input_text(tag='input_acao', width=250, indent=180)

            dpg.add_spacer(height=5)

            dpg.add_button(label='BUSCAR', tag='find_stock', indent=5, callback=self.search_stock)

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
                    dpg.add_text('', tag='long_name_text')

                with dpg.table_row():
                    dpg.add_text('Nome Abreviado: '.upper())
                    dpg.add_text('', tag='short_name_text')

                with dpg.table_row():
                    dpg.add_text('Simbolo: '.upper())
                    dpg.add_text('', tag='symbol_text')

                with dpg.table_row():
                    dpg.add_text('Preço da ação: '.upper())
                    dpg.add_text('', tag='regular_market_price_text')

                with dpg.table_row():
                    dpg.add_text('Preço de abertura: '.upper().upper())
                    dpg.add_text('', tag='regular_market_open_text')

                with dpg.table_row():
                    dpg.add_text('Preço de fechamento: '.upper())
                    dpg.add_text('', tag='regular_market_previous_close_text')

                with dpg.table_row():
                    dpg.add_text('Preço do dia anterior: '.upper())
                    dpg.add_text('', tag='regular_market_day_range_text')

                with dpg.table_row():
                    dpg.add_text('Alta de preço nas ultimas 2 semanas: '.upper())
                    dpg.add_text('', tag='fifty_two_week_high_text')

                with dpg.table_row():
                    dpg.add_text('Baixa de preço nas ultimas 2 semanas: '.upper())
                    dpg.add_text('', tag='fifty_two_week_low_text')

                with dpg.table_row():
                    dpg.add_text('Variação de preço nas ultimas 2 semanas (média): '.upper())
                    dpg.add_text('', tag='fifty_two_week_range_text')
