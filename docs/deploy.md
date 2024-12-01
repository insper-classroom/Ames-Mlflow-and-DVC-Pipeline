# Deploy do Modelo

Este projeto utiliza a AWS para o deploy do modelo. A arquitetura do sistema está ilustrada na figura abaixo:

![Organização do projeto](img/aws_infra.jpeg)

## Funcionamento do Sistema

Um cliente, como um funcionário de uma corretora de imóveis, utiliza uma interface gráfica (um site, por exemplo) para enviar os parâmetros necessários. Esses parâmetros são enviados ao **gateway da API**, que os direciona para o **AWS Lambda**. O Lambda realiza a predição e:

1. Armazena o resultado no **Amazon S3**.
2. Envia os logs para o **CloudWatch**, permitindo monitoramento e análise.

## Gerenciamento de Experimentos

Para o versionamento dos experimentos e acompanhamento do progresso, foi utilizado o **MLFlow**. Ele permite:

- Armazenar os resultados de experimentos em um banco de dados SQL.
- Armazenar os artefatos dos experimentos no **Amazon S3**.
- Visualizar os experimentos por meio de sua interface gráfica, como mostrado na imagem abaixo:

![Visualização do MLFlow](img/infra.jpeg)

Essa estrutura garante rastreabilidade, monitoramento eficiente e facilidade de uso para o cliente final. Os experimenros armazenados e modelos guardados podem ser vistos na interface grafica do mlflow como mostrado na imagem abaixo:
![Visualização do MLFlow](img/Mlflow.png)

## Versionamento de Dados - DVC

Para o versionamento dos dados, foi utilizado o **DVC**. Ele permite:

- Armazenar os dados diretamente no **Amazon S3**.
- Controlar versões dos dados utilizados para os modelos.
- Os dados rastreados são os do dataset ames.csv, que é baixado da API do Ames Housing.
- O remote utilizado é o S3 esta configurado a partir do dvc/config na url = s3://dvc-project-rodrigoap8

![Visualização do DVC](img/dvc.jpeg)

Essa estrutura garante rastreabilidade, monitoramento eficiente e facilidade de uso para o cliente final.

### Pipeline de Dados

Foi criado um pipeline de dados utilizando o **DVC**, que é executado periodicamente para garantir que o modelo esteja sempre atualizado. O pipeline está descrito no arquivo `dvc.yaml` e possui as seguintes etapas:

1. Baixar os dados da API do Ames Housing e executar todas as transformações necessárias.
2. Dividir os dados em treino e teste.
3. Treinar o modelo.
4. Avaliar o modelo.
5. Buildar o Docker para deploy.
6. Ativar o logging na AWS.
7. Taguear a imagem do Docker.
8. Fazer o push da imagem para o ECR.
9. Deletar o gateway antigo, para evitar conflitos.
10. Deletar o Lambda antigo, para evitar conflitos.
11. Criar a nova Lambda function.
12. Criar o novo gateway.

Essa abordagem automatiza o processo, garantindo eficiência e consistência no gerenciamento dos dados e na atualização do modelo.
