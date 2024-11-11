# Engenharia de Atributos

## 1. Remoção de Categorias Irrelevantes em `MS.Zoning`

Identificamos que algumas categorias na variável `MS.Zoning` representam propriedades não-residenciais, o que não é relevante para nosso estudo focado em propriedades residenciais. As categorias removidas foram:

- `C (all)`: Comercial
- `A (agr)`: Agricultura
- `I (all)`: Industrial

## Reclassificação de Categorias em `Sale.Type` e `Sale.Condition`

Após análise, todas as categorias de `Sale.Type` e `Sale.Condition` foram consideradas válidas. No entanto, para melhorar a representatividade e simplificar a análise, realizamos a seguinte reclassificação:

- Agrupamos todos os tipos de escritura de garantia em uma nova categoria chamada `GroupedWD`.
- Mantivemos a categoria `New` como está.
- Agrupamos as demais categorias menos representativas em uma nova categoria chamada `Other`.

## Remoção da Coluna `Street`

A classe `Grvl` na variável `Street` possui baixa representatividade, tornando a variável irrelevante para a análise. Portanto, removemos a coluna `Street` do conjunto de dados.

## Reclassificação das Colunas `Condition.1` e `Condition.2`

Para melhorar a análise das condições dos arredores da casa, realizamos a seguinte reclassificação:

- Agrupamos as categorias de proximidade com a ferrovia (`RRAn`, `RRAe`, `RRNn`, `RRNe`) em `Railroad`.
- Agrupamos as categorias `Feedr` e `Artery` em `Roads`.
- Agrupamos as categorias `PosA` e `PosN` em `Positive`.

### Consolidação das Condições em uma Única Coluna

Com essas reclassificações, combinamos as colunas `Condition.1` e `Condition.2` em uma única coluna categórica chamada `Condition`, com as seguintes categorias:

- `Norm`: Quando `Condition.1` é `Norm`.
- `Railroad`: Quando `Condition.1` é `Railroad` e `Condition.2` é `Norm`.
- `Roads`: Quando `Condition.1` é `Roads` e `Condition.2` não é `Railroad`.
- `Positive`: Quando `Condition.1` é `Positive`.
- `RoadsAndRailroad`: Quando (`Condition.1` é `Railroad` e `Condition.2` é `Roads`) ou (`Condition.1` é `Roads` e `Condition.2` é `Railroad`).

## Transformação de Colunas com Muitos Valores Ausentes (`Misc.Feature` e `Alley`)

As colunas `Misc.Feature` e `Alley` contêm muitos valores ausentes. Criamos novas variáveis binárias para indicar a presença de um barracão (`shed`) e de um acesso a beco (`alley`), respectivamente.

### 1. Transformação de `Misc.Feature` para `HasShed`

Transformamos a coluna `Misc.Feature` em `HasShed`, indicando se a casa possui um barracão (`shed`). Definimos `HasShed` como `True` quando `Misc.Feature` possui o valor `Shed` e `False` nos demais casos.

### 2. Transformação de `Alley` para `HasAlley`

Transformamos a coluna `Alley` em `HasAlley`, indicando se a casa possui acesso a um beco (`alley`). Definimos `HasAlley` como `True` para casas onde `Alley` não é nulo, e `False` nos demais casos.

## Consolidação e Reclassificação dos Revestimentos Externos

Para melhorar a representatividade e simplificar a análise das variáveis de revestimento externo (`Exterior.1st` e `Exterior.2nd`), realizamos as seguintes transformações:

Padronizamos algumas categorias em `Exterior.2nd` e agrupamos materiais externos menos representativos em uma nova categoria chamada `Other`. Consolidamos a informação de revestimento externo em uma única variável chamada `Exterior`, mantendo apenas a primeira coluna (`Exterior.1st`) e removendo ambas as colunas originais após a transformação.

## Remoção da Coluna `Heating` por Baixa Variabilidade

A coluna `Heating` possui baixa variabilidade, fornecendo pouca informação útil para a análise. Optamos por descartá-la.

## Ajustes nas Colunas `Roof.Matl` e `Roof.Style`

Removemos a coluna `Roof.Matl` devido à baixa representatividade das categorias menores. Na coluna `Roof.Style`, agrupamos categorias menores em `Other` para simplificar a análise.

## Ajustes na Coluna `Mas.Vnr.Type`

Agrupamos as categorias menores `BrkCmn` e `CBlock` em `Other` na coluna `Mas.Vnr.Type`. Valores ausentes foram adicionados à categoria `None`.

## Simplificação da Coluna `MS.SubClass`

Reagrupamos as categorias menos representativas em `MS.SubClass` em uma nova categoria chamada `Other`.

## Agrupamento de Categorias Menores na Coluna `Foundation`

Agrupamos categorias com baixa representatividade na coluna `Foundation` em `Other`.

## Remoção de Categorias com Baixa Representatividade na Coluna `Neighborhood`

Optamos por remover linhas correspondentes a bairros com baixa representatividade na coluna `Neighborhood`, como:

- Blueste
- Greens
- GrnHill
- Landmrk

## Criação da Categoria `NoGarage` na Coluna `Garage.Type`

Criamos a categoria `NoGarage` na coluna `Garage.Type` para representar residências sem garagem.

## Remoção da Coluna `Utilities` por Baixa Representatividade

Removemos a coluna `Utilities` devido à baixa representatividade.

## Remoção da Coluna `Pool.QC` por Quantidade Elevada de Valores Ausentes

Removemos a coluna `Pool.QC` devido à alta quantidade de valores ausentes e baixa variabilidade.

## Tratamento da Coluna `Fence` para Representar Ausência de Cerca

Criamos a categoria `NoFence` na coluna `Fence` para representar residências sem cerca, atribuindo valores ausentes a essa nova categoria.

## Remoção da Coluna `Fireplace.Qu` devido à Redundância e Alta Ausência de Dados

Removemos a coluna `Fireplace.Qu` devido à redundância com a coluna `Fireplaces` e alta quantidade de valores ausentes.

## Ajustes nas Colunas de Condição e Acabamento da Garagem

Transformamos `Garage.Finish` de uma variável ordinal para nominal, criando a categoria `NoGarage` para valores ausentes.

## Tratamento da Coluna `Electrical` para Preenchimento de Valor Ausente

Preenchemos o único valor ausente na coluna `Electrical` com a categoria `SBrkr`.

## Tratamento de Valores Ausentes nas Colunas do Porão (`Bsmt.Exposure`, `Bsmt.Qual`, `Bsmt.Cond`, `BsmtFin.Type.1`, `BsmtFin.Type.2`)

Criamos a categoria `NA` para valores ausentes nas colunas do porão e as transformamos em variáveis nominais.

## Transformação da Coluna `SalePrice` para Logaritmo de Base 10

Transformamos a variável `SalePrice` usando o logaritmo de base 10 para normalizar a distribuição dos preços.

## Imputação de Valores Ausentes em `Lot.Frontage`

Imputamos os valores ausentes de `Lot.Frontage` com a mediana dessa variável.

## Correção e Imputação da Idade da Garagem (`Garage.Yr.Blt`)

Corrigimos inconsistências na variável `Garage.Yr.Blt` e imputamos valores ausentes com a mediana da idade da garagem.

## Transformação das Variáveis `Year.Remod.Add` e `Year.Built` para Idade

Transformamos as variáveis `Year.Remod.Add` e `Year.Built` para representar a idade do imóvel no momento da venda.

## Imputação de Valores Ausentes na Coluna `Mas.Vnr.Area`

Imputamos os valores ausentes na coluna `Mas.Vnr.Area` com zero, indicando a inexistência de revestimento.

