import streamlit as st

from pycaret.classification import load_model, predict_model
from io import BytesIO

import pandas as pd

st.set_page_config(initial_sidebar_state='expanded',
                   page_title='Projeto_M38',)
df = None

@st.cache_data
def model():
    return load_model('lightgbm_112024')

@st.cache_data
def to_csv(df):
    return df.to_csv(index=False).encode()

with st.sidebar:
    file = st.file_uploader(label='Credit Dataset:', type=['csv', 'ftr'])
    if file is not None:
        df = pd.read_feather(file)
        df = df.drop(['mau', 'index', 'data_ref'], axis=1)
        
if df is not None:
    model = model()
    pred = predict_model(model, data=df)

    st.write(pred)

    final_csv = to_csv(pred)
    st.download_button('Download Predict', final_csv, file_name='predict.csv')
