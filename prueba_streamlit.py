import streamlit as st
import pandas as pd
from estadisticas_streamlit import data_set_csv
from estadisticas_streamlit import data_set_json
from estadisticas_streamlit import dias_semana
from estadisticas_streamlit import cantidad_operaciones
from estadisticas_streamlit import porcentajes_genero

st.set_option('deprecation.showPyplotGlobalUse', False)
st.header('Logs de UNLP Image')

if st.button("Porcentajes por genero"):
    #grafico porcentajes
    st.subheader("Se calculo el porcentaje del genero de los usuarios y en base a esto se hizo el grafico")
    st.pyplot(porcentajes_genero(data_set_json))

if st.button("Operaciones hechas por dia"):

    #grafico cantidad de operaciones por dia
    st.subheader("Grafico que compara los dias de la semana en los que se realizaron operaciones")
    st.pyplot(dias_semana(data_set_csv))

if st.button("Operaciones por usuarios"):
    #grafico que ordena segun el uso de cada operacion
    st.subheader("Grafico que compara entre las operaciones hechas por los usuarios")
    st.pyplot(cantidad_operaciones(data_set_csv))
