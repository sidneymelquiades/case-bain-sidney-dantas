
#  Predict Chilean Property Price API - Bain & Company Case

# Autor Sidney Dantas

Esta API foi desenvolvida como solução para um case proposto pela Bain & Company, com o objetivo de prever o preço de imóveis — casas e departamentos — na região metropolitana de Santiago, no Chile, com base em características físicas e na localização geográfica.

A proposta foi resolvida de forma prática, adotando uma abordagem simples e introdutória. No entanto, é importante destacar que, para uma aplicação em um cenário real, seriam necessárias diversas melhorias e aprimoramentos na arquitetura e nos processos envolvidos.


---

## Objetivo

Receber informações sobre um imóvel (como tipo, setor, área, número de cômodos, latitude e longitude) e retornar uma previsão de preço com base em um modelo de machine learning previamente treinado.

---

##  Como executar a API

### Pré-requisitos

- Python 3.9 ou superior
- Docker 

### 1. Clone o repositório

```bash
git clone https://github.com/sidneymelquiades/case-bain-sidney-dantas.git
cd case-bain-sidney-dantas
```

### 2. build a aplicação

```bash
docker build -t case-bain .
```

### 3. Rode a aplicação via docker

```bash
docker run -p 8000:8000 minha-api-fastapi

```
##  Autenticação

Para utilizar os endpoints da API, é necessário enviar uma `API Key` válida no header da requisição:

```
Key: api_key
Value: supersecretkey
```

Chaves disponíveis (definidas via arquivo `config.yaml`):

```yaml
api_keys:
  - key: "supersecretkey"
  - key: "outrachave123"
```

---

##  Input - Esquema `PropertyInput`

```json
{
  "type": "casa",
  "sector": "nunoa",
  "net_usable_area": 80.0,
  "net_area": 100.0,
  "n_rooms": 3,
  "n_bathroom": 2,
  "latitude": -33.45,
  "longitude": -70.65
}
```

###  Validações e Premissas:

Algumas premissas foram adotadas com o objetivo de garantir um grau mínimo de confiabilidade nas previsões geradas pelo modelo. São elas:

A variável type deve conter apenas os valores "departamento" ou "casa", restringindo a análise a esses dois tipos de imóvel(conforme arquivo transmitido). A variável sector deve corresponder a um dos seguintes bairros: Vitacura, La Reina, Las Condes, Lo Barnechea, Providencia ou Ñuñoa, garantindo assim que o modelo trabalhe apenas com regiões bem definidas dentro do escopo do projeto. As variáveis net_usable_area e net_area, que representam áreas úteis e totais do imóvel, respectivamente, devem possuir valores maiores que zero, evitando registros inconsistentes ou inválidos. A variável latitude deve estar compreendida entre -34 e -30, enquanto a variável longitude deve estar entre -73 e -68, limitando os dados a uma faixa geográfica coerente com a área urbana considerada para o estudo.

- `type`: apenas "departamento" ou "casa"
- `sector`: um dos seguintes bairros:
  - vitacura, la reina, las condes, lo barnechea, providencia, nunoa
- `net_usable_area` e `net_area`: devem ser > 0
- `latitude`: entre -34 e -30
- `longitude`: entre -73 e -68

---

##  Output - Esquema `PredictionOutput`

```json
{
  "price": 123456789.0
}
```

---

##  Documentação Swagger

Acesse a interface interativa da API:

- [http://localhost:8000/docs](http://localhost:8000/docs)

---

##  Modelo de Machine Learning



O modelo foi treinado utilizando um pipeline que é composto pelas seguintes etapas:

Primeiramente, realiza-se o pré-processamento dos dados, que inclui a codificação das variáveis categóricas e a limpeza dos dados para garantir a qualidade e consistência das informações.

Em seguida, é aplicado um regressor do tipo Gradient Boosting, que é um algoritmo de aprendizado de máquina utilizado para regressão, baseado na combinação de múltiplos modelos fracos para formar um modelo forte.

Para avaliar o desempenho do modelo, são utilizadas métricas como o Erro Quadrático Médio (RMSE), o Erro Médio Absoluto (MAE) e o Erro Percentual Absoluto Médio (MAPE), que permitem medir a precisão e a qualidade das previsões geradas.

Todo esse processo está organizado em scripts localizados no arquivo `pipeline/train.py` e configurados por meio do arquivo de configuração `pipeline/config.yaml`.


---


---

##  Futuras Evoluções

O case previa uma solução simples e introdutória, porém seria bastante recomendável evoluir a arquitetura do projeto, incorporando uma esteira de CI/CD utilizando ferramentas como Jenkins e Spinnaker, por exemplo. Isso permitiria que o retreinamento da aplicação fosse realizado de forma menos burocrática e mais eficiente
---

##  Autor

- **Sidney Melquiades Dantas**
- [sidneymelquiadesdantas@gmail.com](mailto:sidneymelquiadesdantas@gmail.com)
- [github.com/sidneymelquiades](https://github.com/sidneymelquiades)
- [Linkedin](https://www.linkedin.com/in/sidneymelquiadedantas/)

---
