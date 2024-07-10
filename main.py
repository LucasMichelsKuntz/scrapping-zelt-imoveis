from base.Dados_emissao import DadosEmissao
from scripts.emissor import Emissor
from utils.Logger import Logger

if __name__ == "__main__":
    try:
        Logger.debug("Iniciando extração dos dados...")
        dados_emissao = DadosEmissao()
        emissor = Emissor(dados_emissao)
        emissor.iniciar_busca()
        
    except Exception as e:
        Logger.erro('Erro ao extrair dados do site. Seguem dados para teste:\n')
        Logger.erro(emissor.dados)
        Logger.erro(e)
    