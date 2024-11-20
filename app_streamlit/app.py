import streamlit as st
import numpy as np
import pandas as pd
import os
import sys
from PIL import Image
import joblib  # Para cargar el modelo preentrenado

# Cargamos el modelo preentrenado
model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'trained_model_1.pkl')
model = joblib.load(model_path)

# Título de la aplicación
st.title('Predicción de Salarios de Puestos de Trabajo relacionados con el Data Science')

# Foto cabecera
image_path = os.path.join(os.path.dirname(__file__), '..', 'docs', 'header.jpg')
image = Image.open(image_path)
st.image(image)

# Pequeña intro
st.subheader("Si quieres conocer el salario de los puestos más importantes del campo de la IA, ML y el DS, ¡este es tu sitio!")
st.write("Basado en datos históricos, el modelo tiene en cuenta diversas variables para generar una estimación del sueldo anual en dólares. Solo tienes que introducir la información correspondiente en los campos disponibles y el modelo calculará automáticamente una predicción. Puedes experimentar con diferentes combinaciones de variables para ver cómo influyen en la estimación final.¡Explora las predicciones y obtén una visión más clara sobre las expectativas salariales en el mundo del Data Science!")

# Inputs del usuario
st.subheader('Por favor, rellena los siguientes campos:')

# experience_level
exp_level_order = st.selectbox("Nivel de experiencia:",['Junior', 'Intermediate', 'Senior', 'Director'])

# job_title

def job_title_group(job_title):
    if any(keyword in job_title for keyword in ['Data Scientist', 'Machine Learning', 'AI', 'Deep Learning', 'NLP', 'Quantitative', 'Statistical']):
        return 'Data Science & Machine Learning'
    elif any(keyword in job_title for keyword in ['Data Engineer', 'Big Data', 'ETL', 'Infrastructure', 'Pipeline', 'Platform', 'Cloud']):
        return 'Data Engineering & Infrastructure'
    elif any(keyword in job_title for keyword in ['BI', 'Business Intelligence', 'Analyst', 'Analytics', 'Power BI', 'Insight']):
        return 'Business Intelligence & Analytics'
    elif any(keyword in job_title for keyword in ['Software', 'Engineer', 'Developer', 'Backend', 'Frontend', 'Full Stack', 'DevOps', 'Solutions Architect']):
        return 'Software Development & Engineering'
    elif any(keyword in job_title for keyword in ['Manager', 'Lead', 'Head', 'Director', 'Consultant']):
        return 'Management & Leadership'
    else:
        return 'Specialized Roles'
    
job_titles = [
    'Data Scientist', 'Machine Learning Engineer', 'AI Specialist', 'Deep Learning Researcher', 
    'NLP Expert', 'Quantitative Analyst', 'Statistical Modeler', 
    'Data Engineer', 'Big Data Architect', 'ETL Developer', 'Cloud Engineer', 'Pipeline Architect', 
    'BI Analyst', 'Business Intelligence Specialist', 'Analytics Expert', 'Power BI Developer', 'Insight Analyst', 
    'Software Engineer', 'Backend Developer', 'Frontend Developer', 'Full Stack Developer', 'DevOps Engineer', 
    'Solutions Architect', 'Manager', 'Lead', 'Head', 'Director', 'Consultant']


job_title = st.selectbox("Rol a desempeñar:", job_titles)

# Clasificar el título seleccionado
if job_title:
    job_group = job_title_group(job_title)
else:
    st.write("Por favor, selecciona un título de trabajo de la lista")

#company_location / employee_residence
countries = ['Canada','United States','Latvia','United Kingdom','Lithuania','Italy','Philippines','Spain','Austria','Netherlands','South Africa','Australia','Slovakia','Mexico','Germany','Poland','France','New Zealand','Argentina','Portugal','Ireland','Croatia','Switzerland','Finland','Brazil','Colombia','Israel','Singapore','Sweden','Chile','Ukraine','Turkey','Pakistan','Japan','Armenia','Honduras','Greece','Egypt','Malta','Czech Republic','Belgium','Cyprus','Bulgaria','Luxembourg','Serbia and Montenegro','Denmark','Saudi Arabia','Bosnia and Herzegovina','Estonia','Hungary','Vietnam','Slovenia','Mauritius','Russia','Andorra','Ecuador','Norway','Hong Kong','Thailand','Iran','Puerto Rico','Indonesia','Malaysia','China','Moldova','India','Georgia','Uganda','Tunisia','Peru','Nigeria','Ghana','Uzbekistan','Kuwait','Costa Rica','Bolivia','Dominican Republic','Jersey','Romania']

#Campos que no usamos en el modelo pero los metemos igualmente
st.selectbox("Tipo de trabajo:",['Full-Time', 'Part-Time', 'Contract', 'Freelance'])
st.selectbox("Presencialidad:",['<=20% teletrabajo', 'Híbrido', '>=80% teletrabajo'])
st.selectbox("Tamaño de la compañía:",['Menos de 50 empleados', 'Entre 50 y 250 empleados', 'Más de 250 empleados'])

#Necesito la tabla "maestra" en la que tengo las relaciones de los países con su pib y su tasa de desempleo
csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed', 'salaries_final_v2.csv')
tabla_maestra = pd.read_csv(csv_path)

company__location = st.selectbox('País de la sede de la empresa:', countries)
employee_residence = st.selectbox('País de residencia del empleado:', countries)

# Botón para realizar la predicción
if st.button('Calcular Salario'):

    # Convertir inputs a valores numéricos
    experience_mapping = {'Junior': 1, 'Intermediate': 2, 'Senior': 3, 'Director': 4}
    american_based_mapping = {'Sí': 1, 'No': 0}
    data_science_ml = 1 if job_group == 'Data Science & Machine Learning' else 0
    business_intelligence = 1 if job_group == 'Business Intelligence & Analytics' else 0
    software_development = 1 if job_group == 'Software Development & Engineering' else 0
    experience_value = experience_mapping[exp_level_order]

    # Crear un DataFrame con los datos de entrada
    input_data = pd.DataFrame({
        "experience_level": [experience_value],
        "mean_pib":[tabla_maestra[tabla_maestra["company_country"] == company__location]["mean_pib"].values[0]],
        "unemployment_rate":[tabla_maestra[tabla_maestra["company_country"] == employee_residence]["unemployment_rate"].values[0]],
        "company_employee_US": [1 if company__location == "United States" and employee_residence == "United States" else 0] ,
        "company__Americas":[tabla_maestra[tabla_maestra["company_country"] == company__location]["company__Americas"].values[0]],
        "company__Europe": [tabla_maestra[tabla_maestra["company_country"] == company__location]["company__Europe"].values[0]],
        'Business Intelligence & Analytics':[business_intelligence],
        'Data Science & Machine Learning':[data_science_ml],
        'Software Development & Engineering':[software_development]
    })

    # Realizar la predicción con el modelo
    predicted_salary = model.predict(input_data)

    # Mostrar el salario predicho
    st.subheader('Salario Predicho:')
    st.write(f'${predicted_salary[0]:,.2f} USD')