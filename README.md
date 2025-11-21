---
title: dp25
app_file: app.py
sdk: gradio
sdk_version: 5.49.1
---

# Sistema de Detección de Diabetes con Inteligencia Artificial

Este proyecto implementa un sistema de **detección temprana de diabetes** utilizando un modelo de **Machine Learning (Random Forest)** entrenado sobre datasets clínicos reales. Incluye un notebook de análisis completo y una **interfaz web interactiva con Gradio** para realizar predicciones en tiempo real.

---

## Objetivo del Proyecto

Proveer una herramienta de **screening médico no invasivo**, capaz de estimar el **riesgo de diabetes** de una persona mediante variables demográficas, historial médico y biomarcadores clínicos.  
Este sistema **no reemplaza un diagnóstico profesional**, pero sirve como apoyo para una detección temprana que permita una intervención médica oportuna.

---

## Arquitectura General del Sistema

1. **Módulo de Análisis de Datos**  
   Preprocesamiento, limpieza, análisis exploratorio y visualización.

2. **Motor de Machine Learning**  
   Modelo Random Forest entrenado, evaluado e interpretado.

3. **Interfaz Web (Gradio)**  
   Aplicación moderna e intuitiva para ingreso de datos y obtención de resultados.

4. **Sistema de Predicción IA**  
   Generación de probabilidades de riesgo y recomendaciones asociadas.

---

## Estructura del Repositorio

- `Detección y Tratamiento de Diabetes Mellitus mediante el modelo Random Forest.ipynb`  
  Notebook principal con todo el flujo: EDA, preprocesamiento, entrenamiento, métricas, exportación del modelo.

- `app.py`  
  Aplicación web en Gradio para realizar predicciones.

- `Datasets/diabetes_prediction_dataset.csv`  
  Dataset principal usado para entrenamiento.

- `Datasets/diabetes.csv`  
  Dataset alternativo o complementario.

- `dataset.csv`  
  Archivo local de trabajo.

---

## Dataset Utilizado

### Dataset Principal: `diabetes_prediction_dataset.csv`
- **100,000 registros**
- **9 variables** clínicas y demográficas
- **Desbalance moderado** (8.5% casos positivos)

### Variables de Entrada

#### Datos Demográficos
- `Gender` — Género  
- `Age` — Edad  

#### Historial Médico
- `Hypertension`  
- `Heart Disease`  
- `Smoking History` (6 categorías)

#### Biomarcadores Clínicos
- `BMI`  
- `HbA1c`  
- `Blood Glucose Level`

---

## Algoritmo de Machine Learning

### Random Forest Classifier
**Ventajas:**
- Alta precisión  
- Robusto ante datos ruidosos  
- Funciona bien con variables mixtas  
- Evita overfitting  
- Permite interpretar características más importantes

### Proceso de Entrenamiento
1. División estratificada: 70% train – 20% test – 10% val  
2. Preprocesamiento y codificación  
3. Optimización de hiperparámetros  
4. Validación cruzada repetida  

---

## Métricas del Modelo

| Métrica       | Resultado |
|---------------|-----------|
| **Accuracy**  | 97.13%    |
| **Precision** | 92.24%    |
| **Recall**    | 58.42%    |
| **F1-Score**  | 71.53%    |

**Interpretación:**  
- Excelente precisión (pocos falsos positivos)  
- Sensibilidad moderada  
- Buen equilibrio general entre métricas  

---

## Interfaz Web Interactiva (Gradio)

### Características
- Inputs validados con rangos reales  
- Controles deslizantes, botones y listas desplegables  
- Resultados con códigos de color  
- Visualización clara del porcentaje de riesgo  

### Flujo de Usuario
1. Ingresar datos clínicos y demográficos  
2. El modelo procesa la información en tiempo real  
3. Se muestra un **porcentaje de riesgo**  
4. Se generan **recomendaciones básicas**  

### Códigos de riesgo
- 🟢 **Verde**: Bajo riesgo  
- 🔴 **Rojo**: Alto riesgo  

---

## Análisis Exploratorio de Datos

### Acciones realizadas
- Eliminación de duplicados (3,854 registros)  
- Limpieza de nulos  
- Estudio de correlaciones  
- Manejo de outliers  
- Codificación categórica y normalización  

---

## Importancia de Variables (Top 4)

1. **Nivel de Glucosa en Sangre**
2. **HbA1c**
3. **IMC**
4. **Edad**

---

## Instalación y Ejecución

### Requisitos
- Python 3.9+
- `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `joblib`, `gradio`

### Crear entorno e instalar dependencias

```powershell
python -m venv .venv
.\.venv\Scripts\Activate

pip install -r requirements.txt
# o instalar manualmente:
pip install pandas numpy scikit-learn matplotlib seaborn joblib gradio