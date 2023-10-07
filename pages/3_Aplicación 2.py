import streamlit as st
import math

# Diseño personalizado
st.header("Aplicación 2")

result = st.header("");

def calcular_raiz_cuadrada(numero):
    return math.sqrt(numero)


st.title("Calculadora de Raíz Cuadrada")
numero = st.number_input("Ingresa un número para calcular su raíz cuadrada:")


if st.button("Calcular"):
    resultado = calcular_raiz_cuadrada(numero)
    st.write(f"La raíz cuadrada de {numero} es {resultado}")
    resultado = calcular_raiz_cuadrada(numero)
    result.text(resultado)
    
    

   

