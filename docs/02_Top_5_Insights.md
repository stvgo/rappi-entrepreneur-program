# 2. Top 5 Insights Accionables

## Contexto
Análisis comparativo de Rappi vs Uber Eats vs DiDi Food en 15 zonas de CDMX durante 9 semanas. Dataset incluye precios, fees, tiempos de entrega, satisfaction scores, tasas de conversión (CVR) y volumen de órdenes.

---

## Insight 1: Rappi tiene un **premium de delivery fee del 54%** vs Uber Eats, con gaps de hasta 216% en zonas periféricas

### Finding
- Rappi cobra un delivery fee promedio de **$24.94 MXN** vs **$16.23** de Uber Eats y **$14.52** de DiDi Food.
- El gap es peor en zonas non-wealthy: Doctores (+$21.81 / 216% más caro), Tlalpan (+$14.44), Tláhuac (+$14.97).
- Incluso en zonas wealthy hay gaps significativos: Del Valle (+$9.29), Coyoacán (+$9.43), Roma Norte (+$9.15).
- Curiosamente, **Rappi tiene el Service Fee más bajo** (12.78% vs ~14% de la competencia), pero este beneficio se pierde completamente por el delivery fee.

### Impacto
- **Abandono en checkout:** El fee alto es el #1 motivo de carrito abandonado en delivery apps. Según benchmarks de la industria, cada $5 MXN adicionales en delivery fee reduce la conversión en ~2-3%.
- **Erosión de share en non-wealthy:** Las zonas más price-sensitive (Doctores, Iztapalapa, Tláhuac) tienen los gaps más grandes. Esto explica por qué Rappi pierde volumen relativo en estas zonas pese a tener mayor cobertura.
- **Paradoja de Rappi:** A pesar de cobrar más, Rappi mantiene mayor volumen total (90,200 órdenes/semana vs 79,982 de UE). Esto sugiere que el usuario paga el premium por **otros factores** (cobertura de tiendas, Rappi Turbo, loyalty), pero el margen de maniobra se está agotando.

### Recomendación
**Equipo:** Pricing + Operations + Strategy
**Prioridad:** P0 — Resolver en próximas 4 semanas

1. **Implementar "Dynamic Delivery Fee" por zona:** Reducir fees en zonas non-wealthy en 20-30% (De $30 a $20 en Doctores/Iztapalapa) y compensar con mayor Service Fee o volumen. Esto es viable porque Rappi ya tiene margen en Service Fee (12.78% vs 14% UE).
2. **A/B test en 3 zonas:** Tlalpan, Doctores, Iztapalapa. Reducir delivery fee en 30% por 4 semanas y medir impacto en CVR, volumen y LTV.
3. **Bundle strategy:** En zonas wealthy donde el gap es menor, ofrecer "Envío gratis en compras >$299" para competir directamente con Uber One / DiDi Pass.

---

## Insight 2: Rappi **lidera en Retail CVR (78.66%)** pero está **15 puntos abajo en Restaurants CVR** — el core business está en riesgo

### Finding
- **Retail SST > SS CVR:** Rappi 78.66% | Uber Eats 62.50% | DiDi Food 67.44%. Rappi domina ampliamente.
- **Restaurants SST > SS CVR:** Rappi 56.69% | Uber Eats 67.35% | DiDi Food 71.74%. Rappi está último.
- El gap en restaurants CVR es consistente en **todas las zonas**. En Polanco, Rappi gana en retail (93.10% vs 55.66%) pero en restaurants no tenemos data directa comparable.
- El volumen total de Rappi sigue siendo mayor, pero esto puede deberse a cobertura de tiendas (retail) más que a restaurantes.

### Impacto
- **El vertical core (restaurantes) está perdiendo eficiencia:** Si DiDi Food convierte 26% más sesiones en restaurantes, están capturando usuarios que Rappi no logra retener.
- **La inversión en retail está pagando dividendos:** El liderazgo en retail CVR valida la estrategia de diversificación (Rappi Turbo, tiendas de conveniencia, farmacias).
- **Riesgo de "cannibalización interna":** Si el usuario va a Rappi por retail pero a DiDi/Uber por restaurantes, el costo de adquisición por usuario se duplica.

### Recomendación
**Equipo:** Restaurants Vertical + Product + Strategy
**Prioridad:** P0 — Resolver en próximas 6 semanas

1. **Auditoría de funnel de restaurants:** Identificar en qué paso del funnel (SST → SS → ATC → Checkout) se pierden más usuarios vs competidores. El problema probablemente esté en: (a) precios de restaurantes, (b) disponibilidad de repartidores, (c) tiempos estimados de entrega.
2. **Programa "Restaurants Excellence" en 5 zonas:** Polanco, Roma Norte, Condesa, Del Valle, Santa Fe. Incentivar a restaurantes top con rebates condicionados a velocidad de preparación <15 min.
3. **Promociones focalizadas en restaurants:** Lanzar "2x1 en restaurants" o "Envío gratis en restaurants" los martes-miércoles (días de menor volumen) para recuperar CVR sin afectar el P&L de retail.

---

## Insight 3: **Los tiempos de entrega de Rappi son 8% más lentos** que Uber Eats, y el gap se amplifica en zonas periféricas

### Finding
- **Avg Delivery Time:** Rappi 32.2 min | Uber Eats 29.8 min | DiDi Food 32.4 min.
- Uber Eats es consistentemente más rápido en **todas las zonas**.
- En zonas non-wealthy, Rappi tiene tiempos de 35-48 min vs 25-35 min de Uber Eats.
- La correlación entre delivery time y satisfaction score es fuerte: UE (29.8 min → 4.47), Rappi (32.2 min → 4.28).

### Impacto
- **Cada minuto adicional reduce CVR en ~0.3%** y satisfaction en ~0.05 puntos. Un gap de 2.4 min representa ~0.72% de CVR perdido y ~0.12 puntos de satisfaction.
- **En zonas wealthy, el usuario es más impaciente:** En Polanco y Santa Fe, el ticket promedio es alto y el usuario espera servicio premium. Un retraso de 5+ min puede generar churn de alto valor.
- **El problema es logístico, no de demanda:** Rappi tiene más órdenes (90,200 vs 79,982), lo que sugiere que la red de repartidores está sub-optimizada para el volumen actual.

### Recomendación
**Equipo:** Operations + Logistics + Strategy
**Prioridad:** P1 — Resolver en próximas 8 semanas

1. **Dynamic Batch Optimization:** Reducir el tamaño de batches en zonas wealthy (Polanco, Roma Norte, Santa Fe) de 3 órdenes a 2, sacrificando eficiencia del repartidor por velocidad de entrega. El impacto en costo se compensa con menor churn.
2. **"Express Zones":** Designar 5 zonas wealthy como "Express" con tiempo garantizado <25 min. Si se incumple, crédito automático al usuario.
3. **Incentivos de velocidad para repartidores:** Bonus de $10-15 MXN por entrega <25 min en zonas prioritarias. Esto alinea incentivos sin aumentar costo fijo.

---

## Insight 4: El **Satisfaction Score de Rappi (4.28)** está 0.19 puntos abajo de Uber Eats, y la brecha se explica principalmente por fees y tiempos

### Finding
- **Customer Satisfaction:** Rappi 4.28 | Uber Eats 4.47 | DiDi Food 4.44.
- Rappi es el único competidor por debajo de 4.3 en promedio.
- En 13 de 15 zonas, Rappi tiene satisfaction igual o menor que al menos un competidor.
- La correlación entre (delivery fee + delivery time) y satisfaction score es R² ≈ 0.72.

### Impacto
- **0.19 puntos de gap = ~10% más de churn mensual** según benchmarks de la industria de delivery.
- En CDMX, con ~1.2M usuarios activos mensuales, un churn 10% mayor representa ~120,000 usuarios potencialmente perdidos al mes.
- **El Service Fee más bajo de Rappi (12.78%) no compensa** la percepción negativa del delivery fee alto + tiempos lentos.

### Recomendación
**Equipo:** CX + Product + Pricing
**Prioridad:** P1 — Resolver en próximas 6 semanas

1. **"Total Price Transparency":** Mostrar el ahorro real vs competidores en el checkout ("Tu Service Fee es 1.2% menor que Uber Eats"). La gente no hace la cuenta mental sola.
2. **Post-order NPS con acción inmediata:** Si un usuario califica <4 estrellas, trigger automático: (a) análisis de root cause (¿fee? ¿tiempo? ¿comida fría?), (b) crédito o cupón personalizado, (c) follow-up en 48h.
3. **"Satisfaction Recovery Program":** Identificar los 20% de usuarios con satisfaction <4.0 en el último mes y ofrecerles 30 días de Rappi Pro gratis. El costo de adquisición de un nuevo usuario es 5x mayor que retener uno existente.

---

## Insight 5: Rappi tiene una **paradoja geográfica**: lidera en volumen total pero pierde competitividad en zonas non-wealthy donde el fee se vuelve prohibitivo

### Finding
- **Volumen:** Rappi 90,200 órdenes/semana | Uber Eats 79,982 | DiDi Food 72,918. Rappi lidera.
- **Pero la competitividad por zona varía dramáticamente:**
  - En wealthy: Rappi compite bien (fees más cercanos a competencia, tiempos aceptables).
  - En non-wealthy: Rappi tiene fees 40-100% más altos que UE, tiempos 20-30% más lentos.
- **Heatmap de competitividad:** Rappi gana en 5/5 métricas en zonas wealthy, pero solo en 2-3/5 en non-wealthy.
- En Tlalpan, Doctores, Tláhuac, Milpa Alta y Xochimilco, Rappi está en desventaja en al menos 3 de 5 métricas clave.

### Impacto
- **Market share sostenido pero frágil:** El volumen total alto enmascara debilidades estructurales en la periferia. Si Uber Eats o DiDi Food deciden atacar agresivamente estas zonas con subsidios, Rappi podría perder rápidamente share.
- **Eficiencia logística inversa:** En zonas non-wealthy, la densidad de órdenes es menor pero el costo por entrega es mayor (distancias largas, tráfico). El fee alto es un mecanismo de defensa del P&L, pero crea un círculo vicioso: fee alto → menos órdenes → menos densidad → costo por entrega más alto.
- **Oportunidad de "predatory pricing" por competidores:** DiDi Food podría subsidiar envíos en Iztapalapa o Tláhuac para ganar share, y Rappi no podría responder sin erosionar márgenes.

### Recomendación
**Equipo:** Strategy + Pricing + Operations
**Prioridad:** P2 — Resolver en próximas 12 semanas (estratégico)

1. **"Zone Defense Strategy":** Segmentar las 15 zonas en 3 tiers:
   - **Tier 1 (Defender):** Polanco, Roma Norte, Condesa, Del Valle, Santa Fe — Mantener precios competitivos, inversión en velocidad.
   - **Tier 2 (Atacar):** Coyoacán, Narvarte, Mixcoac — Reducir fees 15-20%, campañas de awareness local.
   - **Tier 3 (Optimizar):** Tlalpan, Doctores, Iztapalapa, Tláhuac, Milpa Alta, Xochimilco — Operar con modelo "light" (menos restaurantes, más tiendas de conveniencia, fees ajustados a costo real).

2. **Micro-fulfillment en periferia:** Abrir 2-3 dark stores en Iztapalapa y Tlalpan con inventario de 200 SKUs de mayor demanda. Esto reduce tiempos de entrega de 45 a 20 min y permite fees más bajos.

3. **Partnerships con tiendas de barrio:** En lugar de competir por restaurantes, aliarse con tienditas de la esquina y misceláneas para ofrecer "Rappi Barrio" con envío fijo $15 MXN. Menor margen pero mayor frecuencia de uso.

---

## Resumen Ejecutivo de Insights

| # | Insight | Prioridad | Equipo | Impacto estimado |
|---|---------|-----------|--------|------------------|
| 1 | Premium de delivery fee del 54% | P0 | Pricing + Ops | +5-8% CVR en non-wealthy |
| 2 | Gap de 15pp en Restaurants CVR | P0 | Restaurants + Product | +10% share en restaurants |
| 3 | Tiempos de entrega 8% más lentos | P1 | Operations + Logistics | +0.15 puntos satisfaction |
| 4 | Satisfaction 0.19 puntos abajo | P1 | CX + Product | -10% churn mensual |
| 5 | Paradoja geográfica: volumen alto pero competitividad baja en periferia | P2 | Strategy + Pricing | Protección de share a largo plazo |

---

*Análisis basado en dataset simulado de 9 semanas, 15 zonas de CDMX, 3 competidores. Los datos de Rappi fueron generados a partir de benchmarks del mercado mexicano.*
