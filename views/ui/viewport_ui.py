"""UI viewport and main interface"""
#TODO Fazer janela de informações ditas pela IA sobre ação pesquisada caso não for pesquisada antes mostre algum tipo de erro
import dearpygui.dearpygui as dpg
from config import settings
from controller.ai_google_controller import AiGoogleController

class ViewportUi:

    def get_credentials(self):
        """
        Retrieves the credentials entered by the user.

        :return:
        """
        google_token = dpg.get_value('google_token')

        brapi_api = dpg.get_value('brapi_api')

        settings.google_token = google_token

        settings.brapi_api_token = brapi_api

    def load_information_selic(self):
        """
        Load information for selic.

        :return:
        """

        ai_google = AiGoogleController()

        ai_google.selic_information()

        dpg.set_value(item='information_selic', value=ai_google.dto.selic_rate)

    def load_information_dollar_euro(self):
        """
        Load information for dollar and euro.

        :return:
        """

        ai_google = AiGoogleController()

        ai_google.dollar_euro_information()

        dpg.set_value(item='information_dolar_euro_tag', value=ai_google.dto.dollar_euro)

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
                dpg.add_menu_item(label="selic".upper(), callback=self.selic_window_information)

                dpg.add_menu_item(label="dolar e euro".upper(), callback=self.dolar_euro_window_information)

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
                      '\n2 - PODE COLOCAR SUAS CRENDENCIAIS DENTRO DO PRÓPRIO SOFTWARE OU SETAR NAS VARIAVEIS DE '
                      '\nAMBIENTE DENTRO DO WINDOWS FICA A SUA PREFERENCIA. PARA POR DENTRO DO AMBIENTE DO WINDOWS '
                      '\nCRIE VARAIVEIS COM O SEGUINTE NOME BRAPI_API_TOKEN E COLOCQUE O VALOR, GOOGLE_GEMINI E COLOQUE '
                      '\nO VALOR FAZENDO ISSO O SOFTWARE PARA DE APARECER O POPUP DE CREDENCIAIS.'
                      '\n3 - CASO QUEIRA TROCAR SUAS CREDENCIAIS APENAS ADICIONE NOVAMENTE NA PARTE DE CREDENCIAIS.'
                      '\n4 - COM AS CREDENCAIS TODAS OK UTILIZE O SOFTWARE COMO BEM ENTENDER.',
                tag='information_tag',
                pos=(-400,50),
                show_label=True
            )

    def selic_window_information(self):
        """
        Create information window with selic

        :return:
        """

        with dpg.window(
                label="CARREGANDO INFORMAÇÕES SOBRE A SELIC...",
                modal=True,
                show=True,
                height=700,
                width=900,
                pos=(190,10)
        ):

            dpg.add_text(
                tag='information_selic',
                wrap=890
            )

        self.load_information_selic()

    def dolar_euro_window_information(self):
        """
        Create information window with dolar

        :return:
        """

        with dpg.window(
                label="CARREGANDO INFORMAÇÕES SOBRE O DOLAR E EURO...",
                modal=True,
                show=True,
                height=700,
                width=900,
                pos=(190, 10)
        ):

            dpg.add_text(
                tag='information_dolar_euro_tag',
                wrap=890
            )

        self.load_information_dollar_euro()

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
