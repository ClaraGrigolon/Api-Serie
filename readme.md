# API de Series - WebAPI

Está é uma API RESTful desenvolvida para o gerenciamento de informações de series, utilizando **Python.py** e **Express**. A API permite criar, ler, atualizar e excluir series, com validação dos dados utilizando a biblioteca **Joi**.

Este é um projeto inicial de CRUD (Create, Read, Update, Delete),que será expandido no futuro. Este é apenas o escopo inical.

## Funcionalidades

- **GET /**: Retorna a lista completa de series.
- **GET /:id**: Retorna as informações de uma serie especifica, identificada pelo id
- **GET /:titulo**: Retorna as informações de uma serie especifica, identificada pelo titulo
- **POST /**: Adiciona uma nova serie à lista.
- **PUT /:id**: Atualiza as informações de uma serie especifica, identificada pelo id.
- **DELETE /:id**: Remove uma serie especifica pelo id.

## Estrutura do Projeto

- **app.py**: Arquivo principal que configura o servidor Express e as rotas da API.
- **series.db**: Contém a lista de series (dados fictícios).
- **validacao.py**: Contém as validações Joi para os dados das series.

## Endpoints

### 1. **GET /**

Retorna a lista completa de series disponíveis.

#### Exemplo de Resposta:

```json
[
    {
        "id": 1,
        "titulo": "Supernatural",
        "elenco": "Jensen Ackles, Jared Padalecki, Misha Collins",
        "lancamento": "2005",
        "genero": "Drama"
    },
    {
        "id": 3,
        "titulo": "How I Met Your Mother",
        "elenco": "Josh Radnor, Neil Patrick Harris, Cobie Smulders, Alyson Hannigan, Jason Segel",
        "lancamento": "2005",
        "genero": "Sitcom"
    }
]
```
### 2. **GET /:id**

Retorna as informações de um serie especifica, identificada pelo id.

### Exemplo de Requisição:

`GET /1`

### Exemplo de Resposta:

```json
{
    "id": 1,
    "titulo": "Supernatural",
    "elenco": "Jensen Ackles, Jared Padalecki, Misha Collins",
    "lancamento": "2005",
    "genero": "Drama"
}
```

### 3. **GET /:titulo**

Retorna as informações de um serie especifica, identificada pelo titulo.

### Exemplo de Requisição:

`GET /Supernatural`

### Exemplo de Resposta:

```json
{
    "id": 1,
    "titulo": "Supernatural",
    "elenco": "Jensen Ackles, Jared Padalecki, Misha Collins",
    "lancamento": "2005",
    "genero": "Drama"
}
```
### 3. **POST /**

Adiciona uma nova serie à lista.

#### Exemplo de Requisição:

`POST \`

**Content-Type:** application/json

```json
{
    "titulo": "Supernatural",
    "elenco": "Jensen Ackles, Jared Padalecki, Misha Collins",
    "lancamento": "2005",
    "genero": "Drama"
}
```

#### Exemplo de Resposta:

```json
{
    "id": 1,
    "titulo": "Supernatural",
    "elenco": "Jensen Ackles, Jared Padalecki, Misha Collins",
    "lancamento": "2005",
    "genero": "Drama"
}
```

### 4. **PUT /:id**

Atualiza as informações de uma serie específica.

#### Exemplo de Requisição:

`PUT /1`

**Content-Type:** application/json

```json
{
    "lancamento": "2004"
}
```

#### Exemplo de resposta:

```json
{
    "id": 1,
    "titulo": "Supernatural",
    "elenco": "Jensen Ackles, Jared Padalecki, Misha Collins",
    "lancamento": "2004",
    "genero": "Drama"
}
```

### 5. **DELETE /:id**

Remove uma serie específica pelo id.

#### Exemplo de Requisição:

`DELETE /1`

#### Exemplo de Resposta:

```json
{
    "id": 3,
    "titulo": "How I Met Your Mother",
    "elenco": "Josh Radnor, Neil Patrick Harris, Cobie Smulders, Alyson Hannigan, Jason Segel",
    "lancamento": "2005",
    "genero": "Sitcom"
}
```

## Como Rodar o Projeto

1. **Clone este repositório:**

  ```bash
  git clone https://github.com/ClaraGrigolon/Api-Serie
  ```

2. **Instale as dependências:**

  Navegue até o diretório do projeto e execute o comando:

  ```bash
  pip install flask flask-sqlalchemy
  ```
3. **Inicie o servidor**
  Após a instalação das dependências, inicie o servidor:

  ```bash
  python app.py
  ```

4. **Acesse a API**

A API está disponível em (http://127.0.0.1:5000/Serie)

## Validações 

Os dados enviados para API são validados com **Joi** para garantir que todos os campos sejam fornecidos corretamente. As validações incluem:

- O titulo, elenco, genero e lancamento da serie devem ter pelo menos 1 caracter.
- Durante a atualização, pelo menos um campo precisa ser fornecido.

## Autores

Desenvolvido por:
    Ana Clara Grigolon Dutra Rosa
    Davi Furlan Pereira
