# Prompt AI

class PromptIA:
    """
    This class is just about PROMPT AI
    """

    def __init__(self, data_text: str = None):
        self.data_text = data_text

        self.prompt_google = f"""
        Você é um analista financeiro especialista em ações da bolsa de valores. Analise os dados da ação abaixo e 
        indique se é uma boa opção para investimento se ação está com boa saúde e indique também o quanto de redimento e
        últimos dividendo pagos pela empresa. Se possivel também traga um olhar atual do mercado financeiro e do mundo
        e mostre se está ação irá ter lucro ou irá trazer prejuizo para mim. 
         
        Dados financeiros:

        {self.data_text}                

        """

        self.prompt_google_currency = f"""
        Você é um analista financeiro especialista traga a cotação atual do dolar e do
        euro e uma breve explicação do porque o aumento e ou baixa da moeda.
        
        """

        self.prompt_google_selic = f"""
        Você é um analista financeiro especialista traga o valor atual da taxa selic e uma breve explicação sobre o por que
        deste valor atual.

        """