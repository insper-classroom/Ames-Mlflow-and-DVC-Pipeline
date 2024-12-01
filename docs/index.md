# MLOps Project

Projeto da disciplina de MLOps do curso de Engenharia da Computação do Insper.

## Grupo

- Arthur Barreto
- Rodrigo Patelli

## Vídeo do Projeto

O vídeo do projeto pode ser encontrado [aqui](https://youtu.be/s1CFCVYezjc).

## Objetivo

O projeto consiste em escolher um projeto de Machine Learning já existente e aplicar os conceitos vistos em aula, como CI/CD, testes, monitoramento, entre outros.

Como projeto base, foi escolhido o **Ames Housing Dataset**, que consiste em um dataset com informações sobre casas e seus preços de venda. Na eletiva de **Machine Learning**, foi desenvolvido o modelo de predição deste dataset, e agora, na eletiva de **MLOps**, será feita a aplicação dos conceitos de MLOps.

O professor da eletiva de **Machine Learning** disponibilizou a análise exploratória, disponível [aqui](https://github.com/FabioAyresInsper/ames). O projeto desenvolvido pode ser encontrado [aqui](https://github.com/AntonioAEMartins/projeto1-ml-ames.git), que será o projeto base para este trabalho.

## Organização do Projeto

Dentro da pasta `notebooks`, estão os notebooks utilizados para a análise exploratória, feature engineering e treinamento do modelo, desenvolvidos originalmente como parte do projeto de Machine Learning. Para a etapa de MLOps, foi criada a pasta `src`, onde estão os scripts que separam as responsabilidades de cada etapa do projeto, evitando a necessidade de um único notebook extenso para realizar todas as tarefas. A pasta `docs` contém a documentação em formato mkdocs.

## Documentação

A documentação foi dividida em algumas seções, sendo elas:

- **Base de dados**: descrição do dataset utilizado, com informações sobre as features e a variável alvo `preço de vendas` [data](data.md).
- **Feature Engineering**: descrição das transformações feitas nas features do dataset [feature-engineering](engineering.md).
- **Modelo**: descrição do modelo utilizado, com informações sobre a escolha do modelo, treinamento e métricas de avaliação [model](model.md).
- **Deploy**: descrição do deploy do modelo, bem como as melhorias no âmbito de MLOps [deploy](deploy.md).

## Utilização

### Utilizando a infraestrutura ja pronta na aws

Este projeto já possui uma infraestrutura pronta na aws, com as instâncias já ativas, caso deseje testá-las e obter predições basta executar o arquivo `aws_utils/test_gatway.py`, este arquivo já possui um dicionário pré-definido contendo os valores das features, que pode ser alterado como desejar, basta rodar o arquivo e obter a predição.

```bash
python aws_utils/test_gateway.py
```

### Criando o modelo e subindo a infraestrutura por conta própria

Para utilizar e construir a infraestrutura o projeto siga os passos abaixo:

1. Para rodar o projeto, é necessário instalar as dependências listadas no arquivo `requirements.txt`. Para isso, execute o comando abaixo:

```bash
pip install -r requirements.txt
```

2. Também é imprtante criar um arquivo `.env` na raiz do projeto, seguindo o arquivo .env.example disponibilizado na raiz do projeto.

3. Em seguida, é necessrário inciar o mlflow server, para isso, basta rodar o comando:

```bash
mlflow server --backend-store-uri postgresql://postgres:7F3x2D5fa29Emd@mlflow.cgtdf7yvdtuk.us-east-2.rds.amazonaws.com:5432/mlflow_project_rodrigoap8 --default-artifact-root s3://mlflow-exp-tracking-rodrigoap8
```

4. Antes de de fato realizar a execução da pipeline, é necessário também possuir a Docker Engine instalada e rodando.

5. Para executar a pipeline de treinamento e deploy do modelo usando o DVC, utilize o comando:

```bash
dvc repro
```

### Observações

- Caso deseje utilizar suaps próprias instancias na aws, altere os comandos da pipeline dvc em `dvc.yaml` para apontar para suas instâncias.
