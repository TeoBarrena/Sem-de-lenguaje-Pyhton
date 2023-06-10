
import streamlit
import pandas as pd
from estadisticas_streamlit import data_set_csv
from estadisticas_streamlit import data_set_json
from estadisticas_streamlit import dias_semana
from estadisticas_streamlit import cantidad_operaciones
from estadisticas_streamlit import porcentajes_genero
from estadisticas_streamlit import cant_operaciones_usuarios

streamlit.set_option('deprecation.showPyplotGlobalUse', False)
streamlit.header('Logs de UNLP Image')

if streamlit.button("Porcentajes por genero"):
    #grafico porcentajes
    streamlit.subheader("Se calculo el porcentaje del genero de los usuarios y en base a esto se hizo el grafico")
    streamlit.pyplot(porcentajes_genero(data_set_json))

if streamlit.button("Operaciones hechas por dia"):

    #grafico cantidad de operaciones por dia
    streamlit.subheader("Grafico que compara los dias de la semana en los que se realizaron operaciones")
    streamlit.pyplot(dias_semana(data_set_csv))

if streamlit.button("Operaciones por usuarios"):
    #grafico que ordena segun el uso de cada operacion
    streamlit.subheader("Grafico que compara entre las operaciones hechas por los usuarios")
    streamlit.pyplot(cantidad_operaciones(data_set_csv))

if streamlit.button("Cantidad de operaciones de cada usuario"):
    streamlit.pyplot(cant_operaciones_usuarios(data_set_csv))