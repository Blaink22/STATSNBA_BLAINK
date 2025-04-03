import streamlit as st
import pandas as pd

st.set_page_config(page_title="NBA Stats Analyzer", layout="wide")
st.title("🏀 NBA Stats Analyzer")

tabs = st.tabs(["Dobles Realizados", "Dobles Intentados", "Estadísticas Completas", "Apuesta del Día"])

with tabs[0]:
    st.header("🎯 Dobles Realizados")
    df = pd.DataFrame({
        "Puntos": [None]*10,
        "Triples": [None]*10,
        "Libres": [None]*10
    })
    df = st.data_editor(df, use_container_width=True, num_rows="fixed", key="dobles_realizados")

    if df.dropna().shape[0] == 10:
        df["Puntos"] = pd.to_numeric(df["Puntos"], errors="coerce")
        df["Triples"] = pd.to_numeric(df["Triples"], errors="coerce")
        df["Libres"] = pd.to_numeric(df["Libres"], errors="coerce")
        df = df.dropna(subset=["Puntos", "Triples", "Libres"])
        df["Dobles"] = (df["Puntos"] - df["Triples"] * 3 - df["Libres"]) / 2
        st.dataframe(df, use_container_width=True)
        linea = st.number_input("🔢 Línea a evaluar", min_value=0.0, step=0.5)
        aciertos = (df["Dobles"] > linea).sum()
        st.success(f"Aciertos: {aciertos}/10" if aciertos > 6 else
                   f"Aciertos: {aciertos}/10", icon="✅" if aciertos > 6 else "⚠️")

with tabs[1]:
    st.header("🎯 Dobles Intentados")
    df = pd.DataFrame({
        "FGA (Tiros de campo intentados)": [None]*10,
        "Triples intentados": [None]*10
    })
    df = st.data_editor(df, use_container_width=True, num_rows="fixed", key="dobles_intentados")

    if df.dropna().shape[0] == 10:
        df["FGA (Tiros de campo intentados)"] = pd.to_numeric(df["FGA (Tiros de campo intentados)"], errors="coerce")
        df["Triples intentados"] = pd.to_numeric(df["Triples intentados"], errors="coerce")
        df = df.dropna()
        df["Dobles Intentados"] = df["FGA (Tiros de campo intentados)"] - df["Triples intentados"]
        st.dataframe(df, use_container_width=True)
        linea = st.number_input("🔢 Línea a evaluar", min_value=0.0, step=0.5, key="linea_int")
        aciertos = (df["Dobles Intentados"] > linea).sum()
        st.success(f"Aciertos: {aciertos}/10" if aciertos > 6 else
                   f"Aciertos: {aciertos}/10", icon="✅" if aciertos > 6 else "⚠️")

with tabs[2]:
    st.header("📊 Estadísticas Completas (Carga manual)")
    df = pd.DataFrame({
        "Puntos": [None]*10,
        "Triples": [None]*10,
        "Libres": [None]*10,
        "FGA": [None]*10,
        "3PT INT": [None]*10
    })
    df = st.data_editor(df, use_container_width=True, num_rows="fixed", key="completo")
    st.markdown("Esta sección es informativa. No realiza cálculos por ahora.")

with tabs[3]:
    st.header("📝 Apuesta del Día")
    st.markdown("Esta apuesta fue actualizada manualmente por **@BlainkEiou**.")
    st.markdown("📬 Ante cualquier duda o sugerencia, contactame por Telegram: [@BlainkEiou](https://t.me/BlainkEiou)")
    st.markdown("📅 **Última actualización:** 2025-04-03 17:35hs")
    try:
        df_apuesta = pd.read_excel("apuesta_dia.xlsx", engine="openpyxl")
        st.table(df_apuesta)
    except Exception as e:
        st.error(f"Error al leer la apuesta del día: {e}")
