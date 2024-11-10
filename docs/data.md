# Ames Housing Dataset - Documentação Completa

## Visão Geral

Este dataset contém informações detalhadas sobre propriedades residenciais vendidas em Ames, Iowa, entre 2006 e 2010. Originalmente criado para um projeto de regressão, ele é uma excelente alternativa ao famoso dataset de Boston Housing, oferecendo mais variáveis e contextos para análise de preços de imóveis.

- **Tipo:** População
- **Tamanho:** 2930 observações, 82 variáveis
- **Origem:** Ames, Iowa Assessor's Office
- **Título do Artigo:** *Ames Iowa: Alternative to the Boston Housing Data Set*

## Variáveis

O dataset possui 82 colunas divididas em variáveis nominais, ordinais, discretas e contínuas.

### Variáveis Discretas e Identificadoras

| Variável      | Tipo     | Descrição                                                                                          |
|---------------|----------|----------------------------------------------------------------------------------------------------|
| `Order`       | Discreta | Número de observação.                                                                               |
| `PID`         | Nominal  | Número de identificação do lote - usado para revisão no site da cidade.                             |

### Classificação do Imóvel e Zonas

| Variável      | Tipo     | Descrição                                                                                          |
|---------------|----------|----------------------------------------------------------------------------------------------------|
| `MS SubClass` | Nominal  | Tipo de residência.                                                                                |
|               | Valores  | 
|               |          | 020: 1-ANDARE 1946 E MAIS RECENTE, TODOS OS ESTILOS                                                |
|               |          | 030: 1-ANDAR 1945 E MAIS ANTIGO                                                                    |
|               |          | 040: 1-ANDAR COM SÓTÃO ACABADO, TODAS AS IDADES                                                    |
|               |          | 045: 1-1/2 ANDAR - NÃO ACABADO, TODAS AS IDADES                                                    |
|               |          | 050: 1-1/2 ANDAR ACABADO, TODAS AS IDADES                                                          |
|               |          | 060: 2-ANDARES 1946 E MAIS RECENTE                                                                 |
|               |          | 070: 2-ANDARES 1945 E MAIS ANTIGO                                                                  |
|               |          | 075: 2-1/2 ANDAR, TODAS AS IDADES                                                                  |
|               |          | 080: SPLIT OU NÍVEL MÚLTIPLO                                                                       |
|               |          | 085: SPLIT FOYER                                                                                   |
|               |          | 090: DUPLEX - TODOS OS ESTILOS E IDADES                                                            |
|               |          | 120: PUD (Desenvolvimento de Unidade Planejada) DE 1-ANDAR - 1946 E MAIS RECENTE                   |
|               |          | 150: PUD DE 1-1/2 ANDAR, TODAS AS IDADES                                                           |
|               |          | 160: PUD DE 2-ANDARES - 1946 E MAIS RECENTE                                                        |
|               |          | 180: PUD - NÍVEL MÚLTIPLO - INCLUI SPLIT LEV/FOYER                                                 |
|               |          | 190: CONVERSÃO DE 2 FAMÍLIAS - TODOS OS ESTILOS E IDADES                                           |
| `MS Zoning`   | Nominal  | Classificação geral de zoneamento da venda.                                                         |
|               | Valores  | 
|               |          | A: Agricultura                                                                                     |
|               |          | C: Comercial                                                                                       |
|               |          | FV: Residencial Floating Village                                                                   |
|               |          | I: Industrial                                                                                      |
|               |          | RH: Residencial de Alta Densidade                                                                  |
|               |          | RL: Residencial de Baixa Densidade                                                                 |
|               |          | RP: Parque Residencial de Baixa Densidade                                                          |
|               |          | RM: Residencial de Média Densidade                                                                 |

### Dimensões do Lote e Acesso

| Variável         | Tipo         | Descrição                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| `Lot Frontage`   | Contínua     | Comprimento em pés lineares da rua conectada à propriedade.                             |
| `Lot Area`       | Contínua     | Tamanho do lote em pés quadrados.                                                       |
| `Street`         | Nominal      | Tipo de acesso rodoviário à propriedade.                                                |
|               | Valores  |                                                                                             |
|               |          | Grvl: Cascalho                                                                               |
|               |          | Pave: Pavimentado                                                                            |
| `Alley`          | Nominal      | Tipo de acesso de beco.                                                                 |
|               | Valores  |                                                                                             |
|               |          | Grvl: Cascalho                                                                               |
|               |          | Pave: Pavimentado                                                                            |
|               |          | NA: Sem acesso                                                                               |

### Formato do Lote e Contorno

| Variável         | Tipo         | Descrição                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| `Lot Shape`      | Ordinal      | Formato geral da propriedade.                                                           |
|               | Valores  |                                                                                             |
|               |          | Reg: Regular                                                                                  |
|               |          | IR1: Ligeiramente irregular                                                                  |
|               |          | IR2: Moderadamente irregular                                                                 |
|               |          | IR3: Irregular                                                                               |
| `Land Contour`   | Nominal      | Característica do terreno (nível, inclinado, depressão, etc.).                          |
|               | Valores  |                                                                                             |
|               |          | Lvl: Quase plano/nivelado                                                                    |
|               |          | Bnk: Elevado - Elevação rápida e significativa da rua para o edifício                         |
|               |          | HLS: Encosta - Inclinação significativa de um lado ao outro                                  |
|               |          | Low: Depressão                                                                               |

### Infraestrutura e Configuração do Lote

| Variável         | Tipo         | Descrição                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| `Utilities`      | Ordinal      | Tipo de utilidades disponíveis (água, esgoto, etc.).                                    |
|               | Valores  |                                                                                             |
|               |          | AllPub: Todas as utilidades públicas (Eletricidade, Gás, Água e Esgoto)                      |
|               |          | NoSewr: Eletricidade, Gás e Água (Tanque Séptico)                                           |
|               |          | NoSeWa: Apenas Eletricidade e Gás                                                           |
|               |          | ELO: Apenas Eletricidade                                                                    |
| `Lot Config`     | Nominal      | Configuração do lote.                                                                   |
|               | Valores  |                                                                                             |
|               |          | Inside: Lote interno                                                                        |
|               |          | Corner: Lote de esquina                                                                     |
|               |          | CulDSac: Cul-de-sac                                                                         |
|               |          | FR2: Fachada em 2 lados da propriedade                                                     |
|               |          | FR3: Fachada em 3 lados da propriedade                                                     |
| `Land Slope`     | Ordinal      | Inclinação do terreno.                                                                  |
|               | Valores  |                                                                                             |
|               |          | Gtl: Inclinação suave                                                                       |
|               |          | Mod: Inclinação moderada                                                                    |
|               |          | Sev: Inclinação severa                                                                      |

### Localização e Condições da Vizinhança

| Variável         | Tipo         | Descrição                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| `Neighborhood`   | Nominal      | Localização física dentro dos limites da cidade de Ames.                                |
|               | Valores  |                                                                                             |
|               |          | Blmngtn: Bloomington Heights                                                                 |
|               |          | Blueste: Bluestem                                                                            |
|               |          | BrDale: Briardale                                                                           |
|               |          | BrkSide: Brookside                                                                          |
|               |          | ClearCr: Clear Creek                                                                        |
|               |          | CollgCr: College Creek                                                                      |
|               |          | Crawfor: Crawford                                                                           |
|               |          | Edwards: Edwards                                                                            |
|               |          | Gilbert: Gilbert                                                                            |
|               |          | Greens: Greens                                                                              |
|               |          | GrnHill: Green Hills                                                                        |
|               |          | IDOTRR: Iowa DOT and Rail Road                                                              |
|               |          | Landmrk: Landmark                                                                           |
|               |          | MeadowV: Meadow Village                                                                     |
|               |          | Mitchel: Mitchell                                                                           |
|               |          | Names: North Ames                                                                           |
|               |          | NoRidge: Northridge                                                                         |
|               |          | NPkVill: Northpark Villa                                                                    |
|               |          | NridgHt: Northridge Heights                                                                 |
|               |          | NWAmes: Northwest Ames                                                                      |
|               |          | OldTown: Old Town                                                                           |
|               |          | SWISU: South & West of Iowa State University                                                |
|               |          | Sawyer: Sawyer                                                                              |
|               |          | SawyerW: Sawyer West                                                                        |
|               |          | Somerst: Somerset                                                                           |
|               |          | StoneBr: Stone Brook                                                                        |
|               |          | Timber: Timberland                                                                          |
|               |          | Veenker: Veenker                                                                            |
| `Condition 1`    | Nominal      | Proximidade a várias condições ambientais ou infraestruturais.                          |
|               | Valores  |                                                                                             |
|               |          | Artery: Adjacente a rua principal                                                            |
|               |          | Feedr: Adjacente a rua alimentadora                                                          |
|               |          | Norm: Normal                                                                                |
|               |          | RRNn: Dentro de 200' da Ferrovia Norte-Sul                                                  |
|               |          | RRAn: Adjacente à Ferrovia Norte-Sul                                                        |
|               |          | PosN: Perto de característica positiva - parque, área verde, etc.                           |
|               |          | PosA: Adjacente a característica positiva                                                   |
|               |          | RRNe: Dentro de 200' da Ferrovia Leste-Oeste                                                |
|               |          | RRAe: Adjacente à Ferrovia Leste-Oeste                                                      |
| `Condition 2`    | Nominal      | Segunda proximidade, caso existam múltiplas condições ambientais ou infraestruturais.    |
|               | Valores  |                                                                                             |
|               |          | Artery: Adjacente a rua principal                                                            |
|               |          | Feedr: Adjacente a rua alimentadora                                                          |
|               |          | Norm: Normal                                                                                |
|               |          | RRNn: Dentro de 200' da Ferrovia Norte-Sul                                                  |
|               |          | RRAn: Adjacente à Ferrovia Norte-Sul                                                        |
|               |          | PosN: Perto de característica positiva - parque, área verde, etc.                           |
|               |          | PosA: Adjacente a característica positiva                                                   |
|               |          | RRNe: Dentro de 200' da Ferrovia Leste-Oeste                                                |
|               |          | RRAe: Adjacente à Ferrovia Leste-Oeste                                                      |

### Tipo e Estilo da Construção

| Variável         | Tipo         | Descrição                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| `Bldg Type`      | Nominal      | Tipo de moradia (unifamiliar, duplex, etc.).                                            |
|               | Valores  |                                                                                             |
|               |          | 1Fam: Casa unifamiliar                                                                      |
|               |          | 2FmCon: Conversão para duas famílias (originalmente construída como unifamiliar)            |
|               |          | Duplx: Duplex                                                                               |
|               |          | TwnhsE: Townhouse, unidade de ponta                                                        |
|               |          | TwnhsI: Townhouse, unidade interna                                                         |
| `House Style`    | Nominal      | Estilo da moradia (um andar, dois andares, etc.).                                       |
|               | Valores  |                                                                                             |
|               |          | 1Story: Um andar                                                                            |
|               |          | 1.5Fin: Um andar e meio, segundo nível acabado                                              |
|               |          | 1.5Unf: Um andar e meio, segundo nível inacabado                                            |
|               |          | 2Story: Dois andares                                                                        |
|               |          | 2.5Fin: Dois andares e meio, segundo nível acabado                                          |
|               |          | 2.5Unf: Dois andares e meio, segundo nível inacabado                                        |
|               |          | SFoyer: Foyer dividido                                                                      |
|               |          | SLvl: Nível dividido                                                                        |

### Qualidade e Condição Geral da Propriedade

| Variável         | Tipo         | Descrição                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| `Overall Qual`   | Ordinal      | Qualidade geral dos materiais e acabamento (escala de 1 a 10).                          |
|               | Valores  |                                                                                             |
|               |          | 10: Muito Excelente                                                                         |
|               |          | 9: Excelente                                                                                |
|               |          | 8: Muito Bom                                                                                |
|               |          | 7: Bom                                                                                      |
|               |          | 6: Acima da Média                                                                           |
|               |          | 5: Médio                                                                                    |
|               |          | 4: Abaixo da Média                                                                          |
|               |          | 3: Regular                                                                                  |
|               |          | 2: Pobre                                                                                    |
|               |          | 1: Muito Pobre                                                                             |
| `Overall Cond`   | Ordinal      | Condição geral da casa (escala de 1 a 10).                                              |
|               | Valores  |                                                                                             |
|               |          | 10: Muito Excelente                                                                         |
|               |          | 9: Excelente                                                                                |
|               |          | 8: Muito Bom                                                                                |
|               |          | 7: Bom                                                                                      |
|               |          | 6: Acima da Média                                                                           |
|               |          | 5: Médio                                                                                    |
|               |          | 4: Abaixo da Média                                                                          |
|               |          | 3: Regular                                                                                  |
|               |          | 2: Pobre                                                                                    |
|               |          | 1: Muito Pobre                                                                             |

### Ano de Construção e Reforma

| Variável         | Tipo         | Descrição                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| `Year Built`     | Discreta     | Ano da construção original.                                                             |
| `Year Remod/Add` | Discreta     | Ano de reforma ou adição (igual ao ano de construção se não houver reforma).            |

### Cobertura e Material do Telhado

| Variável         | Tipo         | Descrição                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| `Roof Style`     | Nominal      | Tipo de telhado.                                                                        |
|               | Valores  |                                                                                             |
|               |          | Flat: Telhado plano                                                                          |
|               |          | Gable: Telhado de duas águas                                                                 |
|               |          | Gambrel: Telhado estilo celeiro (mansarda holandesa)                                         |
|               |          | Hip: Telhado de quatro águas                                                                 |
|               |          | Mansard: Telhado mansarda                                                                    |
|               |          | Shed: Telhado de uma água                                                                    |
| `Roof Matl`      | Nominal      | Material do telhado.                                                                    |
|               | Valores  |                                                                                             |
|               |          | ClyTile: Telha de argila ou cerâmica                                                         |
|               |          | CompShg: Telha composta padrão                                                               |
|               |          | Membran: Membrana                                                                            |
|               |          | Metal: Metal                                                                                |
|               |          | Roll: Rolo                                                                                   |
|               |          | Tar&Grv: Cascalho e piche                                                                    |
|               |          | WdShake: Telhas de madeira                                                                  |
|               |          | WdShngl: Telhas de madeira                                                                   |

### Revestimento Externo

| Variável         | Tipo         | Descrição                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| `Exterior 1`     | Nominal      | Material de revestimento externo principal.                                             |
|               | Valores  |                                                                                             |
|               |          | AsbShng: Telhas de amianto                                                                   |
|               |          | AsphShn: Telhas de asfalto                                                                   |
|               |          | BrkComm: Tijolo comum                                                                        |
|               |          | BrkFace: Tijolo à vista                                                                      |
|               |          | CBlock: Bloco de concreto                                                                    |
|               |          | CemntBd: Placa de cimento                                                                    |
|               |          | HdBoard: Madeira dura                                                                        |
|               |          | ImStucc: Estuque de imitação                                                                 |
|               |          | MetalSd: Revestimento metálico                                                               |
|               |          | Other: Outro                                                                                 |
|               |          | Plywood: Compensado                                                                          |
|               |          | PreCast: Pré-moldado                                                                         |
|               |          | Stone: Pedra                                                                                 |
|               |          | Stucco: Estuque                                                                              |
|               |          | VinylSd: Revestimento de vinil                                                               |
|               |          | Wd Sdng: Revestimento de madeira                                                             |
|               |          | WdShing: Telhas de madeira                                                                   |
| `Exterior 2`     | Nominal      | Material de revestimento externo secundário, se existir.                                |
|               | Valores  |                                                                                             |
|               |          | AsbShng: Telhas de amianto                                                                   |
|               |          | AsphShn: Telhas de asfalto                                                                   |
|               |          | BrkComm: Tijolo comum                                                                        |
|               |          | BrkFace: Tijolo à vista                                                                      |
|               |          | CBlock: Bloco de concreto                                                                    |
|               |          | CemntBd: Placa de cimento                                                                    |
|               |          | HdBoard: Madeira dura                                                                        |
|               |          | ImStucc: Estuque de imitação                                                                 |
|               |          | MetalSd: Revestimento metálico                                                               |
|               |          | Other: Outro                                                                                 |
|               |          | Plywood: Compensado                                                                          |
|               |          | PreCast: Pré-moldado                                                                         |
|               |          | Stone: Pedra                                                                                 |
|               |          | Stucco: Estuque                                                                              |
|               |          | VinylSd: Revestimento de vinil                                                               |
|               |          | Wd Sdng: Revestimento de madeira                                                             |
|               |          | WdShing: Telhas de madeira                                                                   |

### Tipo e Área de Alvenaria

| Variável         | Tipo         | Descrição                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| `Mas Vnr Type`   | Nominal      | Tipo de alvenaria.                                                                      |
|               | Valores  |                                                                                             |
|               |          | BrkCmn: Tijolo comum                                                                         |
|               |          | BrkFace: Tijolo à vista                                                                      |
|               |          | CBlock: Bloco de concreto                                                                    |
|               |          | None: Nenhum                                                                                 |
|               |          | Stone: Pedra                                                                                |
| `Mas Vnr Area`   | Contínua     | Área de alvenaria em pés quadrados.                                                     |

### Qualidade e Condição Externa

| Variável         | Tipo         | Descrição                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| `Exter Qual`     | Ordinal      | Qualidade do material exterior.                                                         |
|               | Valores  |                                                                                             |
|               |          | Ex: Excelente                                                                                |
|               |          | Gd: Bom                                                                                      |
|               |          | TA: Médio/Típico                                                                            |
|               |          | Fa: Regular                                                                                  |
|               |          | Po: Pobre                                                                                    |
| `Exter Cond`     | Ordinal      | Condição atual do material exterior.                                                    |
|               | Valores  |                                                                                             |
|               |          | Ex: Excelente                                                                                |
|               |          | Gd: Bom                                                                                      |
|               |          | TA: Médio/Típico                                                                            |
|               |          | Fa: Regular                                                                                  |
|               |          | Po: Pobre                                                                                    |

### Fundação e Qualidade do Porão

| Variável         | Tipo         | Descrição                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| `Foundation`     | Nominal      | Tipo de fundação (concreto, pedra, etc.).                                               |
|               | Valores  |                                                                                             |
|               |          | BrkTil: Tijolo e telha                                                                       |
|               |          | CBlock: Bloco de concreto                                                                    |
|               |          | PConc: Concreto despejado                                                                    |
|               |          | Slab: Laje                                                                                   |
|               |          | Stone: Pedra                                                                                 |
|               |          | Wood: Madeira                                                                               |
| `Bsmt Qual`      | Ordinal      | Avaliação da altura do porão.                                                           |
|               | Valores  |                                                                                             |
|               |          | Ex: Excelente (100+ polegadas)                                                               |
|               |          | Gd: Bom (90-99 polegadas)                                                                    |
|               |          | TA: Típico (80-89 polegadas)                                                                 |
|               |          | Fa: Regular (70-79 polegadas)                                                                |
|               |          | Po: Pobre (<70 polegadas)                                                                    |
|               |          | NA: Sem porão                                                                               |
| `Bsmt Cond`      | Ordinal      | Condição geral do porão.                                                                |
|               | Valores  |                                                                                             |
|               |          | Ex: Excelente                                                                                |
|               |          | Gd: Bom                                                                                      |
|               |          | TA: Típico - leve umidade permitida                                                          |
|               |          | Fa: Regular - umidade ou algumas rachaduras                                                  |
|               |          | Po: Pobre - rachaduras graves, assentamento ou umidade significativa                         |
|               |          | NA: Sem porão                                                                               |

### Exposição e Tipo de Área Acabada do Porão

| Variável         | Tipo         | Descrição                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| `Bsmt Exposure`  | Ordinal      | Exposição do porão a paredes de nível de jardim ou saídas.                              |
|               | Valores  |                                                                                             |
|               |          | Gd: Boa exposição                                                                            |
|               |          | Av: Exposição média (níveis divididos ou foyers geralmente têm média ou acima)              |
|               |          | Mn: Exposição mínima                                                                         |
|               |          | No: Sem exposição                                                                            |
|               |          | NA: Sem porão                                                                               |
| `BsmtFin Type 1` | Ordinal      | Tipo da área acabada do porão (principal).                                              |
|               | Valores  |                                                                                             |
|               |          | GLQ: Boa área de habitação                                                                   |
|               |          | ALQ: Área de habitação média                                                                 |
|               |          | BLQ: Área de habitação abaixo da média                                                       |
|               |          | Rec: Sala de recreação média                                                                 |
|               |          | LwQ: Qualidade baixa                                                                         |
|               |          | Unf: Não acabado                                                                             |
|               |          | NA: Sem porão                                                                               |
| `BsmtFin SF 1`   | Contínua     | Área em pés quadrados do Tipo 1 acabado no porão.                                       |
| `BsmtFin Type 2` | Ordinal      | Tipo da área acabada adicional no porão, se houver.                                     |
|               | Valores  |                                                                                             |
|               |          | GLQ: Boa área de habitação                                                                   |
|               |          | ALQ: Área de habitação média                                                                 |
|               |          | BLQ: Área de habitação abaixo da média                                                       |
|               |          | Rec: Sala de recreação média                                                                 |
|               |          | LwQ: Qualidade baixa                                                                         |
|               |          | Unf: Não acabado                                                                             |
|               |          | NA: Sem porão                                                                               |
| `BsmtFin SF 2`   | Contínua     | Área em pés quadrados do Tipo 2 acabado no porão.                                       |

### Área Não Acabada e Total do Porão

| Variável         | Tipo         | Descrição                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| `Bsmt Unf SF`    | Contínua     | Área não acabada do porão em pés quadrados.                                             |
| `Total Bsmt SF`  | Contínua     | Área total do porão em pés quadrados.                                                   |

### Sistema de Aquecimento e Condição

| Variável         | Tipo         | Descrição                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| `Heating`        | Nominal      | Tipo de aquecimento.                                                                    |
|               | Valores  |                                                                                             |
|               |          | Floor: Aquecedor de piso                                                                      |
|               |          | GasA: Forno a gás com ar quente forçado                                                      |
|               |          | GasW: Aquecimento a gás por água quente ou vapor                                             |
|               |          | Grav: Forno de gravidade                                                                     |
|               |          | OthW: Aquecimento por água quente ou vapor, exceto a gás                                    |
|               |          | Wall: Aquecedor de parede                                                                    |
| `HeatingQC`      | Ordinal      | Qualidade e condição do sistema de aquecimento.                                         |
|               | Valores  |                                                                                             |
|               |          | Ex: Excelente                                                                                |
|               |          | Gd: Bom                                                                                      |
|               |          | TA: Médio/Típico                                                                            |
|               |          | Fa: Regular                                                                                  |
|               |          | Po: Pobre                                                                                    |

### Ar Condicionado Central

| Variável         | Tipo         | Descrição                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| `Central Air`    | Nominal      | Indica se a casa possui ar condicionado central.                                        |
|               | Valores  |                                                                                             |
|               |          | N: Não                                                                                       |
|               |          | Y: Sim                                                                                       |

### Sistema Elétrico

| Variável         | Tipo         | Descrição                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| `Electrical`     | Ordinal      | Sistema elétrico (padrão, fusíveis, etc.).                                              |
|               | Valores  |                                                                                             |
|               |          | SBrkr: Disjuntores padrão e fiação Romex                                                    |
|               |          | FuseA: Caixa de fusíveis acima de 60 AMP com fiação Romex (Médio)                           |
|               |          | FuseF: Caixa de fusíveis de 60 AMP com fiação Romex (Regular)                               |
|               |          | FuseP: Caixa de fusíveis de 60 AMP com fiação de botão e tubo (Pobre)                       |
|               |          | Mix: Sistema misto                                                                          |

### Área e Banheiros

| Variável         | Tipo         | Descrição                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| `1st Flr SF`     | Contínua     | Área do primeiro andar em pés quadrados.                                               |
| `2nd Flr SF`     | Contínua     | Área do segundo andar em pés quadrados.                                                |
| `Low Qual Fin SF`| Contínua     | Área de baixa qualidade acabada em pés quadrados.                                      |
| `Gr Liv Area`    | Contínua     | Área acima do nível do solo em pés quadrados.                                          |
| `Bsmt Full Bath` | Discreta     | Número de banheiros completos no porão.                                               |
| `Bsmt Half Bath` | Discreta     | Número de meios-banheiros no porão.                                                    |
| `Full Bath`      | Discreta     | Número de banheiros completos acima do solo.                                           |
| `Half Bath`      | Discreta     | Número de meios-banheiros acima do solo.                                               |

### Quartos e Qualidade da Cozinha

| Variável         | Tipo         | Descrição                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| `Bedroom`        | Discreta     | Número de quartos acima do solo.                                                       |
| `Kitchen`        | Discreta     | Número de cozinhas acima do solo.                                                      |
| `KitchenQual`    | Ordinal      | Qualidade da cozinha.                                                                  |
|               | Valores  |                                                                                             |
|               |          | Ex: Excelente                                                                                |
|               |          | Gd: Bom                                                                                      |
|               |          | TA: Típico/Médio                                                                            |
|               |          | Fa: Regular                                                                                  |
|               |          | Po: Pobre                                                                                    |

### Total de Cômodos e Funcionalidade

| Variável         | Tipo         | Descrição                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| `TotRmsAbvGrd`   | Discreta     | Número total de cômodos acima do solo (não inclui banheiros).                          |
| `Functional`     | Ordinal      | Funcionalidade da casa.                                                                |
|               | Valores  |                                                                                             |
|               |          | Typ: Funcionalidade típica                                                                  |
|               |          | Min1: Pequenas deduções 1                                                                   |
|               |          | Min2: Pequenas deduções 2                                                                   |
|               |          | Mod: Deduções moderadas                                                                     |
|               |          | Maj1: Grandes deduções 1                                                                    |
|               |          | Maj2: Grandes deduções 2                                                                    |
|               |          | Sev: Severamente danificada                                                                 |
|               |          | Sal: Somente para salvamento                                                                |

### Lareiras e Garagem

| Variável         | Tipo         | Descrição                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| `Fireplaces`     | Discreta     | Número de lareiras.                                                                    |
| `FireplaceQu`    | Ordinal      | Qualidade da lareira.                                                                  |
|               | Valores  |                                                                                             |
|               |          | Ex: Excelente - Lareira de alvenaria excepcional                                            |
|               |          | Gd: Bom - Lareira de alvenaria no nível principal                                           |
|               |          | TA: Médio - Lareira pré-fabricada na área principal ou de alvenaria no porão               |
|               |          | Fa: Regular - Lareira pré-fabricada no porão                                                |
|               |          | Po: Pobre - Lareira tipo Ben Franklin Stove                                                |
|               |          | NA: Sem lareira                                                                             |
| `Garage Type`    | Nominal      | Localização da garagem.                                                                 |
|               | Valores  |                                                                                             |
|               |          | 2Types: Mais de um tipo de garagem                                                          |
|               |          | Attchd: Anexada à casa                                                                      |
|               |          | Basment: Garagem no porão                                                                   |
|               |          | BuiltIn: Integrada (parte da casa, normalmente com cômodo acima)                           |
|               |          | CarPort: Carport                                                                            |
|               |          | Detchd: Destacada da casa                                                                   |
|               |          | NA: Sem garagem                                                                            |
| `Garage Yr Blt`  | Discreta     | Ano de construção da garagem.                                                          |
| `Garage Finish`  | Ordinal      | Acabamento interior da garagem.                                                        |
|               | Valores  |                                                                                             |
|               |          | Fin: Acabada                                                                                |
|               |          | RFn: Acabada superficialmente                                                               |
|               |          | Unf: Sem acabamento                                                                         |
|               |          | NA: Sem garagem                                                                             |
| `Garage Cars`    | Discreta     | Capacidade da garagem em número de carros.                                             |
| `Garage Area`    | Contínua     | Área da garagem em pés quadrados.                                                      |
| `Garage Qual`    | Ordinal      | Qualidade da garagem.                                                                  |
|               | Valores  |                                                                                             |
|               |          | Ex: Excelente                                                                                |
|               |          | Gd: Bom                                                                                      |
|               |          | TA: Médio/Típico                                                                            |
|               |          | Fa: Regular                                                                                  |
|               |          | Po: Pobre                                                                                    |
|               |          | NA: Sem garagem                                                                             |
| `Garage Cond`    | Ordinal      | Condição da garagem.                                                                   |
|               | Valores  |                                                                                             |
|               |          | Ex: Excelente                                                                                |
|               |          | Gd: Bom                                                                                      |
|               |          | TA: Médio/Típico                                                                            |
|               |          | Fa: Regular                                                                                  |
|               |          | Po: Pobre                                                                                    |
|               |          | NA: Sem garagem                                                                             |

### Entrada Pavimentada e Áreas Externas

| Variável         | Tipo         | Descrição                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| `Paved Drive`    | Ordinal      | Entrada pavimentada.                                                                    |
|               | Valores  |                                                                                             |
|               |          | Y: Pavimentada                                                                               |
|               |          | P: Pavimentação parcial                                                                      |
|               |          | N: Terra/Cascalho                                                                            |
| `Wood Deck SF`   | Contínua     | Área de deck de madeira em pés quadrados.                                              |
| `Open Porch SF`  | Contínua     | Área de varanda aberta em pés quadrados.                                               |
| `Enclosed Porch` | Contínua     | Área de varanda fechada em pés quadrados.                                              |
| `3-Ssn Porch`    | Contínua     | Área de varanda para três estações em pés quadrados.                                   |
| `Screen Porch`   | Contínua     | Área de varanda com tela em pés quadrados.                                             |
| `Pool Area`      | Contínua     | Área da piscina em pés quadrados.                                                      |
| `Pool QC`        | Ordinal      | Qualidade da piscina.                                                                  |
|               | Valores  |                                                                                             |
|               |          | Ex: Excelente                                                                                |
|               |          | Gd: Bom                                                                                      |
|               |          | TA: Médio/Típico                                                                            |
|               |          | Fa: Regular                                                                                  |
|               |          | NA: Sem piscina                                                                             |
| `Fence`          | Ordinal      | Qualidade da cerca.                                                                    |
|               | Valores  |                                                                                             |
|               |          | GdPrv: Boa privacidade                                                                       |
|               |          | MnPrv: Privacidade mínima                                                                    |
|               |          | GdWo: Boa madeira                                                                            |
|               |          | MnWw: Madeira/arame mínimo                                                                   |
|               |          | NA: Sem cerca                                                                               |

### Recursos Adicionais e Vendas

| Variável         | Tipo         | Descrição                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| `Misc Feature`   | Nominal      | Recurso adicional não coberto em outras categorias.                                     |
|               | Valores  |                                                                                             |
|               |          | Elev: Elevador                                                                               |
|               |          | Gar2: Segunda garagem (se não descrito na seção de garagem)                                  |
|               |          | Othr: Outro                                                                                  |
|               |          | Shed: Barracão (mais de 100 pés quadrados)                                                   |
|               |          | TenC: Quadra de tênis                                                                        |
|               |          | NA: Nenhum                                                                                   |
| `Misc Val`       | Contínua     | Valor em dólares do recurso adicional.                                                 |
| `Mo Sold`        | Discreta     | Mês da venda.                                                                          |
| `Yr Sold`        | Discreta     | Ano da venda.                                                                          |
| `Sale Type`      | Nominal      | Tipo de venda.                                                                         |
|               | Valores  |                                                                                             |
|               |          | WD: Escritura de garantia - Convencional                                                     |
|               |          | CWD: Escritura de garantia - À vista                                                        |
|               |          | VWD: Escritura de garantia - Empréstimo VA                                                  |
|               |          | New: Casa recém-construída e vendida                                                        |
|               |          | COD: Escritura de oficial de justiça/herança                                                |
|               |          | Con: Contrato com 15% de entrada e condições regulares                                      |
|               |          | ConLw: Contrato com entrada baixa e juros baixos                                            |
|               |          | ConLI: Contrato com juros baixos                                                            |
|               |          | ConLD: Contrato com entrada baixa                                                           |
|               |          | Oth: Outro                                                                                  |
| `Sale Condition` | Nominal      | Condição da venda.                                                                    |
|               | Valores  |                                                                                             |
|               |          | Normal: Venda normal                                                                        |
|               |          | Abnorml: Venda anormal (troca, execução hipotecária, venda rápida)                          |
|               |          | AdjLand: Compra de terreno adjacente                                                        |
|               |          | Alloca: Alocação - duas propriedades ligadas com escrituras separadas                       |
|               |          | Family: Venda entre familiares                                                              |
|               |          | Partial: Casa não estava completa quando foi avaliada pela última vez                       |
| `SalePrice`      | Contínua     | Preço de venda em dólares.                                                             |

## Notas Especiais

Para análise educacional, recomenda-se remover as propriedades com mais de 4000 pés quadrados para evitar a influência de outliers. Existem 5 observações que podem ser removidas antes de disponibilizar o dataset para estudantes. Três dessas observações são outliers reais (vendas parciais que provavelmente não representam valores de mercado reais), enquanto as outras duas são vendas incomuns de casas muito grandes com preços relativamente apropriados.

## História do Dataset

Este dataset foi criado para um projeto de final de semestre de um curso de regressão para graduação. Os dados originais, obtidos diretamente do Escritório de Avaliação de Ames, são utilizados para fins de avaliação tributária, mas se aplicam diretamente à previsão de preços de venda de imóveis. O tipo de informação contida no dataset é similar ao que um comprador típico de imóveis gostaria de saber antes de realizar uma compra, sendo assim as variáveis são geralmente fáceis de entender.

## Notas Pedagógicas

Para instrutores que não estão familiarizados com regressão múltipla, recomenda-se utilizar este dataset juntamente com um artigo da JSE que aborda as principais questões da modelagem de regressão:

- **Kuiper, S.** (2008). "Introduction to Multiple Regression: How Much Is Your Car Worth?", *Journal of Statistics Education*, Volume 16, Número 3.

Além das questões gerais de regressão múltipla discutidas nesse artigo, este dataset específico oferece oportunidades para discutir como o propósito de um modelo pode afetar o tipo de modelagem realizada. Outra referência relevante é:

- **Pardoe, I.** (2008). "Modeling home prices using realtor data", *Journal of Statistics Education*, Volume 16, Número 2.

Questões como homocedasticidade e violações de suposições são comuns em modelos de preços de imóveis que focam apenas nos tamanhos de casas e lotes. Embora essa violação possa ser atenuada transformando a variável de resposta (preço de venda), isso pode resultar em valores ajustados de difícil interpretação (como preço em log ou raiz quadrada). Esse contexto abre a possibilidade de discutir os custos e benefícios de corrigir ou não essas violações, e as diferenças entre modelos preditivos, mineração de dados e inferência estatística formal.

Outra questão importante é o tratamento de outliers e observações incomuns. Geralmente, é recomendável não excluir pontos de dados apenas porque não correspondem às expectativas iniciais, especialmente em análises para fins de pesquisa. No entanto, ao criar um modelo de uso comum para estimar vendas "típicas", pode ser interessante remover observações que pareçam atípicas (como vendas entre familiares ou execuções hipotecárias).

## Referências

Casas específicas no dataset podem ser consultadas diretamente no site do Escritório de Avaliação de Ames, utilizando o PID presente no dataset. Esses valores são nominais, e zeros iniciais devem ser incluídos no campo de entrada no site. Acesso ao banco de dados pode ser feito no site de Ames [Link](http://www.cityofames.org/assessor/) em "property search" ou via Beacon [Link](http://beacon.schneidercorp.com/Default.aspx), inserindo Iowa e Ames nos campos apropriados. Um mapa da cidade mostrando as localizações de todos os bairros também está disponível no site de Ames em "Maps" e "Residential Assessment Neighborhoods (City of Ames Only)".

## Enviado por

**Dean De Cock**  
Truman State University  
100 E. Normal St., Kirksville, MO, 63501  
Email: decock@truman.edu
