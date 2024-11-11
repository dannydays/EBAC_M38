# Previsão de Crédito com Machine Learning

Este projeto utiliza técnicas de aprendizado de máquina para prever o risco de crédito, fornecendo uma interface interativa com Streamlit. O modelo de classificação **LightGBM** foi treinado para identificar se um cliente está em risco de inadimplência com base em um conjunto de dados de crédito.

## Funcionalidades:
- **Carregamento de Dataset**: O usuário pode carregar um dataset de crédito no formato CSV ou Feather.
- **Previsão de Risco**: O modelo faz previsões para cada cliente no dataset carregado.
- **Exportação de Resultados**: O usuário pode baixar os resultados das previsões em formato CSV.

### Requisitos:
- Python 3.11
- Bibliotecas:
  - `streamlit`
  - `pandas`
  - `pycaret`
  - `scikit-learn`
  - `pyarrow` (para Feather)
  
### Instalação:
```bash
pip install streamlit pandas pycaret scikit-learn pyarrow
```
### Rodando a aplicação:
```
streamlit run app.py
```
## Demonstração:
[streamlit-app-2024-11-11-17-11-74.webm](https://github.com/user-attachments/assets/2ff25831-a409-46a9-a53d-9d8022d29841)
