import streamlit as st
import platform

# Diseño personalizado
st.header("Aplicación 2")

def main():
    st.title ("Información del sistema")
    
    system_info = platform.uname()

    st.write("Sistema operativo:", 
    system_info.system), 
    system_info = platform.uname(),
    system_info = platform.un
    system_info = platform
    system_info = system_info
   
    st.write("Versión:", system_info.version)
    st.write("Nombre del nodo:", system_info.node)
    st.write("Arquitectura:", system_info.machine)
    st.write("Procesador:", system_info.processor)

if __name__ == "__main__":
    main()