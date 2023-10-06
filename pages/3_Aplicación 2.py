import streamlit as st
import platform

# Diseño personalizado
st.header("Aplicación 2")

st.number_input 
def main():
    system_info = platform.uname()
    
    print("Información del sistema:")
    print(f"Sistema operativo: {system_info.system}")
    print(f"Versión: {system_info.version}")
    print(f"Nombre del nodo: {system_info.node}")
    print(f"Arquitectura: {system_info.machine}")
    print(f"Procesador: {system_info.processor}")

if __name__ == "__main__":
    main()