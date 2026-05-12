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

# ==================== CSS LIMPIO ====================
st.markdown("""
<style>
    .kpi-box {
        background: #ffffff;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        border: 1px solid #f0f0f0;
    }
    .kpi-number {
        font-size: 2rem;
        font-weight: 700;
        color: #FF6600;
        line-height: 1.2;
    }
    .kpi-label {
        font-size: 0.8rem;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-top: 4px;
    }
    .kpi-delta-pos { color: #16a34a; font-weight: 600; font-size: 0.85rem; }
    .kpi-delta-neg { color: #dc2626; font-weight: 600; font-size: 0.85rem; }
    
    .comp-card {
        border-radius: 12px;
        padding: 24px 16px;
        text-align: center;
        color: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .comp-price { font-size: 2.2rem; font-weight: 800; margin: 8px 0; }
    .comp-name { font-size: 1rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }
    .comp-detail { font-size: 0.85rem; margin-top: 8px; opacity: 0.95; line-height: 1.7; }
    
    .section-title {
        color: #1a1a2e;
        font-size: 1.3rem;
        font-weight: 700;
        margin: 32px 0 16px 0;
        padding-bottom: 8px;
        border-bottom: 2px solid #FF6600;
        display: inline-block;
    }
    
    .insight-box {
        background: #fafafa;
        border-left: 4px solid #FF6600;
        border-radius: 0 8px 8px 0;
        padding: 12px 16px;
        margin: 6px 0;
    }
    .insight-box.green { border-left-color: #16a34a; background: #f0fdf4; }
    .insight-box.red { border-left-color: #dc2626; background: #fef2f2; }
    .insight-box.blue { border-left-color: #2563eb; background: #eff6ff; }
    
    .badge {
        display: inline-block;
        padding: 2px 10px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    .badge-winner { background: #dcfce7; color: #166534; }
    .badge-loser { background: #fee2e2; color: #991b1b; }
</style>
""", unsafe_allow_html=True)

# ==================== FUNCIONES ====================

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

# ==================== HEADER ====================
st.markdown('<h1 style="text-align:center;color:#FF6600;margin-bottom:4px">🛵 SmartComp</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center;color:#64748b;margin-top:0">Comparador Inteligente — Rappi vs Uber Eats vs DiDi Food</p>', unsafe_allow_html=True)

# ==================== SIDEBAR ====================
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
        st.success("✅ API key cargada")
    model = st.text_input("Modelo", value="nvidia/nemotron-3-super-120b-a12b:free")
    st.markdown("---")
    st.markdown("### 📚 Documentación")
    st.page_link("pages/Documentacion.py", label="Ver Documentación", icon="📄")

# ==================== DATA ====================
st.markdown(f"<div class='section-title'>📍 Análisis: {selected_product} en {selected_zone}</div>", unsafe_allow_html=True)

df_filtered = df[(df["zone"] == selected_zone) & (df["product"] == selected_product)]

if len(df_filtered) == 0:
    st.error("No se encontraron datos.")
    st.stop()

findings, recommendations, actions, rappi, uber, didi = local_analyze(selected_product, selected_zone, df_filtered)

# ==================== KPI ROW ====================
df_zone = df[df["zone"] == selected_zone]
rappi_zone = df_zone[df_zone["competitor"] == "Rappi"]
uber_zone = df_zone[df_zone["competitor"] == "Uber Eats"]
didi_zone = df_zone[df_zone["competitor"] == "DiDi Food"]

rappi_avg = rappi_zone["final_total"].mean()
uber_avg = uber_zone["final_total"].mean()
didi_avg = didi_zone["final_total"].mean()
market_avg = (rappi_avg + uber_avg + didi_avg) / 3

cheapest_overall = min([("Rappi", rappi_avg), ("Uber", uber_avg), ("DiDi", didi_avg)], key=lambda x: x[1])
is_rappi_cheapest = cheapest_overall[0] == "Rappi"
gap_vs_market = ((rappi["final_total"] - market_avg) / market_avg) * 100 if market_avg > 0 else 0
delivery_gap = rappi["delivery_fee"] - min(rappi["delivery_fee"], uber["delivery_fee"], didi["delivery_fee"])

k1, k2, k3, k4 = st.columns(4)
with k1:
    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-number">{'#1 🥇' if is_rappi_cheapest else '#2-3'}</div>
        <div class="kpi-label">Posición Mercado</div>
        <div class="{'kpi-delta-pos' if is_rappi_cheapest else 'kpi-delta-neg'}">
            {'Más barato' if is_rappi_cheapest else f'🔻 ${rappi["final_total"] - cheapest_overall[1]:.0f} vs {cheapest_overall[0]}'}
        </div>
    </div>
    """, unsafe_allow_html=True)
with k2:
    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-number">{gap_vs_market:+.1f}%</div>
        <div class="kpi-label">Gap vs Mercado</div>
        <div class="{'kpi-delta-pos' if gap_vs_market <= 0 else 'kpi-delta-neg'}">
            {'✅ Bajo mercado' if gap_vs_market <= 0 else '⚠️ Sobre mercado'}
        </div>
    </div>
    """, unsafe_allow_html=True)
with k3:
    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-number">+${delivery_gap:.0f}</div>
        <div class="kpi-label">Delivery Fee Gap</div>
        <div class="{'kpi-delta-pos' if delivery_gap <= 0 else 'kpi-delta-neg'}">
            {'✅ Competitivo' if delivery_gap <= 0 else f'🔻 ${delivery_gap:.0f} vs mejor'}
        </div>
    </div>
    """, unsafe_allow_html=True)
with k4:
    n_products = len(rappi_zone)
    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-number">{n_products}</div>
        <div class="kpi-label">Productos Zona</div>
        <div class="kpi-delta-pos">📦 Catálogo activo</div>
    </div>
    """, unsafe_allow_html=True)

# ==================== AI BUTTON ====================
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

# ==================== COMPETITOR CARDS ====================
st.markdown(f"<div class='section-title'>🏆 Comparativa de Precios</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
for col, data, name, color, icon in [
    (col1, rappi, "Rappi", "#FF6600", "🛵"),
    (col2, uber, "Uber Eats", "#276EF1", "🚗"),
    (col3, didi, "DiDi Food", "#FFA500", "🚕")
]:
    with col:
        is_winner = data["final_total"] == min(rappi["final_total"], uber["final_total"], didi["final_total"])
        badge = '<span class="badge badge-winner">🏆 Más barato</span>' if is_winner else '<span class="badge badge-loser">+${:.0f}</span>'.format(data["final_total"] - min(rappi["final_total"], uber["final_total"], didi["final_total"]))
        st.markdown(f"""
        <div class="comp-card" style="background:{color}">
            <div class="comp-name">{icon} {name}</div>
            <div class="comp-price">${data['final_total']} MXN</div>
            <div style="margin:6px 0">{badge}</div>
            <div class="comp-detail">
                🍔 Producto: ${data['product_price']}<br>
                📦 Envío: ${data['delivery_fee']}<br>
                ⚙️ Service: ${data['service_fee']}<br>
                🎁 Promo: {data['promo']}
            </div>
        </div>
        """, unsafe_allow_html=True)

# ==================== TABS: GRÁFICOS ====================
st.markdown(f"<div class='section-title'>📊 Análisis Visual</div>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📊 Costos", "⚡ Gauge", "🎯 Radar"])

with tab1:
    g1, g2 = st.columns(2)
    with g1:
        fig = go.Figure(data=[
            go.Bar(name='Producto', x=['Rappi','Uber','DiDi'], 
                   y=[rappi['product_price'], uber['product_price'], didi['product_price']], 
                   marker_color='#FF6B00',
                   text=[f"${rappi['product_price']}", f"${uber['product_price']}", f"${didi['product_price']}"],
                   textposition='inside', textfont=dict(color='white')),
            go.Bar(name='Envío', x=['Rappi','Uber','DiDi'], 
                   y=[rappi['delivery_fee'], uber['delivery_fee'], didi['delivery_fee']], 
                   marker_color='#FFB366',
                   text=[f"${rappi['delivery_fee']}", f"${uber['delivery_fee']}", f"${didi['delivery_fee']}"],
                   textposition='inside', textfont=dict(color='#333')),
            go.Bar(name='Service', x=['Rappi','Uber','DiDi'], 
                   y=[rappi['service_fee'], uber['service_fee'], didi['service_fee']], 
                   marker_color='#FFD9B3',
                   text=[f"${rappi['service_fee']}", f"${uber['service_fee']}", f"${didi['service_fee']}"],
                   textposition='inside', textfont=dict(color='#333')),
        ])
        fig.update_layout(
            barmode='stack', 
            title='Desglose de Costos',
            yaxis_title='MXN',
            plot_bgcolor='#ffffff', paper_bgcolor='#ffffff',
            font=dict(color="#1a1a2e"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
            margin=dict(t=60)
        )
        st.plotly_chart(fig, use_container_width=True, key="stacked")
    
    with g2:
        fig2 = go.Figure(data=[
            go.Bar(x=['Rappi', 'Uber Eats', 'DiDi Food'], 
                   y=[rappi['final_total'], uber['final_total'], didi['final_total']],
                   marker_color=['#FF6600', '#276EF1', '#FFA500'],
                   text=[f"${rappi['final_total']}", f"${uber['final_total']}", f"${didi['final_total']}"],
                   textposition='outside', textfont=dict(size=14))
        ])
        fig2.update_layout(
            title='Precio Final',
            yaxis_title='MXN',
            plot_bgcolor='#ffffff', paper_bgcolor='#ffffff',
            showlegend=False,
            margin=dict(t=60),
            yaxis=dict(range=[0, max(rappi['final_total'], uber['final_total'], didi['final_total']) * 1.15])
        )
        st.plotly_chart(fig2, use_container_width=True, key="final")

with tab2:
    g3, g4 = st.columns(2)
    with g3:
        market_min = min(rappi['final_total'], uber['final_total'], didi['final_total'])
        comp = (market_min / rappi['final_total']) * 100 if rappi['final_total'] > 0 else 0
        fig_g = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=comp,
            title={'text': "Competitividad Rappi", 'font': {'size': 16}},
            delta={'reference': 100, 'suffix': '%'},
            gauge={'axis': {'range': [50, 100]},
                   'bar': {'color': '#FF6600'},
                   'steps': [
                       {'range': [50, 70], 'color': '#fee2e2'},
                       {'range': [70, 85], 'color': '#fef9c3'},
                       {'range': [85, 100], 'color': '#dcfce7'}],
                   'threshold': {'line': {'color': '#16a34a', 'width': 3}, 'value': 100}}
        ))
        fig_g.update_layout(height=300, margin=dict(t=50, b=20))
        st.plotly_chart(fig_g, use_container_width=True, key="gauge1")
    
    with g4:
        total_mkt = rappi['final_total'] + uber['final_total'] + didi['final_total']
        share = (rappi['final_total'] / total_mkt) * 100 if total_mkt > 0 else 0
        fig_s = go.Figure(go.Indicator(
            mode="gauge+number",
            value=share,
            title={'text': "Share de Precio Rappi", 'font': {'size': 16}},
            number={'suffix': '%'},
            gauge={'axis': {'range': [0, 50]},
                   'bar': {'color': '#FF6600'},
                   'steps': [
                       {'range': [0, 33], 'color': '#dcfce7'},
                       {'range': [33, 40], 'color': '#fef9c3'},
                       {'range': [40, 50], 'color': '#fee2e2'}]}
        ))
        fig_s.update_layout(height=300, margin=dict(t=50, b=20))
        st.plotly_chart(fig_s, use_container_width=True, key="gauge2")

with tab3:
    cats = ['Precio Total', 'Delivery', 'Service', 'Promo', 'Producto']
    max_t = max(rappi['final_total'], uber['final_total'], didi['final_total'])
    max_d = max(rappi['delivery_fee'], uber['delivery_fee'], didi['delivery_fee'])
    max_s = max(rappi['service_fee'], uber['service_fee'], didi['service_fee'])
    max_p = max(rappi['product_price'], uber['product_price'], didi['product_price'])
    max_disc = max(rappi['discount'], uber['discount'], didi['discount'])
    
    rv = [100 - (rappi['final_total']/max_t*100), 100 - (rappi['delivery_fee']/max_d*100),
          100 - (rappi['service_fee']/max_s*100), (rappi['discount']/max_disc*100) if max_disc>0 else 0,
          100 - (rappi['product_price']/max_p*100)]
    uv = [100 - (uber['final_total']/max_t*100), 100 - (uber['delivery_fee']/max_d*100),
          100 - (uber['service_fee']/max_s*100), (uber['discount']/max_disc*100) if max_disc>0 else 0,
          100 - (uber['product_price']/max_p*100)]
    dv = [100 - (didi['final_total']/max_t*100), 100 - (didi['delivery_fee']/max_d*100),
          100 - (didi['service_fee']/max_s*100), (didi['discount']/max_disc*100) if max_disc>0 else 0,
          100 - (didi['product_price']/max_p*100)]
    
    fig_r = go.Figure()
    fig_r.add_trace(go.Scatterpolar(r=rv+[rv[0]], theta=cats+[cats[0]], fill='toself', name='Rappi', line_color='#FF6600'))
    fig_r.add_trace(go.Scatterpolar(r=uv+[uv[0]], theta=cats+[cats[0]], fill='toself', name='Uber', line_color='#276EF1'))
    fig_r.add_trace(go.Scatterpolar(r=dv+[dv[0]], theta=cats+[cats[0]], fill='toself', name='DiDi', line_color='#FFA500'))
    fig_r.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
        title='Perfil Competitivo',
        height=450,
        margin=dict(t=60)
    )
    st.plotly_chart(fig_r, use_container_width=True, key="radar")

# ==================== INSIGHTS ====================
st.markdown(f"<div class='section-title'>🧠 Análisis Inteligente</div>", unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    st.markdown("**🔍 Hallazgos**")
    for f in findings:
        cls = "green" if "más barata" in f.lower() else "red" if "más caro" in f.lower() or "crítico" in f.lower() else ""
        st.markdown(f'<div class="insight-box {cls}">{f}</div>', unsafe_allow_html=True)

with c2:
    st.markdown("**💡 Recomendaciones**")
    for r in recommendations:
        cls = "green" if "mantener" in r.lower() else "red" if "crítico" in r.lower() else "blue"
        st.markdown(f'<div class="insight-box {cls}">{r}</div>', unsafe_allow_html=True)

st.markdown("**✅ Acciones Recomendadas**")
for a in actions:
    st.markdown(f'<div class="insight-box">{a}</div>', unsafe_allow_html=True)

# ==================== SIMULADOR ====================
st.markdown(f"<div class='section-title'>🎮 Simulador de Escenarios</div>", unsafe_allow_html=True)

s1, s2, s3 = st.columns(3)
with s1:
    new_delivery = st.slider("Delivery Fee", max(5, int(rappi['delivery_fee']-15)), int(rappi['delivery_fee']+10), int(rappi['delivery_fee']))
with s2:
    new_service = st.slider("Service Fee", max(5, int(rappi['service_fee']-10)), int(rappi['service_fee']+10), int(rappi['service_fee']))
with s3:
    new_promo = st.selectbox("Promoción", ["Ninguna", "Envío gratis", "10% off", "15% off", "20% off"])

new_total = rappi['product_price'] + new_delivery + new_service
if new_promo == "Envío gratis": new_total -= new_delivery
elif new_promo == "10% off": new_total -= round(rappi['product_price']*0.10)
elif new_promo == "15% off": new_total -= round(rappi['product_price']*0.15)
elif new_promo == "20% off": new_total -= round(rappi['product_price']*0.20)

delta = rappi['final_total'] - new_total
delta_pct = (delta / rappi['final_total']) * 100
comp_min = min(uber['final_total'], didi['final_total'])

m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Actual", f"${rappi['final_total']} MXN")
with m2: st.metric("Nuevo", f"${new_total} MXN", delta=f"{delta_pct:+.1f}%")
with m3: st.metric("Gap vs Mejor", f"${new_total - comp_min:.0f} MXN")
with m4: st.metric("Resultado", "🎉 Rappi gana" if new_total <= comp_min else "⚠️ 2°/3°")

# Gauge del simulador
fig_sim = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=new_total,
    title={'text': "Precio Simulado Rappi", 'font': {'size': 16}},
    delta={'reference': rappi['final_total'], 'suffix': ' MXN'},
    number={'suffix': ' MXN'},
    gauge={'axis': {'range': [min(rappi['final_total']-20, new_total-10), max(rappi['final_total']+10, uber['final_total']+10, didi['final_total']+10)]},
           'bar': {'color': '#FF6600'},
           'steps': [
               {'range': [0, comp_min], 'color': '#dcfce7'},
               {'range': [comp_min, comp_min+10], 'color': '#fef9c3'},
               {'range': [comp_min+10, comp_min+30], 'color': '#fee2e2'}],
           'threshold': {'line': {'color': '#16a34a', 'width': 3}, 'value': comp_min}}
))
fig_sim.update_layout(height=280, margin=dict(t=50, b=20))
st.plotly_chart(fig_sim, use_container_width=True, key="sim")

st.markdown("<p style='text-align:center;color:#94a3b8;font-size:0.8rem;margin-top:40px'>🛵 SmartComp — Rappi Entrepreneur Program</p>", unsafe_allow_html=True)
