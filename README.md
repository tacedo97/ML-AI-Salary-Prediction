# 📊 ML-AI-Salary-Prediction 📊 

![logos](./docs/header.jpg)



## 🎯 Objetivo del Proyecto
El objetivo de este proyecto es construir un modelo predictivo que permita estimar el salario anual en USD para diferentes roles relacionados con el mundo del Data Science, Machine Learning e Inteligencia Artificial, teniendo en cuenta características clave como el nivel de experiencia, la ubicación de la empresa y del empleado... La idea principal es dar transparencia y guía sobre las expectativas salariales en el sector, proporcionando información útil tanto para profesionales como para empresas.

## 🚀 Tecnologías Utilizadas
Este proyecto se ha realizado usando una combinación de tecnologías de Data Science y Machine Learning. Las principales herramientas utilizadas incluyen:

- Python 🐍: lenguaje principal del proyecto.
- Pandas, NumPy 📊: para la manipulación y análisis de datos.
- Matplotlib, Seaborn 🎨: para la visualización de datos y gráficos.
- Scikit-Learn 📘: para la creación y ajuste de modelos.
- XGBoost, LightGBM ⚡: modelos avanzados para mejorar la precisión.
- Streamlit 🌐: para el desarrollo de la aplicación interactiva.

## 🛠️ Estructura del Proyecto
El repositorio está organizado de la siguiente manera:

```
📂 ML-AI-Salary-Prediction
│
|── 📁 app_streamlit    
│   └── app.py                              # Código principal de la aplicación
|   └── requirements.txt                    # Pendiente de hacer
|
├── 📁 data                 
│   ├── processed                           # Datos procesados listos para el entrenamiento
│   └── raw                                 # Datos  originales
|   └── test                                # Conjunto de entrenamiento
|   └── train                               # Conjunto de test
│
|── 📁 docs                                 # Documentación e imágenes utilizadas          
|
├── 📁 models                               # Modelos entrenados (pendiente definir uno no supervisado y una red neuronal, además del archivo .yaml)
│   └── trained_model_1.pkl   
│   └── trained_model_2.pkl   
|   └── trained_model_3.pkl
│   └── trained_model_4.pkl
|   └── trained_model_5.pkl
│
├── 📁 notebooks  
|   └── 01_Fuentes.ipynb                    # Adquisición de datos y unión de las diferentes fuentes.
│   └── 02_LimpiezaEDA.ipynb                # Tratamiento de los datos
|   └── 03_Entrenamiento_Evaluacion.ipynb   # Proceso de entrenamiento y obtención de resultados de los distintos modelos
|
├── 📁 src                                  # Pendiente de hacer
|
└── README.md                # Este archivo
```

## 📊 Análisis Realizado
El proyecto implicó un análisis exhaustivo de los datos y varios procesos de Feature Engineering, incluyendo:

- Limpieza y preprocesamiento de datos: eliminando valores nulos, corrigiendo errores y ajustando las variables relevantes.
- Análisis exploratorio 📊: visualización de distribuciones, relaciones entre variables, correlaciones, etc.
- Feature Engineering 🛠️: transformación y selección de características que afectan significativamente al salario.
- Entrenamiento de modelos supervisados 📈: usando técnicas como Árboles de Decisión, SVR, Random Forest, XGBoost, LightGBM, etc.
- Evaluación y ajuste de modelos ⚙️: utilizando GridSearchCV para encontrar los mejores hiperparámetros y mejorar la precisión.

## 🧠 Modelos Supervisados Utilizados
En este proyecto, se probaron y optimizaron los siguientes modelos:

- Decision Tree Regressor 🌳
- Support Vector Regressor (SVR) 📉
- XGBoost 🚀
- Random Forest Regressor 🌲
- LightGBM 💡
Cada modelo fue ajustado mediante una búsqueda exhaustiva de hiperparámetros para mejorar su rendimiento en términos de Error Absoluto Medio (MAE) y R².

## 🖥️ Aplicación Interactiva
Puedes acceder a la aplicación de predicción usando Streamlit, donde podrás introducir los parámetros específicos y obtener una predicción instantánea del salario. ¡Experimenta con diferentes combinaciones para ver cómo cambian los resultados!

### Cómo Ejecutar la Aplicación:
*Pendiente de incluir*

## 📚 Aprendizajes y Reflexiones
Una de las lecciones más importantes aprendidas en este proyecto fue la importancia de contar con datos de calidad. A pesar de los esfuerzos en la selección de características y la optimización de modelos, la precisión final depende en gran medida de los datos utilizados para el entrenamiento. Este proyecto resalta que, en Data Science, la calidad de los datos es tan crucial como la elección de los modelos.