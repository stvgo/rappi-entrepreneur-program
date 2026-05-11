# Análisis de Estrategia Promocional

**Contexto:** Análisis de promociones activas por competidor en 10 productos × 15 zonas de CDMX (150 combinaciones producto/zona por competidor). Datos del dataset de SmartComp.

---

## 1. Resumen Ejecutivo

| Métrica | Rappi | Uber Eats | DiDi Food |
|---------|-------|-----------|-----------|
| **Sin promoción** | 95/150 (63.3%) | 83/150 (55.3%) | 98/150 (65.3%) |
| **Con promoción** | 55/150 (36.7%) | 67/150 (44.7%) | 52/150 (34.7%) |
| **Promo más frecuente** | 2x1 en combos (22) | 15% off primer orden (29) | DiDi Pass mensual (18) |

**Hallazgo clave:** Rappi no está necesariamente "perdiendo" en volumen absoluto de promociones, pero **la naturaleza de sus promociones es menos efectiva**: son condicionales (requieren monto mínimo) mientras Uber Eats usa descuentos directos y programas de fidelidad.

---

## 2. Tipos de Promociones por Competidor

### 2.1 Rappi — Promociones condicionales

| Promoción | Frecuencia | % del total | Característica |
|-----------|-----------|-------------|----------------|
| Ninguna | 95 | 63.3% | — |
| 2x1 en combos | 22 | 14.7% | Solo fast food |
| Envío gratis >$200 | 20 | 13.3% | Umbral alto |
| 10% off próxima compra | 13 | 8.7% | Diferido |

**Problema:** Las promociones son condicionales. "Envío gratis >$200" no aplica a pedidos pequeños. "10% off próxima compra" no reduce el precio percibido en el checkout actual.

### 2.2 Uber Eats — Descuentos directos + fidelidad

| Promoción | Frecuencia | % del total | Característica |
|-----------|-----------|-------------|----------------|
| Ninguna | 83 | 55.3% | — |
| 15% off primer orden | 29 | 19.3% | Directo, inmediato |
| Uber One 50% off | 21 | 14.0% | Programa de suscripción |
| Envío gratis siempre | 17 | 11.3% | Para miembros Uber One |

**Estrategia:** Fuerte inversión en adquisición (19.3% con 15% off) + retención vía Uber One.

### 2.3 DiDi Food — Mix de suscripción y descuentos

| Promoción | Frecuencia | % del total | Característica |
|-----------|-----------|-------------|----------------|
| Ninguna | 98 | 65.3% | — |
| DiDi Pass mensual | 18 | 12.0% | Suscripción tipo Uber One |
| Envío gratis >$150 | 17 | 11.3% | Umbral más bajo que Rappi |
| 20% off restaurants | 17 | 11.3% | Ataca vertical core |

**Estrategia:** Menor frecuencia pero mayor agresividad cuando ataca. "20% off restaurants" golpea donde Rappi es más débil.

---

## 3. Análisis por Tipo de Zona

### Wealthy (60 combinaciones por competidor)

| Competidor | Sin promo | Con promo |
|------------|-----------|-----------|
| Rappi | 33 (55.0%) | 27 (45.0%) |
| Uber Eats | 34 (56.7%) | 26 (43.3%) |
| DiDi Food | 33 (55.0%) | 27 (45.0%) |

**Insight:** En zonas wealthy, los tres competidores tienen niveles similares. La batalla es por programas de fidelidad.

### Mixed (40 combinaciones por competidor)

| Competidor | Sin promo | Con promo |
|------------|-----------|-----------|
| Rappi | 29 (72.5%) | 11 (27.5%) |
| Uber Eats | 22 (55.0%) | 18 (45.0%) |
| DiDi Food | 27 (67.5%) | 13 (32.5%) |

**Insight:** Rappi está **muy por debajo** en zonas mixed. Uber está captando usuarios nuevos agresivamente.

### Non-wealthy (50 combinaciones por competidor)

| Competidor | Sin promo | Con promo |
|------------|-----------|-----------|
| Rappi | 33 (66.0%) | 17 (34.0%) |
| Uber Eats | 27 (54.0%) | 23 (46.0%) |
| DiDi Food | 38 (76.0%) | 12 (24.0%) |

**Insight:** DiDi tiene mayor % sin promos pero usa umbral más bajo ($150 vs $200 de Rappi).

---

## 4. Impacto en Precio Final

| Escenario | Rappi | Uber Eats | DiDi Food |
|-----------|-------|-----------|-----------|
| Big Mac sin promo | $121 MXN | $118 MXN | $114 MXN |
| Big Mac con mejor promo | $121 MXN | $111 MXN | $120 MXN |

**Conclusión:** Las promociones de Uber son más consistentes. El usuario percibe que "Uber siempre tiene descuento" mientras Rappi parece "sin promociones".

---

## 5. Recomendaciones

### Corto plazo (2-4 semanas)
1. **"Bienvenida Rappi"**: 15% off en primera orden sin condiciones
2. **Bajar umbral envío gratis**: De $200 a $150 MXN
3. **Promociones en retail**: "3x2 en Coca-Cola", "Agua $10 MXN"

### Mediano plazo (4-8 semanas)
4. **"Rappi Pro Lite"**: Suscripción $49 MXN/mes con envío gratis >$150 y 5% cashback
5. **"Martes de Rappi"**: Día semanal con rotación de promos

### Largo plazo (8-12 semanas)
6. **Promociones geo-targeted dinámicas**: Si usuario abre Uber, enviar push con envío gratis

---

*John Stiven Valeriano | Mayo 2026*
