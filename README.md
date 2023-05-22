# Fumpnews

Api para extrair notícias do site da Fundação Universitária Mendes Pimentel - [FUMP](https://www.fump.ufmg.br/).

## Como executar

Clone o repositório e entre na pasta do projeto.

Crie um ambiente virtual com a ferramenta de sua preferência, aqui vou utilizar o venv.

~~~sh
python3 -m venv venv
~~~
> O ambiente será criado na pasta ***venv***.

Aive o ambiente

~~~ sh
source venv/bin/activate
~~~

Instale as dependências
~~~sh
pip install -r requirements.txt
~~~

## Criando o Banco de dados

Para criar do zero o banco de dados, você deve executar o arquivo ***scrapper.py***.
~~~ sh
python scrapper.py
~~~
> O banco será criado na pasta ***instance***.

## Subindo a API
Para subir a API, basta executar o arquivo ***app.py***.
~~~sh
python app.py
~~~