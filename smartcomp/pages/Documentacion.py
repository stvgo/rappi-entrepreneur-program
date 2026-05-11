#!/usr/bin/env python3
import streamlit as st
from pathlib import Path

def read_md(fp):
    with open(fp, "r", encoding="utf-8") as f:
        return f.read()

st.set_page_config(page_title="Documentación", page_icon="📚", layout="wide")
st.markdown("<h1 style='text-align:center;color:#FF6600'>📚 Documentación</h1>", unsafe_allow_html=True)

st.page_link("smartcomp_app.py", label="⬅️ Volver al Comparador")

docs_dir = Path(__file__).parent.parent / "docs"
docs = sorted([f for f in docs_dir.glob("*.md")])

labels = {
    "01_Plan_Recoleccion_Datos.md": "📋 Plan de Recolección de Datos (2.1)",
    "02_Top_5_Insights.md": "💡 Top 6 Insights Accionables (2.3)",
    "03_Documento_Ejecutivo.md": "📊 Documento Ejecutivo",
    "04_Exportable_IA_AI_First.md": "🤖 Proceso AI-First (5)",
    "05_Analisis_Promociones.md": "🎯 Análisis de Promociones",
}

selected = st.selectbox("Selecciona un documento", [labels.get(d.name, d.name) for d in docs])
selected_doc = next((d for d in docs if labels.get(d.name, d.name) == selected), None)

if selected_doc:
    st.markdown(f"### {selected}")
    st.markdown(read_md(selected_doc))
