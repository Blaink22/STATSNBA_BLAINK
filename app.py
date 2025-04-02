
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="NBA Stats Analyzer", layout="wide")
st.title("🏀 NBA Stats Analyzer")

tabs = st.tabs(["Dobles Realizados", "Dobles Intentados", "Estadísticas Completas", "Apuesta del Día"])

# --- Dobles Realizados ---
with tabs[0]:
    st.header("🎯 Dobles Realizados")
    data = pd.DataFrame({"Puntos": [None]*10, "Triples": [None]*10, "Libres": [None]*10})
    df = st.data_editor(data, num_rows="fixed", use_container_width=True, key="dobles_realizados")
    if df.dropna().shape[0] < 10:
        st.info("Por favor completá los 10 partidos para continuar.")
    else:
        df["Dobles"] = (df["Puntos"] - df["Triples"]*3 - df["Libres"]) / 2
        linea = st.number_input("Línea a evaluar (dobles)", min_value=0.0, step=0.5)
        aciertos = (df["Dobles"] > linea).sum()
        st.success(f"Aciertos: {aciertos}/10")

# --- Dobles Intentados ---
with tabs[1]:
    st.header("🏹 Dobles Intentados")
    data = pd.DataFrame({"F.G.A": [None]*10, "3PT ATT": [None]*10})
    df = st.data_editor(data, num_rows="fixed", use_container_width=True, key="dobles_intentados")
    if df.dropna().shape[0] < 10:
        st.info("Por favor completá los 10 partidos para continuar.")
    else:
        df["Dobles Intentados"] = (df["F.G.A"] - df["3PT ATT"] * 3) / 2
        linea = st.number_input("Línea a evaluar (dobles intentados)", min_value=0.0, step=0.5)
        aciertos = (df["Dobles Intentados"] > linea).sum()
        st.success(f"Aciertos: {aciertos}/10")

# --- Estadísticas Completas ---
with tabs[2]:
    st.header("📊 Estadísticas Completas (Carga manual)")
    data = pd.DataFrame({
        "Puntos": [None]*10, "Triples": [None]*10, "Libres": [None]*10,
        "FGA": [None]*10, "3PT INT": [None]*10
    })
    df = st.data_editor(data, num_rows="fixed", use_container_width=True, key="stats_completas")
    if df.dropna().shape[0] < 10:
        st.info("Cargá los datos de 10 partidos para continuar.")
    else:
        df["Dobles Realizados"] = (df["Puntos"] - df["Triples"]*3 - df["Libres"]) / 2
        df["Dobles Intentados"] = (df["FGA"] - df["3PT INT"]*3) / 2
        st.dataframe(df, use_container_width=True)

# --- Apuesta del Día ---
with tabs[3]:
    st.header("📝 Apuesta del Día")
    st.markdown("Esta apuesta fue actualizada manualmente por **@BlainkEiou**.")
    st.markdown("📬 Ante cualquier duda o sugerencia, contactame por Telegram: [@BlainkEiou](https://t.me/BlainkEiou)")

    try:
        if os.path.exists("apuesta_dia.xlsx"):
            df_apuesta = pd.read_excel("apuesta_dia.xlsx", engine="openpyxl")
            df_apuesta = df_apuesta.fillna("")
            st.markdown("🗓️ **Última actualización:** 2025-03-19 00:00:00")
            st.dataframe(df_apuesta, use_container_width=True, hide_index=True)
        else:
            st.info("No se encontró una apuesta del día. Subí el archivo `apuesta_dia.xlsx` al repositorio.")
    except Exception as e:
        st.error(f"Ocurrió un error al leer la apuesta del día: {e}")
