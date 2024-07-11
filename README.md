Este projeto contém scripts para raspagem de dados do site da Zelt Imovéis.

Em primeiro momento, foram parametrizados dados base para as requisições, na classe DadosEmissao. Porém, caso necessário pode ser parametrizável.
Busca por apartamentos que contenham:
. 1 Quartos +;
. Tipo de contrato para aluguel;
. valor máximo de 1800 reais.

É gerado um CSV com:
. Endereço;
. Tamanho em metros quadrados;
. Quantidade de quartos;
. Quantidade de suítes;
. Quantidade de banheiros;
. Preço;
. Tipo contrato;
. Tipo do imovél.

Para rodar o script basta instalar as dependências e utilizar o comando python3 main.py (É necessário o python 3.10.2+), ou buildar e rodar o docker-compose,
que utiliza volumes para transporte do CSV para fora do contâiner.
