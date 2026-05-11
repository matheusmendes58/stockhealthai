"""UI viewport and main interface"""

import dearpygui.dearpygui as dpg
from config import settings

class ViewportUi:

    def screen_viewport(self):
        """"
        Viewport screen software

        :return:
        """

        dpg.create_viewport(title="StockHealth AI", width=1280, height=720)

        with dpg.viewport_menu_bar():
            with dpg.menu(label="Primeiro passos".upper()):
                dpg.add_menu_item(label="Como Usar este software".upper(), callback=self.credential_popup)

            with dpg.menu(label="Credenciais".upper()):
                dpg.add_menu_item(label="Adicionar".upper(), callback=self.credential_popup)

        self.warning_popup()

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

    def credential_popup(self):
        """
        Create a popup for adding credentials in software

        :return:
        """

        with dpg.window(label="Credenciais", modal=True, show=True,height=200, width=700):

            dpg.add_input_text(label='DIGITE SUA CREDENCIAL DO GOOGLE', tag='google_token')

            dpg.add_input_text(label='DIGITE SUA CREDENCIAL DO BRAPI', tag='brapi_api')

            dpg.add_button(label='SALVAR', tag='save_credentials', callback=self.get_credentials)

    def warning_popup(self):
        """
        Warning if you are without credentials.

        :return:
        """

        if not settings.env_check():

            with dpg.window(label="Credenciais", modal=True, show=True, height=100, width=500, pos=(360,260)):
                dpg.add_text(
                    label='SOFTWARE SEM CREDENCIAIS ADICIONE NO MENU CREDENCIAIS | ADICIONAR',
                    show_label=True,
                    pos=(-320,50)
                )

    def get_credentials(self):
        """
        Retrieves the credentials entered by the user.

        :return:
        """
        google_token = dpg.get_value('google_token')

        brapi_api = dpg.get_value('brapi_api')

        settings.google_token = google_token

        settings.brapi_api_token = brapi_api



