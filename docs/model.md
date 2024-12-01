# Escolha do Modelo

A seleção do melhor modelo foi realizada no `notebook` **04_model_selection**, disponível na pasta `notebooks`.

Foram avaliados os seguintes modelos:

- **Random Forest Regressor**
- **Decision Tree Regressor**
- **Lasso**
- **Ridge**
- **Gradient Boosting Regressor**

## Critério de Avaliação

O critério escolhido para avaliar os modelos foi o **Root Mean Squared Error (RMSE)**, uma métrica amplamente utilizada para medir erros em problemas de regressão. O RMSE é calculado como a raiz quadrada da média dos erros quadráticos, fornecendo uma estimativa intuitiva da discrepância entre os valores previstos e os valores reais.

## Metodologia

Para garantir resultados robustos e evitar o problema de overfitting, foram adotadas as seguintes práticas:

1. **GridSearchCV**: Utilizado para encontrar a combinação ideal de hiperparâmetros para cada modelo.
2. **Cross-Validation**: Implementado para dividir os dados em múltiplos conjuntos de treinamento e validação, assegurando que o modelo seja testado em diferentes subconjuntos de dados.
3. **Teste de Hipótese**: Para comparar os resultados dos modelos e confirmar que o **Random Forest Regressor** apresentou um desempenho significativamente superior.

Detalhes completos sobre os experimentos e análises podem ser encontrados no notebook **04_model_selection**.

## Importância das Features

O **Random Forest Regressor** foi selecionado como o melhor modelo para os dados. A análise de importância das features revelou os seguintes atributos mais relevantes:

1. **Fireplaces**
2. **Kitchen.Qual**
3. **Remod.Age**
4. **Open.Porch.SF**
5. **Garage.Age**
6. **Lot.Area**
7. **Full.Bath**
8. **BsmtFin.SF.1**
9. **Garage.Cars**
10. **X1st.Flr.SF**
11. **Exter.Qual**
12. **Total.Bsmt.SF**
13. **Garage.Area**
14. **Gr.Liv.Area**
15. **Overall.Qual**

## Modelo Reduzido

Com base nos resultados apresentados no notebook **04_model_selection**, constatou-se que treinar o modelo apenas com essas features já oferece um desempenho satisfatório. Ao aplicar o **Random Forest Regressor** com as features selecionadas, o erro em relação ao preço real das casas foi reduzido para **13,3%**, demonstrando a eficiência do modelo ajustado.

Para mais informações e análises detalhadas, consulte o notebook mencionado.
