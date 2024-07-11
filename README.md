
Projeto de Raspagem de Dados - Zelt Imóveis
Este projeto contém scripts para raspagem de dados do site da Zelt Imóveis. Ele busca por apartamentos disponíveis para aluguel, filtrados de acordo com parâmetros específicos, e gera um arquivo CSV com os detalhes dos imóveis encontrados.

Parâmetros de Busca
Os parâmetros de busca são definidos na classe DadosEmissao e incluem:

Número de Quartos: 1 ou mais
Tipo de Contrato: Aluguel
Valor Máximo: 1800 reais
Dados Gerados
O script gera um arquivo CSV com as seguintes informações sobre os imóveis encontrados:

Endereço
Tamanho (em metros quadrados)
Quantidade de Quartos
Quantidade de Suítes
Quantidade de Banheiros
Preço
Tipo de Contrato
Tipo do Imóvel
Requisitos
Python 3.10.2 ou superior
Docker (opcional, para execução via contêiner)

Instalação e Execução

Executar o Script Diretamente
Instale as dependências:
pip install -r requirements.txt

Execute o script:
python3 main.py

Executar com Docker Compose
Construa e inicie os serviços definidos no docker-compose.yml:
docker-compose up --build

Estrutura do Projeto
project-root/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── main.py
├── base/
│   └── DadosEmissao.py
├── scripts/
│   └── emissor.py
└── csv/
    └── (arquivos CSV gerados)

