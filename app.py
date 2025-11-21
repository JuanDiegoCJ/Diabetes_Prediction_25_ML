import gradio as gr
import pandas as pd
import joblib

# Cargar el modelo entrenado
rf_model = joblib.load('rf_model.pkl')

# Función principal de predicción
def predict_diabetes_web(name, gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level):
    gender_map = {"Mujer": 0, "Hombre": 1}
    hypertension_map = {"No": 0, "Sí": 1}
    heart_disease_map = {"No": 0, "Sí": 1}
    smoking_map = {
        "Nunca": 0,
        "Exfumador": 1,
        "Fumador ocasional": 2,
        "Fumador actual": 3
    }

    # Crear DataFrame con los datos convertidos
    input_data = pd.DataFrame({
        'gender': [gender_map[gender]],
        'age': [age],
        'hypertension': [hypertension_map[hypertension]],
        'heart_disease': [heart_disease_map[heart_disease]],
        'smoking_history': [smoking_map[smoking_history]],
        'bmi': [bmi],
        'HbA1c_level': [HbA1c_level],
        'blood_glucose_level': [blood_glucose_level]
    })

    # Realizar predicción y obtener probabilidad
    prediction = rf_model.predict(input_data)[0]
    probability = rf_model.predict_proba(input_data)[0][1] * 100

    if prediction == 1:
        return f"""
        <div style='background-color: #c82333; padding: 20px; border-radius: 10px; color: #ffffff; font-family: Arial;'>
            <h3>{name}, estos son tus resultados:</h3>
            <h3>🔴 Riesgo de diabetes detectado: {probability:.1f}%</h3>
            <p>Consulta con un profesional médico lo antes posible.</p>
            <ul>
                <li>🩺 Programa una cita médica</li>
                <li>🍎 Reduce el consumo de azúcares refinados</li>
                <li>🚶‍♂️ Camina 30 minutos diarios</li>
                <li>📊 Monitorea tus niveles de glucosa</li>
            </ul>
            <em>Detección de Diabetes bajo el modelo de Random Forest 2025</em>
        </div>
        """
    else:
        return f"""
        <div style='background-color: #28a745; padding: 20px; border-radius: 10px; color: #ffffff; font-family: Arial;'>
            <h3>{name}, estos son tus resultados:</h3>
            <h3>🟢 Bajo riesgo de diabetes: {probability:.1f}%</h3>
            <p>¡Sigue cuidando tu salud!</p>
            <ul>
                <li>🥗 Mantén una dieta saludable</li>
                <li>🧘‍♀️ Maneja el estrés adecuadamente</li>
                <li>🏋️‍♂️ Realiza ejercicio físico regular</li>
                <li>💤 Duerme al menos 7-8 horas</li>
            </ul>
            <em>Detección de Diabetes bajo el modelo de Random Forest 2025</em>
        </div>
        """

# Nueva función para calcular IMC dado peso (kg) y altura (cm)
def calcular_imc(peso, altura):
    if altura <= 0:
        return 0
    return round(peso / ((altura / 100) ** 2), 2)

# Interfaz principal con Gradio
with gr.Blocks(theme=gr.themes.Soft(primary_hue="blue", secondary_hue="cyan")) as interface:
    gr.HTML("""
    <div style="text-align:center; padding: 20px;">
        <h1 style="font-size: 2.5em; color: #cee8ff;">🔬 Predicción de Diabetes</h1>
        <p style="color: #cee8ff; font-size: 1.1em;">
            Completa tus datos para conocer tu riesgo según un modelo clínico de ML.
        </p>
    </div>
    """)

    with gr.Row():
        with gr.Column():
            gr.Markdown("### 📍 Datos Demográficos")
            name_input = gr.Textbox(label="Nombre")
            gender = gr.Radio(["Mujer", "Hombre"], label="Género")
            age = gr.Slider(0, 100, step=1, label="Edad")

            gr.Markdown("### 🏥 Historial Médico")
            hypertension = gr.Radio(["No", "Sí"], label="Hipertensión")
            heart_disease = gr.Radio(["No", "Sí"], label="Enfermedad Cardíaca")
            smoking_history = gr.Dropdown(
                ["Nunca", "Exfumador", "Fumador ocasional", "Fumador actual"],
                label="Historial de Tabaquismo"
            )

        with gr.Column():
            gr.Markdown("### 📊 Biomarcadores Clave")
            bmi = gr.Slider(10, 60, step=0.1, label="IMC")  # Campo que se actualizará automáticamente

            HbA1c_level = gr.Slider(3.0, 15.0, step=0.1, label="HbA1c (%)")
            blood_glucose_level = gr.Slider(50, 300, step=1, label="Glucosa en Sangre (mg/dL)")

            # Nuevo bloque para calcular IMC a partir de peso y altura
            gr.Markdown("### ⚖️ Calcula tu IMC")
            peso = gr.Number(label="Peso (kg)")
            altura = gr.Number(label="Altura (cm)")
            calcular_btn = gr.Button("Calcular IMC")

            # Al hacer clic en calcular, el valor calculado se pone directamente en el slider de IMC
            calcular_btn.click(fn=calcular_imc, inputs=[peso, altura], outputs=bmi)

    # Botón para analizar riesgo y HTML para mostrar resultados
    analyze_btn = gr.Button("ANALIZAR RIESGO")
    result = gr.HTML()

    # Ejecutar predicción al hacer clic
    analyze_btn.click(
        fn=predict_diabetes_web,
        inputs=[name_input, gender, age, hypertension, heart_disease,
                smoking_history, bmi, HbA1c_level, blood_glucose_level],
        outputs=result
    )

    # Footer
    gr.HTML("""
    <div style="text-align:center; color:#999; font-size: 0.9em; padding-top: 30px;">
        <p>© 2025 | Esta herramienta fue elaborada con fines educativos. No reemplaza un diagnóstico médico profesional.</p>
    </div>
    """)

# Lanzar la app (uso localmente antes del deploy)
if __name__ == "__main__":
    interface.launch()
