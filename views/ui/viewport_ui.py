"""UI viewport and main interface"""
#TODO Criar Views para os menus selic e dolar
#TODO Trazer resultado da IA para o menu informações sobre dolar e selic.
#TODO Melhorar informações sobre "primeiro passos"
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
                dpg.add_menu_item(label="Como Usar este software".upper(), callback=self.software_information_popup)

            with dpg.menu(label="Credenciais".upper()):
                dpg.add_menu_item(label="Adicionar".upper(), callback=self.credential_popup)

            with dpg.menu(label="informações".upper()):
                dpg.add_menu_item(label="selic".upper(), callback=self.credential_popup)

                dpg.add_menu_item(label="dolar e euro".upper(), callback=self.credential_popup)

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

        with dpg.window(label="Credenciais", modal=True, show=True, height=200, width=700, pos=(360,260)):

            dpg.add_input_text(label='DIGITE SUA CREDENCIAL DO GOOGLE', tag='google_token')

            dpg.add_input_text(label='DIGITE SUA CREDENCIAL DO BRAPI', tag='brapi_api')

            dpg.add_button(label='SALVAR', tag='save_credentials', callback=self.get_credentials)

    def software_information_popup(self):
        """
        Create a popup for adding software information

        :return:
        """

        with dpg.window(label="COMO USAR ESTE SOFTWARE", modal=True, show=True,height=200, width=700, pos=(360,260)):

            dpg.add_text(
                label='COMO USAR ESTE SOFTWARE'
                      '\n1 - PRIMEIRO COLOQUE SUAS CREDENCIAIS DO GOOGLE E API DE CONSUMO BRAPI.'
                      '\n2 - PESQUISE A AÇÃO QUE QUISER NA AREA DE PESQUISA E ESPERE O RESULTADO.'
                      '\n3 - CASO QUEIRA TROCAR SUAS CREDENCIAIS APENAS ADICIONE NOVAMENTE.',
                tag='information_tag',
                pos=(-400,50),
                show_label=True
            )


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
