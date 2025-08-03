# Property-Friends Real Estate API

> Projeto fictício para estimar valores de imóveis residenciais no Chile usando ML.

---

## Sobre o projeto

Esse projeto surgiu para atender um cliente do setor imobiliário no Chile, que precisava de uma solução rápida para estimar preços de imóveis residenciais. O objetivo foi pegar um modelo já treinado e transformar ele numa solução produtiva, com uma API que permite receber dados do imóvel e retornar a estimativa de preço.

Além disso, desenvolvemos um pipeline para re-treinamento automático do modelo, usando arquivos CSV de treino e teste, para garantir que o sistema possa evoluir.

---

## O que tem aqui

- API REST em FastAPI para fazer previsões de preço de imóvel.
- Endpoint para re-treinamento do modelo enviando arquivos CSV.
- Sistema simples de autenticação via API Key.
- Logs para monitorar predições e treinamentos.
- Documentação automática via Swagger.
- Código modular e organizado para facilitar manutenção e evolução.
- Dockerfile para rodar a aplicação em container facilmente.

---

## Como rodar

### Pré-requisitos

- Python 3.9 ou superior
- Docker (recomendado para deploy em produção)

#### Contato

- Sidney Dantas
- Email: <sidneymelquiadesdantas@gmail.com>
- GitHub: github.com/sidneymelquiades


### to-do's

- criar camada de testes com pytest (testar)

- melhorar read me

- criar github e não esquecer de suprimir a data do cliente

- passar tudo por linter e rever comentarios e etc

- testar docker de tudo e ver como esta funcionado

- traduzir tudo para inglês