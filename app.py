
import streamlit as st
import pandas as pd

st.set_page_config(page_title="NBA Stats Analyzer", layout="wide")
st.title("🏀 NBA Stats Analyzer")

tabs = st.tabs(["Dobles Realizados", "Dobles Intentados", "Estadísticas Completas"])

# Datos iniciales vacíos
def create_empty_df_realizados():
    return pd.DataFrame({ "Puntos": [None]*10, "Triples": [None]*10, "Libres": [None]*10 })

def create_empty_df_intentados():
    return pd.DataFrame({ "FGA (Tiros de campo intentados)": [None]*10, "Triples intentados": [None]*10 })

def create_empty_df_completas():
    return pd.DataFrame({ "Puntos": [None]*10, "Triples": [None]*10, "Libres": [None]*10, "FGA": [None]*10, "3PT INT": [None]*10 })

# Session state inicialización
if "realizados_df" not in st.session_state:
    st.session_state.realizados_df = create_empty_df_realizados()
if "intentados_df" not in st.session_state:
    st.session_state.intentados_df = create_empty_df_intentados()
if "completas_df" not in st.session_state:
    st.session_state.completas_df = create_empty_df_completas()

# DOBLES REALIZADOS
with tabs[0]:
    st.header("🎯 Dobles Realizados")
    if st.button("🧹 Borrar datos", key="reset_realizados"):
        st.session_state.realizados_df = create_empty_df_realizados()
        st.success("Datos reiniciados correctamente")

    df = st.data_editor(st.session_state.realizados_df, num_rows="fixed", use_container_width=True, key="editor_realizados")

    if df.dropna().shape[0] == 10:
        df["Dobles"] = (df["Puntos"] - df["Triples"] * 3 - df["Libres"]) / 2
        st.dataframe(df, use_container_width=True)

# DOBLES INTENTADOS
with tabs[1]:
    st.header("🎯 Dobles Intentados")
    if st.button("🧹 Borrar datos", key="reset_intentados"):
        st.session_state.intentados_df = create_empty_df_intentados()
        st.success("Datos reiniciados correctamente")

    df2 = st.data_editor(st.session_state.intentados_df, num_rows="fixed", use_container_width=True, key="editor_intentados")

    if df2.dropna().shape[0] == 10:
        df2["Dobles Intentados"] = df2["FGA (Tiros de campo intentados)"] - df2["Triples intentados"]
        st.dataframe(df2, use_container_width=True)

# ESTADÍSTICAS COMPLETAS
with tabs[2]:
    st.header("📊 Estadísticas Completas (Carga manual)")
    if st.button("🧹 Borrar datos", key="reset_completas"):
        st.session_state.completas_df = create_empty_df_completas()
        st.success("Datos reiniciados correctamente")

    df3 = st.data_editor(st.session_state.completas_df, num_rows="fixed", use_container_width=True, key="editor_completas")

    if df3.dropna().shape[0] == 10:
        df3["Dobles Realizados"] = (df3["Puntos"] - df3["Triples"] * 3 - df3["Libres"]) / 2
        df3["Dobles Intentados"] = df3["FGA"] - df3["3PT INT"]
        st.dataframe(df3, use_container_width=True)
