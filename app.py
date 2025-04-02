
import streamlit as st
import pandas as pd

st.set_page_config(page_title="NBA Stats Analyzer", layout="wide")
st.title("🏀 NBA Stats Analyzer")

tabs = st.tabs(["Dobles Realizados", "Dobles Intentados", "Estadísticas Completas", "Apuesta del Día"])

# Utilidad: resetear datos
def reset_dataframe(columns, key):
    if st.button("🗑️ Borrar datos", key=f"reset_{key}"):
        st.session_state[key] = pd.DataFrame({col: [None]*10 for col in columns})
        st.success("✅ Datos reiniciados correctamente")
    return st.session_state.get(key, pd.DataFrame({col: [None]*10 for col in columns}))

# --- Dobles Realizados ---
with tabs[0]:
    st.header("🎯 Dobles Realizados")
    columns = ["Puntos", "Triples", "Libres"]
    df = reset_dataframe(columns, "dobles_realizados")

    df = st.data_editor(df, use_container_width=True, num_rows="fixed", key="dobles_realizados_editor")

    if df.dropna().shape[0] == 10:
        df["Puntos"] = pd.to_numeric(df["Puntos"], errors="coerce")
        df["Triples"] = pd.to_numeric(df["Triples"], errors="coerce")
        df["Libres"] = pd.to_numeric(df["Libres"], errors="coerce")
        df = df.dropna(subset=["Puntos", "Triples", "Libres"])
        df["Dobles"] = (df["Puntos"] - df["Triples"] * 3 - df["Libres"]) / 2
        st.dataframe(df, use_container_width=True)
        linea = st.number_input("🔢 Línea a evaluar", min_value=0.0, step=0.5, key="linea_realizados")
        aciertos = (df["Dobles"] > linea).sum()
        st.success(f"Aciertos: {aciertos}/10")

# --- Dobles Intentados ---
with tabs[1]:
    st.header("🏹 Dobles Intentados")
    columns = ["FGA (Tiros de campo intentados)", "Triples intentados"]
    df = reset_dataframe(columns, "dobles_intentados")

    df = st.data_editor(df, use_container_width=True, num_rows="fixed", key="dobles_intentados_editor")

    if df.dropna().shape[0] == 10:
        df[columns[0]] = pd.to_numeric(df[columns[0]], errors="coerce")
        df[columns[1]] = pd.to_numeric(df[columns[1]], errors="coerce")
        df = df.dropna()
        df["Dobles Intentados"] = df[columns[0]] - df[columns[1]]
        st.dataframe(df, use_container_width=True)
        linea = st.number_input("🔢 Línea a evaluar", min_value=0.0, step=0.5, key="linea_intentados")
        aciertos = (df["Dobles Intentados"] > linea).sum()
        st.success(f"Aciertos: {aciertos}/10")

# --- Estadísticas Completas ---
with tabs[2]:
    st.header("📊 Estadísticas Completas (Carga manual)")
    columns = ["Puntos", "Triples", "Libres", "FGA", "3PT INT"]
    df = reset_dataframe(columns, "completas")

    df = st.data_editor(df, use_container_width=True, num_rows="fixed", key="completas_editor")
    st.markdown("Esta sección es informativa. No realiza cálculos por ahora.")

# --- Apuesta del Día ---
with tabs[3]:
    st.header("📝 Apuesta del Día")
    st.markdown("Esta apuesta fue actualizada manualmente por **@BlainkEiou**.")
    st.markdown("📬 Ante cualquier duda o sugerencia, contactame por Telegram: [@BlainkEiou](https://t.me/BlainkEiou)")
    st.markdown("📅 **Última actualización:** 2025-03-19 00:00:00")
    try:
        df_apuesta = pd.read_excel("apuesta_dia.xlsx", engine="openpyxl")
        df_apuesta = df_apuesta.fillna("")
        st.dataframe(df_apuesta, use_container_width=True, hide_index=True)
    except Exception as e:
        st.error(f"Error al leer la apuesta del día: {e}")
