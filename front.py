import streamlit as st
import requests

API_URL = 'https://api-rest-ia.onrender.com/predict/'

def make_prediction(data):
    response = requests.post(API_URL, json=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Error en la solicitud:", response.text)
        return None

def format_currency(value):
    return "${:,.2f}".format(value)

def main():
    st.title('Modelo de Predicción de Precio de Vivienda')

    st.header('Ingrese los datos de la propiedad:')
    
    habitaciones = st.number_input('¿Cuántas habitaciones tiene la vivienda?', min_value=1, max_value=10)
    baños = st.number_input('¿Cuántos baños tiene la vivienda?', min_value=1, max_value=10)
    parqueaderos = st.number_input('¿Cuántos parqueaderos tiene la vivienda?', min_value=0, max_value=10)
    estrato = st.selectbox('¿Cuál es el estrato de la vivienda?', [1, 2, 3, 4, 5, 6])
    ascensor = st.selectbox('¿La vivienda tiene ascensor?', ["No", "Sí"])
    circuito_cerrado_de_TV = st.selectbox('¿La vivienda tiene circuito cerrado de TV?', ["No", "Sí"])
    parqueadero_visitantes = st.selectbox('¿La vivienda tiene parqueadero para visitantes?', ["No", "Sí"])
    porteria_recepcion = st.selectbox('¿La vivienda tiene portería/recepción?', ["No", "Sí"])
    zonas_verdes = st.selectbox('¿La vivienda tiene zonas verdes?', ["No", "Sí"])
    salon_comunal = st.selectbox('¿La vivienda tiene salón comunal?', ["No", "Sí"])
    balcon = st.selectbox('¿La vivienda tiene balcón?', ["No", "Sí"])
    barra_americana = st.selectbox('¿La vivienda tiene barra americana?', ["No", "Sí"])
    calentador = st.selectbox('¿La vivienda tiene calentador?', ["No", "Sí"])
    chimenea = st.selectbox('¿La vivienda tiene chimenea?', ["No", "Sí"])
    citafono = st.selectbox('¿La vivienda tiene citófono?', ["No", "Sí"])
    cocina_integral = st.selectbox('¿La vivienda tiene cocina integral?', ["No", "Sí"])
    terraza = st.selectbox('¿La vivienda tiene terraza?', ["No", "Sí"])
    vigilancia = st.selectbox('¿La vivienda tiene vigilancia?', ["No", "Sí"])
    parques_cercanos = st.selectbox('¿La vivienda tiene parques cercanos?', ["No", "Sí"])
    estudio = st.selectbox('¿La vivienda tiene estudio?', ["No", "Sí"])
    patio = st.selectbox('¿La vivienda tiene patio?', ["No", "Sí"])
    bodega = st.selectbox('¿La vivienda cuenta con bodega?', ["No", "Sí"])
    nombre = st.selectbox('¿Cuál es el tipo de la vivienda?', ["Apartamento", "Casa"])

    antiguedad = st.selectbox('¿Cuál es la antigüedad de la vivienda?', 
                              ["Menor a 1 año", "De 1 a 8 años", "De 9 a 15 años", "De 16 a 30 años", "Más de 30 años", "No definida"])

    if st.button('Predecir'):
        input_data = {
            'habitaciones': habitaciones,
            'baños': baños,
            'parqueaderos': parqueaderos,
            'estrato': estrato,
            'ascensor': 1 if ascensor == "Sí" else 0,
            'circuito_cerrado_de_TV': 1 if circuito_cerrado_de_TV == "Sí" else 0,
            'parqueadero_visitantes': 1 if parqueadero_visitantes == "Sí" else 0,
            'porteria_recepcion': 1 if porteria_recepcion == "Sí" else 0,
            'zonas_verdes': 1 if zonas_verdes == "Sí" else 0,
            'salon_comunal': 1 if salon_comunal == "Sí" else 0,
            'balcon': 1 if balcon == "Sí" else 0,
            'barra_americana': 1 if barra_americana == "Sí" else 0,
            'calentador': 1 if calentador == "Sí" else 0,
            'chimenea': 1 if chimenea == "Sí" else 0,
            'citafono': 1 if citafono == "Sí" else 0,
            'cocina_integral': 1 if cocina_integral == "Sí" else 0,
            'terraza': 1 if terraza == "Sí" else 0,
            'vigilancia': 1 if vigilancia == "Sí" else 0,
            'parques_cercanos': 1 if parques_cercanos == "Sí" else 0,
            'estudio': 1 if estudio == "Sí" else 0,
            'patio': 1 if patio == "Sí" else 0,
            'bodega': 1 if bodega == "Sí" else 0,
            'nombre': nombre,
            'de_1_a_8años': antiguedad == "De 1 a 8 años",
            'de_16_a_30_años': antiguedad == "De 16 a 30 años",
            'de_9_a_15_años': antiguedad == "De 9 a 15 años",
            'no_definida': antiguedad == "No definida",
            'menor_a_1_año': antiguedad == "Menor a 1 año",
            'mas_de_30_años': antiguedad == "Más de 30 años"
        }

        prediction = make_prediction(input_data)

        if prediction is not None:
            formatted_currency = format_currency(prediction)
            st.write('El precio predicho es:', formatted_currency)

if __name__ == '__main__':
    main()
