import csv
import os
import unicodedata
from bs4 import BeautifulSoup
import requests
from base.Dados_emissao import DadosEmissao
from utils.Logger import Logger


class Emissor():
    def __init__(self, dados: DadosEmissao):
        self.dados = dados
        self.url_base = "https://www.zelt.com.br"
    
    def seta_headers(self):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36"
        }
        return headers
    
    def retorna_imoveis(self):
        """
        Esta função retorna os elementos HTML com as informações dos imoveis.
        """
        try:
            headers = self.seta_headers()
            url = f"https://www.zelt.com.br/imoveis/para-{self.dados.tipo_contrato}/\
                {self.dados.tipo}?quartos={self.dados.quartos}+&preco-de-locacao=\
                {self.dados.valor_min}~{self.dados.valor_max}&ordenar=menor-valor"
            
            request = requests.get(url, headers=headers)
            resposta = request.text
            html = BeautifulSoup(resposta, 'html.parser')

            imoveis = html.select('[class="card-with-buttons borderHover"]')
            Logger.debug(f'Encontrados: {len(imoveis)}')

            return imoveis
        except Exception as e:
            Logger.erro(f'Ocorreu um erro ao extrair imoveis do site.\n {e}')

    def extrai_dados_imoveis(self,imoveis):
        """
        Esta função é encarregada de gerar o CSV com as colunas correspondentes, no diretório /csv
        """
        try:
            csv_path = os.path.join( os.path.join(os.getcwd(), 'csv') , 'imoveis.csv')
            with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([
                    'Endereço', 'Tamanho (m²)', 'Quartos', 'Suítes', 
                    'Banheiros', 'Vagas', 'Preço', 'Tipo Contrato', 'Tipo Imóvel'
                ])
                for card in imoveis:
                    endereco = card.find('h2').get_text(strip=True) if card.find('h2') else 'Sem Endereço'
                    ul = card.select_one('div.card-with-buttons__footer > div:nth-child(1) > ul')
                    detalhes = ul.find_all('li') if ul else []
                    tamanho = detalhes[0].get_text(strip=True) if len(detalhes) > 0 else 'N/A'
                    quartos = detalhes[1].get_text(strip=True) if len(detalhes) > 1 else 'N/A'
                    suites = detalhes[2].get_text(strip=True) if len(detalhes) > 2 else 'N/A'
                    banheiros = detalhes[3].get_text(strip=True) if len(detalhes) > 3 else 'N/A'
                    vagas = detalhes[4].get_text(strip=True) if len(detalhes) > 4 else 'N/A'
                    preco = card.select_one('div.card-with-buttons__container-footer > div > div > p.card-with-buttons__value').get_text(strip=True) if card.select_one('div.card-with-buttons__container-footer > div > div > p.card-with-buttons__value') else 'N/A'
                    writer.writerow([
                        endereco, tamanho, quartos, suites, banheiros, vagas, preco,
                        self.dados.tipo_contrato, self.dados.tipo
                    ])
            Logger.sucesso("Dados extraídos com sucesso!")
        except Exception as e:
            Logger.erro(f"Ocorreu um erro ao extrair dados dos imoveis para o CSV!\n {e}")

    def iniciar_busca(self):
        """
        Essa função executa todas as outras, unificando-as.
        """
        Logger.debug("Parâmetros de busca:")
        for key, value in self.dados.__dict__.items():
            Logger.debug(f"{key}: {value}")        

        imoveis = self.retorna_imoveis()
        self.extrai_dados_imoveis(imoveis)