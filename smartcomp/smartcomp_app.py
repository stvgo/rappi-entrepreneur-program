#!/usr/bin/env python3
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(page_title="SmartComp", page_icon="🛵", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv(Path(__file__).parent / "products_data.csv")

df = load_data()

st.markdown("<h1 style='text-align:center;color:#FF6600'>🛵 SmartComp</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#475569'>Comparador de Precios — Rappi vs Uber Eats vs DiDi Food</p>", unsafe_allow_html=True)

zones = sorted(df["zone"].unique())
products = sorted(df["product"].unique())

with st.sidebar:
    st.markdown("## 🎯 Configuración")
    selected_zone = st.selectbox("📍 Zona", zones)
    selected_product = st.selectbox("🍔 Producto", products)
    st.markdown("---")
    st.page_link("pages/Documentacion.py", label="📚 Ver Documentación")

df_f = df[(df["zone"]==selected_zone) & (df["product"]==selected_product)]

if len(df_f) == 0:
    st.error("No hay datos")
    st.stop()

rappi = df_f[df_f["competitor"]=="Rappi"].iloc[0]
uber = df_f[df_f["competitor"]=="Uber Eats"].iloc[0]
didi = df_f[df_f["competitor"]=="DiDi Food"].iloc[0]

col1, col2, col3 = st.columns(3)
for col, data, name, color in [(col1,rappi,"Rappi","#FF6600"),(col2,uber,"Uber Eats","#276EF1"),(col3,didi,"DiDi Food","#FF6600")]:
    with col:
        st.markdown(f"""
        <div style="background:{color};padding:20px;border-radius:12px;color:white;text-align:center">
            <h3>{name}</h3>
            <h1>${data['final_total']} MXN</h1>
            <p>Producto: ${data['product_price']} MXN<br>
            Envío: ${data['delivery_fee']} MXN<br>
            Service: ${data['service_fee']} MXN<br>
            Promo: {data['promo']}</p>
        </div>
        """, unsafe_allow_html=True)

fig = go.Figure(data=[
    go.Bar(name='Producto', x=['Rappi','Uber Eats','DiDi Food'], y=[rappi['product_price'],uber['product_price'],didi['product_price']], marker_color='#FF6B00'),
    go.Bar(name='Envío', x=['Rappi','Uber Eats','DiDi Food'], y=[rappi['delivery_fee'],uber['delivery_fee'],didi['delivery_fee']], marker_color='#FFB366'),
    go.Bar(name='Service', x=['Rappi','Uber Eats','DiDi Food'], y=[rappi['service_fee'],uber['service_fee'],didi['service_fee']], marker_color='#FFD9B3'),
])
fig.update_layout(barmode='stack', title='Desglose de Costos', yaxis_title='MXN', plot_bgcolor='#fff', paper_bgcolor='#fff')
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("### 📊 Análisis")
totals = {"Rappi":rappi["final_total"],"Uber Eats":uber["final_total"],"DiDi Food":didi["final_total"]}
cheapest = min(totals, key=totals.get)
if cheapest == "Rappi":
    st.success("🟢 Rappi es la opción más barata")
else:
    gap = rappi["final_total"] - totals[cheapest]
    st.warning(f"🔴 Rappi es ${gap} MXN más caro que {cheapest}")
