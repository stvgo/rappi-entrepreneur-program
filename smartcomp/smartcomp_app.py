#!/usr/bin/env python3
"""
SmartComp - Asistente Inteligente de Comparación de Precios
Rappi Entrepreneur Program
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import requests
import json
import os

st.set_page_config(
    page_title="SmartComp - Comparador Inteligente",
    page_icon="🛵",
    layout="wide",
    initial_sidebar_state="expanded",
)

@st.cache_data
def load_data():
    return pd.read_csv(Path(__file__).parent / "products_data.csv")

df = load_data()

st.markdown("""
<style>
    .stApp, .main, .block-container { background-color: #ffffff !important; }
    body, p, div, span, label, li { color: #1a1a2e !important; }
    h1, h2, h3, h4, h5, h6 { color: #1a1a2e !important; }
    [data-testid="stSidebar"] { background: #f8fafc !important; border-right: 1px solid #e2e8f0; }
</style>
""", unsafe_allow_html=True)

def analyze_with_openrouter(product, zone, rappi_data, uber_data, didi_data, api_key, model):
    system_msg = """Eres un analista estratégico de Rappi. Analiza comparaciones de precios y da recomendaciones accionables."""
    user_msg = f"""Producto: {product}, Zona: {zone}
Rappi: ${rappi_data['product_price']} MXN producto + ${rappi_data['delivery_fee']} MXN envío + ${rappi_data['service_fee']} MXN service = ${rappi_data['final_total']} MXN total, Promo: {rappi_data['promo']}
Uber Eats: ${uber_data['product_price']} MXN producto + ${uber_data['delivery_fee']} MXN envío + ${uber_data['service_fee']} MXN service = ${uber_data['final_total']} MXN total, Promo: {uber_data['promo']}
DiDi Food: ${didi_data['product_price']} MXN producto + ${didi_data['delivery_fee']} MXN envío + ${didi_data['service_fee']} MXN service = ${didi_data['final_total']} MXN total, Promo: {didi_data['promo']}

Responde en formato:
ANALISIS: [breve]
RECOMENDACION: [específica]
IMPACTO: [% estimado]
PRIORIDAD: [Alta/Media/Baja]"""
    try:
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_msg}
            ],
            "temperature": 0.5,
            "max_tokens": 600
        }
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json; charset=utf-8",
                "HTTP-Referer": "https://smartcomp-rappi.app",
                "X-Title": "SmartComp"
            },
            data=json.dumps(payload, ensure_ascii=False).encode('utf-8'),
            timeout=30
        )
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"], None
        else:
            return None, f"Error: {response.status_code}"
    except Exception as e:
        return None, f"Error: {str(e)}"

def local_analyze(product, zone, df_filtered):
    rappi = df_filtered[df_filtered["competitor"] == "Rappi"].iloc[0]
    uber = df_filtered[df_filtered["competitor"] == "Uber Eats"].iloc[0]
    didi = df_filtered[df_filtered["competitor"] == "DiDi Food"].iloc[0]
    
    findings = []
    recommendations = []
    actions = []
    
    totals = {"Rappi": rappi["final_total"], "Uber Eats": uber["final_total"], "DiDi Food": didi["final_total"]}
    cheapest = min(totals, key=totals.get)
    gap_rappi = rappi["final_total"] - totals[cheapest]
    gap_pct = (gap_rappi / totals[cheapest]) * 100 if totals[cheapest] > 0 else 0
    
    findings.append(f"💰 **Precio Total:** Rappi ${rappi['final_total']} MXN vs {cheapest} ${totals[cheapest]} MXN")
    
    if cheapest == "Rappi":
        findings.append("🟢 **Rappi es la opción más barata** en esta zona.")
        recommendations.append("✅ Mantener estrategia actual.")
        actions.append("- Capitalizar con badge 'Mejor precio' en la app")
    else:
        findings.append(f"🔴 **Rappi es ${gap_rappi} MXN más caro** ({gap_pct:.1f}% más caro que {cheapest})")
        if rappi["delivery_fee"] > uber["delivery_fee"]:
            diff = rappi["delivery_fee"] - uber["delivery_fee"]
            findings.append(f"📦 **Delivery Fee:** Rappi ${rappi['delivery_fee']} MXN vs Uber ${uber['delivery_fee']} MXN (+${diff} MXN)")
        if gap_pct > 15:
            recommendations.append("🚨 **GAP CRÍTICO (>15%):** Rappi está significativamente más caro.")
            actions.append(f"- Reducir delivery fee de ${rappi['delivery_fee']} MXN a ${rappi['delivery_fee'] - 5} MXN en {zone}")
        elif gap_pct > 8:
            recommendations.append("⚠️ **GAP MODERADO (8-15%):** Ajustes menores recuperan competitividad.")
            actions.append(f"- Reducir delivery fee de ${rappi['delivery_fee']} MXN a ${rappi['delivery_fee'] - 3} MXN")
        else:
            recommendations.append("🟡 **GAP MENOR (<8%):** Pequeños ajustes lo pondrán primero.")
            actions.append(f"- Reducir delivery fee de ${rappi['delivery_fee']} MXN a ${rappi['delivery_fee'] - 2} MXN")
    
    return findings, recommendations, actions, rappi, uber, didi

st.markdown('<h1 style="text-align:center;color:#FF6600">🛵 SmartComp</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center;color:#475569">Comparador Inteligente — Rappi vs Uber Eats vs DiDi Food</p>', unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🎯 Configuración")
    zones = sorted(df["zone"].unique())
    products = sorted(df["product"].unique())
    selected_zone = st.selectbox("📍 Zona", zones)
    selected_product = st.selectbox("🍔 Producto", products)
    st.markdown("---")
    st.markdown("### 🔑 OpenRouter API")
    api_key = st.text_input("API Key (gratis)", value=os.getenv("OPENROUTER_API_KEY", ""), type="password", placeholder="sk-or-v1-...")
    if os.getenv("OPENROUTER_API_KEY"):
        st.success("✅ API key cargada desde variable de entorno")
    model = st.text_input("Modelo", value="nvidia/nemotron-3-super-120b-a12b:free")
    st.markdown("---")
    st.markdown("### 📚 Documentación")
    st.page_link("pages/Documentacion.py", label="Ver Documentación", icon="📄")

st.markdown("---")
st.markdown(f"## 📍 Análisis: **{selected_product}** en **{selected_zone}**")

df_filtered = df[(df["zone"] == selected_zone) & (df["product"] == selected_product)]

if len(df_filtered) == 0:
    st.error("No se encontraron datos.")
    st.stop()

findings, recommendations, actions, rappi, uber, didi = local_analyze(selected_product, selected_zone, df_filtered)

if api_key and st.button("🤖 Analizar con IA", use_container_width=True, type="primary"):
    with st.spinner("Analizando con IA..."):
        ai_response, error = analyze_with_openrouter(
            selected_product, selected_zone,
            dict(rappi), dict(uber), dict(didi),
            api_key, model
        )
    if ai_response:
        st.markdown("### 🤖 Análisis de IA")
        st.code(ai_response, language=None)
    else:
        st.warning(f"AI no disponible: {error}. Usando análisis local...")

# Tarjetas de precios
col1, col2, col3 = st.columns(3)
for col, data, name, color in [(col1, rappi, "🛵 RAPPI", "#FF6600"), (col2, uber, "🚗 UBER EATS", "#276EF1"), (col3, didi, "🚕 DIDI FOOD", "#FF6600")]:
    with col:
        st.markdown(f"""
        <div style="background:{color};padding:20px;border-radius:12px;color:white;text-align:center;margin-bottom:10px">
            <h3 style="color:white!important">{name}</h3>
            <h1 style="color:white!important">${data['final_total']} MXN</h1>
            <p>Producto: ${data['product_price']} MXN<br>
            Envío: ${data['delivery_fee']} MXN<br>
            Service: ${data['service_fee']} MXN<br>
            Promo: {data['promo']}</p>
        </div>
        """, unsafe_allow_html=True)

# Gráfico barras apiladas
fig = go.Figure(data=[
    go.Bar(name='Producto', x=['Rappi','Uber Eats','DiDi Food'], 
           y=[rappi['product_price'], uber['product_price'], didi['product_price']], 
           marker_color='#FF6B00'),
    go.Bar(name='Envío', x=['Rappi','Uber Eats','DiDi Food'], 
           y=[rappi['delivery_fee'], uber['delivery_fee'], didi['delivery_fee']], 
           marker_color='#FFB366'),
    go.Bar(name='Service', x=['Rappi','Uber Eats','DiDi Food'], 
           y=[rappi['service_fee'], uber['service_fee'], didi['service_fee']], 
           marker_color='#FFD9B3'),
])
fig.update_layout(
    barmode='stack', 
    title='Desglose de Costos por Plataforma',
    yaxis_title='MXN',
    plot_bgcolor='#ffffff', 
    paper_bgcolor='#ffffff',
    font=dict(color="#1a1a2e")
)
st.plotly_chart(fig, use_container_width=True)

# Gráfico precio final
fig2 = go.Figure(data=[
    go.Bar(x=['Rappi', 'Uber Eats', 'DiDi Food'], 
           y=[rappi['final_total'], uber['final_total'], didi['final_total']],
           marker_color=['#FF6600', '#276EF1', '#FF6600'],
           text=[f"${rappi['final_total']} MXN", f"${uber['final_total']} MXN", f"${didi['final_total']} MXN"],
           textposition='outside')
])
fig2.update_layout(
    title='Precio Final Comparativo',
    yaxis_title='MXN',
    plot_bgcolor='#ffffff', 
    paper_bgcolor='#ffffff',
    showlegend=False
)
st.plotly_chart(fig2, use_container_width=True)

# Insights
st.markdown("---")
st.markdown("### 📊 Análisis Inteligente")
for finding in findings:
    st.markdown(finding)
for rec in recommendations:
    st.markdown(f"**{rec}**")

st.markdown("---")
st.markdown("### ✅ Acciones Recomendadas")
for action in actions:
    st.markdown(action)

# Simulador
st.markdown("---")
st.markdown("### 🎮 Simulador de Escenarios")
col_s1, col_s2 = st.columns(2)
with col_s1:
    new_delivery = st.slider("Nuevo Delivery Fee", 
                             min_value=max(5, int(rappi['delivery_fee'] - 15)),
                             max_value=int(rappi['delivery_fee'] + 10),
                             value=int(rappi['delivery_fee']))
with col_s2:
    new_promo = st.selectbox("Promoción", ["Ninguna", "Envío gratis", "10% off", "15% off", "20% off"])

new_total = rappi['product_price'] + new_delivery + rappi['service_fee']
if new_promo == "Envío gratis":
    new_total -= new_delivery
elif new_promo == "10% off":
    new_total -= round(rappi['product_price'] * 0.10)
elif new_promo == "15% off":
    new_total -= round(rappi['product_price'] * 0.15)
elif new_promo == "20% off":
    new_total -= round(rappi['product_price'] * 0.20)

delta = rappi['final_total'] - new_total
st.metric("Nuevo Precio Final Rappi", f"${new_total} MXN", delta=f"${delta} MXN vs actual")

if new_total <= min(uber['final_total'], didi['final_total']):
    st.success("🎉 ¡Rappi ahora es la opción más barata!")
else:
    gap = new_total - min(uber['final_total'], didi['final_total'])
    st.warning(f"⚠️ Rappi sigue siendo ${gap} MXN más caro.")
