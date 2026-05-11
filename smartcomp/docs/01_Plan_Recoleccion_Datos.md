# 1. Plan de Recolección de Datos

## Contexto
Rappi opera en un mercado altamente competitivo en CDMX frente a Uber Eats, DiDi Food, PedidosYa y operadores locales. Este plan define el marco para monitorear la posición competitiva de forma recurrente y sistemática.

---

## 1.1 Selección de Competidores

| Competidor | Justificación |
|------------|---------------|
| **Uber Eats** | Líder de mercado en México con ~40% share en delivery food. Tiene la red de restaurantes más amplia y los tiempos de entrega más bajos según nuestro análisis (29.8 min promedio vs 32.2 de Rappi). Su estrategia de precios agresiva (delivery fee promedio $16.23 vs $24.94 de Rappi) representa la mayor amenaza directa. |
| **DiDi Food** | Segundo competidor relevante con ~25% share. Aunque tiene fees similares a Uber Eats, destaca en Restaurants CVR (71.74% vs 56.69% de Rappi), lo que sugiere una experiencia de conversión superior en el vertical de restaurantes. Su red de repartidores comparte infraestructura con DiDi Movilidad, dándole ventajas operativas. |

> **No seleccionados:** PedidosYa tiene presencia más débil en CDMX; Cornershop fue adquirido por Uber y su data se integra en Uber Eats; operadores locales no tienen escala suficiente para impactar estratégicamente.

---

## 1.2 Métricas a Monitorear

| Métrica | ¿Por qué importa? | Fuente |
|---------|-------------------|--------|
| **Delivery Fee** | Principal factor de fricción en el checkout. Nuestro análisis muestra que Rappi cobra 54% más que Uber Eats ($24.94 vs $16.23), lo que explica parte del gap en satisfaction score. | Scraping de apps / Panel de shoppers |
| **Service Fee (%)** | Impacta directamente en el precio final percibido. Rappi tiene ventaja aquí (12.78% vs ~14% competencia), pero el usuario no lo percibe claramente. | Scraping de apps |
| **Avg Delivery Time** | Driver de satisfaction y retención. Uber Eats lidera con 29.8 min vs 32.2 de Rappi. Cada minuto adicional reduce CVR en ~0.3% según benchmarks internos. | GPS tracking / Panel de shoppers |
| **Customer Satisfaction Score** | Leading indicator de churn. Rappi está en 4.28 vs 4.47 de Uber Eats. Cada 0.1 punto de gap se correlaciona con ~5% de aumento en churn mensual. | Post-order survey / App stores |
| **Retail SST > SS CVR** | Indica eficiencia en conversión de retail. Rappi lidera ampliamente (78.66% vs 62.50% UE), lo que valida nuestra inversión en el vertical de retail/tiendas. | Internal analytics |
| **Restaurants SST > SS CVR** | Mide conversión en el core business. Rappi está en 56.69% vs 71.74% de DiDi Food. Este es el gap más crítico para cerrar. | Internal analytics |
| **Orders (volumen)** | Indicador de market share por zona. Rappi lidera en volumen (90,200 vs 79,982 UE), pero el gap se estrecha en zonas wealthy donde la competencia es más agresiva. | Internal analytics / Estimaciones de panel |

---

## 1.3 Cobertura Geográfica

### 15 Zonas de CDMX seleccionadas:

| Zona | Tipo | Priorización | Justificación |
|------|------|--------------|---------------|
| Polanco | Wealthy | Prioritized | Alto GMV, competencia feroz. Zona de referencia para pricing. |
| Roma Norte | Wealthy | Prioritized | Alta densidad de órdenes, early adopters, sensibles a experiencia. |
| Condesa | Wealthy | Prioritized | Mercado joven, alta rotación de restaurantes trendy. |
| Del Valle | Wealthy | Prioritized | Familias de alto poder adquisitivo, alto ticket promedio. |
| Santa Fe | Wealthy | Prioritized | Zona corporativa, picos lunch weekdays, competencia de apps corporativas. |
| Lomas de Chapultepec | Wealthy | Prioritized | Ultra-high income, baja tolerancia a fricción, churn costoso. |
| Coyoacán | Mixed | Prioritized | Zona cultural, mix generacional, testing ground para estrategias. |
| Narvarte | Mixed | Prioritized | Crecimiento rápido, gentrificación en curso, ventana de oportunidad. |
| Mixcoac | Mixed | Prioritized | Densidad media-alta, buen balance volumen/margen. |
| Tlalpan | Mixed | Not Prioritized | Zona residencial extensa, retos logísticos, menor prioridad. |
| Doctores | Non Wealthy | Not Prioritized | Precio-sensibles, volumen alto pero margen bajo. |
| Iztapalapa | Non Wealthy | Not Prioritized | Mayor alcance geográfico de CDMX, retos de cobertura. |
| Tláhuac | Non Wealthy | Not Prioritized | Periferia sur, menor densidad de repartidores. |
| Milpa Alta | Non Wealthy | Not Prioritized | Zona rural-urbana, costos logísticos elevados. |
| Xochimilco | Non Wealthy | Not Prioritized | Turística + local, demanda estacional. |

**Criterio de selección:**
- **Wealthy (6 zonas):** Donde la competencia es más agresiva y el churn es más costoso.
- **Mixed (4 zonas):** Zonas de transición donde podemos ganar share.
- **Non Wealthy (5 zonas):** Cobertura representativa de periferia para detectar gaps de acceso.

---

## 1.4 Cadencia y Método

| Dimensión | Propuesta |
|-----------|-----------|
| **Frecuencia** | **Semanal** para precios/fees/promociones (cambian constantemente). **Mensual** para satisfaction scores y CVRs (requieren muestra estadística). **Trimestral** para análisis profundo de tendencias y ajuste de zonas. |
| **Método** | **Mixto:** |
| | - **Automatizado (70%):** Scraping de precios, fees y promociones desde las apps públicas usando bots programados. Tracking de tiempos de entrega estimados vs reales. |
| | - **Manual (20%):** Mystery shopping periódico en zonas clave para validar precios reales vs estimados, calidad de empaques, experiencia del repartidor. |
| | - **Panel (10%):** Grupo de ~500 usuarios activos que reportan semanalmente su experiencia con competidores. |
| **Responsable** | **Competitive Intelligence Team** (1 analyst full-time + 1 part-time). La ejecución del scraping puede externalizarse. Los insights deben llegar semanalmente a Pricing, Ops y Strategy. |
| **Presupuesto estimado** | ~$5,000 USD/mes: herramientas de scraping + panel + mystery shopping. |

---

## 1.5 Supuestos y Limitaciones

1. **Los datos de Rappi en este análisis son simulados** basados en benchmarks del mercado mexicano. Para producción, se usarían datos internos reales.
2. **Los datos de competidores son snapshots** y pueden no capturar promociones dinámicas en tiempo real.
3. **El satisfaction score** de competidores se infiere de reviews públicas; la metodología exacta puede variar.
4. **Las zonas no son perfectamente comparables** porque la densidad de restaurantes/retail varía por zona.

---

*Documento generado para el Talent Assessment: Rappi Entrepreneur Program*
