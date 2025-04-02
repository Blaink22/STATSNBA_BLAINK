
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="NBA Stats Analyzer", layout="wide")

st.markdown("# 🧾 Apuesta del Día")
st.markdown("Esta apuesta fue actualizada manualmente por **@BlainkEiou**.")
st.markdown("📬 Ante cualquier duda o sugerencia, contactame por Telegram: [@BlainkEiou](https://t.me/BlainkEiou)")

# Leer archivo si existe
if os.path.exists("apuesta_dia.xlsx"):
    try:
        df_data = pd.read_excel("apuesta_dia.xlsx")
        st.markdown(f"📅 **Última actualización:** {df_data.columns[0]}")
        df_data.columns = df_data.iloc[0]
        df_data = df_data.drop(df_data.index[0])
        df_data = df_data.fillna("")  # ← FIX para evitar NaN

        # Mostrar estilizado sin romper la app si falla
        try:
            st.dataframe(
                df_data.style.set_properties(**{
                    "white-space": "pre-wrap"
                }),
                use_container_width=True,
                hide_index=True
            )
        except Exception:
            st.dataframe(df_data, use_container_width=True, hide_index=True)
    except Exception as e:
        st.error(f"❌ Error al leer 'apuesta_dia.xlsx': {e}")
else:
    st.warning("📂 Aún no se subió ninguna apuesta para hoy.")
