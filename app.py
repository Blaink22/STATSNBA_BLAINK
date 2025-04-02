import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="NBA Stats Analyzer", layout="wide")

tabs = st.tabs(["Dobles Realizados", "Dobles Intentados", "Estadísticas Completas"])

with tabs[0]:
    st.markdown("### 🎯 Dobles Realizados")

    if "data_realizados" not in st.session_state:
        st.session_state["data_realizados"] = pd.DataFrame({
            "Puntos": [None]*10,
            "Triples": [None]*10,
            "Libres": [None]*10
        })

    data_input = st.data_editor(st.session_state["data_realizados"], num_rows="fixed", key="realizados")

    if st.button("🧹 Borrar datos", key="clear_realizados"):
        st.session_state["data_realizados"] = pd.DataFrame({
            "Puntos": [None]*10,
            "Triples": [None]*10,
            "Libres": [None]*10
        })
        st.success("Datos reiniciados correctamente.")
        st.experimental_rerun()

    try:
        df = data_input.copy()
        df = df.astype(float)
        df["Dobles"] = (df["Puntos"] - df["Triples"] * 3 - df["Libres"]) / 2
        st.dataframe(df.style.format(precision=1))
    except Exception:
        pass

with tabs[1]:
    st.markdown("### 🏹 Dobles Intentados")

    if "data_intentados" not in st.session_state:
        st.session_state["data_intentados"] = pd.DataFrame({
            "FGA (Tiros de campo intentados)": [None]*10,
            "Triples intentados": [None]*10
        })

    data_input2 = st.data_editor(st.session_state["data_intentados"], num_rows="fixed", key="intentados")

    if st.button("🧹 Borrar datos", key="clear_intentados"):
        st.session_state["data_intentados"] = pd.DataFrame({
            "FGA (Tiros de campo intentados)": [None]*10,
            "Triples intentados": [None]*10
        })
        st.success("Datos reiniciados correctamente.")
        st.experimental_rerun()

    try:
        df2 = data_input2.copy()
        df2 = df2.astype(float)
        df2["Dobles Intentados"] = df2["FGA (Tiros de campo intentados)"] - df2["Triples intentados"]
        st.dataframe(df2.style.format(precision=1))
    except Exception:
        pass

with tabs[2]:
    st.markdown("### 📊 Estadísticas Completas (Carga manual)")

    if "data_completas" not in st.session_state:
        st.session_state["data_completas"] = pd.DataFrame({
            "Puntos": [None]*10,
            "Triples": [None]*10,
            "Libres": [None]*10,
            "FGA": [None]*10,
            "3PT INT": [None]*10
        })

    data_input3 = st.data_editor(st.session_state["data_completas"], num_rows="fixed", key="completas")

    if st.button("🧹 Borrar datos", key="clear_completas"):
        st.session_state["data_completas"] = pd.DataFrame({
            "Puntos": [None]*10,
            "Triples": [None]*10,
            "Libres": [None]*10,
            "FGA": [None]*10,
            "3PT INT": [None]*10
        })
        st.success("Datos reiniciados correctamente.")
        st.experimental_rerun()

    try:
        df3 = data_input3.copy()
        df3 = df3.astype(float)
        df3["Dobles Realizados"] = (df3["Puntos"] - df3["Triples"] * 3 - df3["Libres"]) / 2
        df3["Dobles Intentados"] = df3["FGA"] - df3["3PT INT"]
        st.dataframe(df3.style.format(precision=1))
    except Exception:
        pass