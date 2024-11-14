import streamlit as st
import numpy as np
import pandas as pd
import joblib  # Para cargar el modelo preentrenado

# Cargamos el modelo preentrenado
model = joblib.load(r'C:\Users\tamar\Documents\004. Cursos\000. Bootcamp The Bridge\1. Repositorios\ML-AI-Salary-Prediction\ML-AI-Salary-Prediction\models\modelo_baseline_final.pkl')

# Título de la aplicación
st.title('Predicción de Salario en USD')

# Inputs del usuario
st.subheader('Introduce los siguientes parámetros:')

# Lista de opciones de experiencia
exp_level_order = st.selectbox('Nivel de experiencia:', ['Junior', 'Intermediate', 'Senior', 'Director'])

# ¿Tiene sede en América?
company__Americas = st.selectbox('¿La compañía tiene sede en el continente de América?', ['Sí', 'No'])

# Botón para realizar la predicción
if st.button('Calcular Salario'):

    # Convertir inputs a valores numéricos (ajustar según cómo tu modelo los espera)
    experience_mapping = {'Junior': 0, 'Intermediate': 1, 'Senior': 2, 'Director': 3}
    american_based_mapping = {'Sí': 1, 'No': 0}

    #Cargamos el scaler usado en nuestro modelo
    scaler = joblib.load(r'C:\Users\tamar\Documents\004. Cursos\000. Bootcamp The Bridge\1. Repositorios\ML-AI-Salary-Prediction\ML-AI-Salary-Prediction\models\StandardScaler.pkl')

    # Convertir los valores de entrada
    experience_value = experience_mapping[exp_level_order]
    american_based_value = american_based_mapping[company__Americas]

    # Crear un DataFrame con los datos de entrada
    input_data = pd.DataFrame({
        'exp_level_order': [experience_value],
        'company__Americas': [american_based_value]
    })

    # Escalamos el df de los datos de entrada
    input_data_scaler = scaler.transform(input_data)

    # Realizar la predicción con el modelo
    predicted_log_salary = model.predict(input_data_scaler)

    # Inversa de la transformación logarítmica
    predicted_salary = np.exp(predicted_log_salary)

    # Mostrar el salario predicho
    st.subheader('Salario Predicho:')
    st.write(f'${predicted_salary[0]:,.2f} USD')