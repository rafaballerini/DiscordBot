# BALLE BOT

## Introdução

Esse é um projeto para criar o próprio bot de discord para o servidor da Rafella Ballerini, e aqui estão (até agora) algumas anotações sobre como montar o bot.

<img src="/assets/gif_balle_bot.gif" >

## Techs

Confome desenvolvemos o projeto, atualizar quais tecnologias estamos utilizando

* [Python](https://www.python.org/): Linguagem de programação de sintaxe simples;
* [Mongodb](https://www.mongodb.com/): Bando de dados não relacional para armazenamento de informações, está sendo utilizado o banco diretamente no site;
* [Discord Developer Portal](https://discord.com/developers/applications): site para registrar sua aplicação/bot;
* [Discord.py](https://discordpy.readthedocs.io/en/latest/): Biblioteca para integração com o discord;

## Requisitos

* Ter instalado Python na versão 3.5 (durante o desenvolvimento, começamos na versão 3.5, então não podemos garantir que versões anteriores funcionem);
* Crie um arquivo Token.py, preencha com os seguintes dados:
```py
class TokenDiscord:
  def uploadToken():
    return {
      "database": "Link de conexão ao mongodb",
      "idapresentacao":"é um long que representa o id de um dos canais onde vai ter pontos por reações",
      "idaviso":"é um long que representa o id de um dos canais onde vai ter pontos por reações",
      "token":"token de acesso do bot, gerado no site do Discord Developer Portal"
    }

```

## GAMIFICAÇÃO

A gamificação do bot é feita através de 2 tipos, a xp e níveis, o xp é dividido em semanal e por canal, os níveis são calculados de forma geral;

### XP

O cálculo do xp vai seguir essas regras:
* Por mensagem:
  * Mínimo de 2 palavras;
  * Máximo por mensagem, 40 pontos;
  * Número de caracteres não repetidos / 3;
* Reações a mensagens:
  * Disponíveis em alguns canais;
  * Badlist de emojis, remove pontos, 200 pontos, remove a reação;
  * Goodlist de emojis, 5 emojis, 2x pontos, 100 pontos base;
* Tempo de canais de voz:
  * Conferir quais informações recebemos para avaliar os pontos
* Compartilhamento de tela:
  * Conferir quais informações recebemos para avaliar os pontos


#### pymongo operações

Essas informações que estão sendo mostradas é apenas para enteder como deve ser utilizado o pymongo

* **Insert**
```py
data = {
  'nome': 'Jef',
  'idade': 45
}

responseData = collection.insert_one(data)
# responseData é do tipo InsertOneResult, só vi que tem o inserted_id até agora
```
[Infos sobre InsertOneResult](https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.InsertOneResult)

* **Replace**
```py
data = {
  'nome': 'Jef',
  'idade': 45
}

responseData = collection.replace_one({'nome': 'Mateus'}, data)
# responseData é do tipo UpdateResult, só vi que tem matched_count,modified_count e upserted_id de informações relevantes
```
[Infos sobre UpdateResult](https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.UpdateResult)

* **Update**
```py

responseData = collection.update_one({'nome': 'Mateus'}, {'$inc': {'idade': 2}}, upsert)
# responseData é do tipo UpdateResult, só vi que tem matched_count,modified_count e upserted_id de informações relevantes
# incrementa o valor idade em 2
# upsert é um valor booleano, que vai definir se é necessário inserir o objeto ou não
```
[Infos sobre UpdateResult](https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.UpdateResult)
* Outros operadores interessantes:
  * $set: vai definir um valor específico
  * $mul: vai múltiplicar a propriedade pelo valor especificado
  * $rename: vai trocar o campo
  * $setOnInsert: se a query não resultar em nada, e o objeto tiver que ser inserido, adiciona os campos
  * $unset: remove o campo
* Para arrays:
  * $: atualiza o primeiro que encontrar na condição
  * $[]: atualiza todos os elementos encontrados
  * $[\<identifiers\>]: atualiza todos que combinarem com a condição dentro do parênteses

[Infos sobre Update Operators](https://docs.mongodb.com/manual/reference/operator/update/#std-label-update-operators)


* **update_many**
```py
responseData = collection.update_many(
    {'valor': 10}, {'$set': {'teste2':'novo'}})
# procura todo lugar onde valor é igual a 10, e altera/adiciona o campo teste2 = novo
```
[Infos sobre UpdateResult](https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.UpdateResult)
