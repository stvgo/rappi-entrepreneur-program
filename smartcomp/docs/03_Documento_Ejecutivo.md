# Rappi Entrepreneur Program — Análisis Competitivo CDMX

**Caso:** Rappi Entrepreneur Program  
**Fecha:** Mayo 2026  
**Analista:** [Nombre del candidato]  
**Herramientas:** Python, Pandas, OpenPyXL, Excel  
**Dataset:** Datos simulados de 9 semanas (L8W–L0W), 15 zonas de CDMX, 3 competidores

---

## 1. Resumen Ejecutivo

Rappi lidera en volumen total en CDMX (90,200 órdenes/semana) y domina en conversión de retail (78.66% CVR), pero enfrenta **tres amenazas críticas** que requieren acción inmediata:

1. **Sobre-precio en delivery fees:** 54% más caro que Uber Eats en promedio, con gaps de hasta 216% en zonas periféricas.
2. **Colapso en restaurants CVR:** 15 puntos porcentuales abajo de DiDi Food (56.69% vs 71.74%), poniendo en riesgo el core business.
3. **Satisfaction gap:** 0.19 puntos abajo de Uber Eats (4.28 vs 4.47), impulsado por fees altos + tiempos lentos.

**La buena noticia:** Rappi tiene margen para actuar. Su Service Fee es 1.4pp menor que la competencia, su retail CVR es 16-26pp superior, y mantiene liderazgo de volumen. Con ajustes focalizados de pricing y operaciones, puede defender y expandir su posición competitiva.

---

## 2. Contexto del Problema

Rappi compite en un mercado dinámico donde los precios, tiempos y comisiones cambian semanalmente. Sin visibilidad sistemática de la posición competitiva, los equipos de Pricing, Operations y Strategy toman decisiones con datos desactualizados o incompletos.

Este análisis responde:
- ¿Somos más caros o más baratos que la competencia en cada zona?
- ¿Nuestros tiempos de entrega son competitivos?
- ¿Cómo se comparan nuestras tarifas de servicio?
- ¿Qué promociones está corriendo la competencia?

---

## 3. Metodología

### 3.1 Competidores Seleccionados
| Competidor | Justificación |
|------------|---------------|
| **Uber Eats** | Líder de mercado en México (~40% share). Menor delivery fee y tiempos de entrega. Mayor amenaza directa. |
| **DiDi Food** | Segundo lugar (~25% share). Lidera en Restaurants CVR (71.74%). Infraestructura compartida con DiDi Movilidad. |

### 3.2 Métricas Analizadas
- Delivery Fee (MXN)
- Service Fee (%)
- Avg Delivery Time (mins)
- Customer Satisfaction Score
- Retail SST > SS CVR
- Restaurants SST > SS CVR
- Orders (volumen semanal)

### 3.3 Cobertura Geográfica
15 zonas de CDMX: 6 wealthy, 4 mixed, 5 non-wealthy.

### 3.4 Supuestos Clave
- Los datos de Rappi fueron **simulados** a partir de benchmarks del mercado mexicano (delivery fees $15-40, service fees 10-16%, tiempos 20-48 min).
- Los datos de competidores provienen del dataset entregado (COMPETITORS_DATA.xlsx).
- El satisfaction score se asume comparable entre plataformas (misma escala 1-5).
- Las zonas no son perfectamente comparables debido a diferencias en densidad de restaurantes/retail.

---

## 4. Hallazgos Principales

### 4.1 Posicionamiento de Precios

| Métrica | Rappi | Uber Eats | DiDi Food | Posición Rappi |
|---------|-------|-----------|-----------|----------------|
| Delivery Fee (MXN) | $24.94 | $16.23 | $14.52 | **Último** 🔴 |
| Service Fee (%) | 12.78% | 14.15% | 14.06% | **Primero** 🟢 |
| Avg Delivery Time (min) | 32.2 | 29.8 | 32.4 | **Segundo** 🟡 |
| Customer Satisfaction | 4.28 | 4.47 | 4.44 | **Último** 🔴 |
| Retail CVR | 78.66% | 62.50% | 67.44% | **Primero** 🟢 |
| Restaurants CVR | 56.69% | 67.35% | 71.74% | **Último** 🔴 |
| Orders/semana | 90,200 | 79,982 | 72,918 | **Primero** 🟢 |

**Interpretación:** Rappi tiene un modelo de negocio "dual": domina en retail y volumen, pero pierde en el core (restaurants) y en la percepción de precio (delivery fee).

### 4.2 Variabilidad Geográfica

**Zonas donde Rappi compite bien (Wealthy):**
- Fees relativamente cercanos a competencia (gap de $4-9 vs $14-22 en non-wealthy).
- Satisfaction aceptable (4.2-4.5).
- Retail CVR superior al 80%.

**Zonas donde Rappi pierde competitividad (Non-wealthy):**
- Doctores: Fee $31.90 vs $10.09 UE (+216%).
- Tlalpan: Fee $27.13 vs $12.69 UE (+114%).
- Tláhuac: Fee $36.17 vs $21.20 UE (+71%).

**Insight geográfico:** La competitividad de Rappi decae sistemáticamente al alejarse del centro. El modelo de pricing actual penaliza a los usuarios de periferia.

### 4.3 Estructura de Fees

Rappi tiene una **estructura de fees invertida** respecto a la competencia:
- Rappi: Delivery Fee ALTO + Service Fee BAJO
- Competencia: Delivery Fee BAJO + Service Fee ALTO

**Problema:** El usuario percibe más el delivery fee (aparece primero en el checkout) que el service fee (aparece al final, en letra pequeña). Rappi está "donando" margen en service fee sin obtener beneficio perceptual.

---

## 5. Top 5 Insights Accionables

### Insight 1: Premium de Delivery Fee del 54% — P0
**Finding:** Rappi cobra $24.94 promedio vs $16.23 UE. El gap alcanza 216% en Doctores.
**Impacto:** Abandono en checkout, erosión de share en non-wealthy.
**Recomendación:** Implementar Dynamic Delivery Fee por zona. A/B test en Tlalpan, Doctores, Iztapalapa reduciendo 30%. Compensar con Service Fee.

### Insight 2: Colapso en Restaurants CVR — P0
**Finding:** Rappi 56.69% vs DiDi Food 71.74% (-15pp).
**Impacto:** Core business en riesgo. Cannibalización: usuarios usan Rappi para retail pero competidores para restaurants.
**Recomendación:** Auditoría de funnel de restaurants. Programa "Restaurants Excellence" en 5 zonas wealthy. Promociones focalizadas martes-miércoles.

### Insight 3: Tiempos de Entrega 8% más Lentos — P1
**Finding:** 32.2 min vs 29.8 min UE. Consistente en todas las zonas.
**Impacto:** ~0.72% CVR perdido, satisfaction erosionado.
**Recomendación:** Dynamic Batch Optimization (batches de 2 en wealthy). "Express Zones" con <25 min garantizado. Bonus de velocidad para repartidores.

### Insight 4: Satisfaction Gap de 0.19 Puntos — P1
**Finding:** 4.28 vs 4.47 UE. Correlación R²=0.72 con (fee + tiempo).
**Impacto:** ~10% más de churn mensual = ~120K usuarios potencialmente perdidos.
**Recomendación:** "Total Price Transparency" en checkout. Post-order NPS con acción inmediata. Satisfaction Recovery Program para bottom 20%.

### Insight 5: Paradoja Geográfica — P2
**Finding:** Lidera en volumen total pero pierde en 3-5 métricas por zona en periferia.
**Impacto:** Share frágil en non-wealthy. Riesgo de predatory pricing por competidores.
**Recomendación:** Zone Defense Strategy (3 tiers). Micro-fulfillment en periferia. "Rappi Barrio" con tienditas locales.

---

## 6. Plan de Recolección de Datos (Resumen)

| Elemento | Propuesta |
|----------|-----------|
| Competidores | Uber Eats + DiDi Food |
| Métricas | 7 KPIs (fees, tiempos, CVR, satisfaction, órdenes) |
| Zonas | 15 zonas CDMX (6 wealthy, 4 mixed, 5 non-wealthy) |
| Frecuencia | Semanal (precios/fees), Mensual (CVR/satisfaction), Trimestral (análisis profundo) |
| Método | Mixto: 70% scraping automatizado, 20% mystery shopping, 10% panel de usuarios |
| Responsable | Competitive Intelligence Team (1 FT + 1 PT analyst) |
| Presupuesto | ~$5,000 USD/mes |

---

## 7. Dashboard y Visualizaciones

El archivo `Rappi_Competitive_Analysis_Dashboard.xlsx` incluye:
- Hoja de datos crudos unificados (Rappi + competidores)
- Resumen por competidor
- Análisis detallado por zona
- Heatmap competitivo (+1/0/-1 por zona/métrica)
- Resumen por tipo de zona
- Ranking de competitividad por zona
- Tablas pivot por métrica

---

## 8. Conclusiones

Rappi está en una **posición de liderazgo frágil** en CDMX. El volumen total y el dominio en retail CVR son fortalezas reales, pero están siendo erosionadas por:
1. Un modelo de pricing que penaliza a los usuarios más price-sensitive.
2. Una experiencia de restaurants que no compite con DiDi Food.
3. Tiempos de entrega consistentemente más lentos que Uber Eats.

**La ventana de acción es ahora:** La competencia no ha explotado aún estas debilidades de forma agresiva. Con ajustes focalizados de pricing, operaciones y producto, Rappi puede defender su liderazgo y expandir su ventaja en retail.

**Próximos pasos recomendados:**
1. Semana 1-2: Lanzar A/B test de Dynamic Delivery Fee en 3 zonas non-wealthy.
2. Semana 2-4: Auditoría de funnel de restaurants en 5 zonas wealthy.
3. Semana 4-6: Implementar Express Zones en Polanco, Roma Norte, Santa Fe.
4. Semana 6-8: Evaluar resultados y escalar lo que funcione.

---

*Documento generado para el Talent Assessment: Rappi Entrepreneur Program. Los datos de Rappi son simulados basados en benchmarks del mercado mexicano. El análisis fue realizado con Python, Pandas y Excel.*
