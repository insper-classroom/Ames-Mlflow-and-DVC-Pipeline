# MLOps Project

Projeto da disciplina de MLOps do curso de Engenharia da Computação do Insper.

## Grupo

- Arthur Barreto
- Rodrigo Patelli

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
