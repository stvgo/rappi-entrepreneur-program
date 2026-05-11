# Exportable del Proceso con IA — AI-First Workflow

**Candidato:** John Stiven Valeriano  
**Plataforma:** OpenClaw (Agente Principal)  
**Modelo:** kimi-k2.6 (OpenCode)  
**Fecha:** Mayo 2026

---

## 1. ¿Por qué AI-First?

Este proyecto adoptó un enfoque **AI-First**: no usé la IA como mero corrector de texto, sino como **co-piloto estratégico** en cada fase del proceso. La IA manejó la ejecución técnica (código, datos, visualizaciones), mientras yo proporcioné dirección de negocio, validé prioridades y ajusté el tono.

La diferencia clave: **la IA orquestó, el humano dirigió.**

---

## 2. Plataforma y Modelo

### OpenClaw
OpenClaw es una plataforma de agentes que permite:
- Acceso directo al filesystem (leer/escribir archivos)
- Ejecución de comandos de shell
- Generación de código Python, documentos Word/Excel
- Análisis de datasets CSV/XLSX
- Comunicación continua en sesión directa

**Por qué OpenClaw:** Permite una interacción fluida donde el agente tiene contexto completo del proyecto, acceso a herramientas, y capacidad de ejecutar código sin context switching.

### kimi-k2.6 (OpenCode)
- **Reasoning estructurado:** Ideal para análisis de datos con múltiples dimensiones
- **Manejo de contexto largo:** Crítico para un proyecto con 15 zonas, 3 competidores, 7 métricas
- **Capacidad técnica:** Genera código funcional, estructura documentos, diseña dashboards

---

## 3. Skills Utilizados

En OpenClaw, los skills son instrucciones especializadas que se activan automáticamente según la tarea. Usé los siguientes:

| Skill | Cuándo se usó | Qué aportó |
|-------|---------------|------------|
| **using-superpowers** | En cada interacción | Direccionó automáticamente a los skills más específicos según la etapa del proyecto. Garantizó que brainstorming se usara antes de cualquier trabajo creativo, y verification-before-completion antes de declarar listo. |
| **brainstorming** | Antes de crear dashboard, app web, documentos | Definió estructura de entregables, métricas clave, formato de insights. Evitó rework al establecer scope antes de escribir código. |
| **writing-plans** | Para cada entregable (2.1, 2.2, 2.3) | Generó planes de implementación con archivos, dependencias y orden de ejecución. Proporcionó hoja de ruta clara. |
| **verification-before-completion** | Antes de declarar cada entregable listo | Detectó gaps críticos: falta de productos estandarizados en 2.1, ausencia de análisis de promociones en 2.2. |

---

## 4. Archivos de Contexto (.md)

El workspace de OpenClaw incluye archivos que persisten entre sesiones:

- **AGENTS.md:** Reglas del workspace — qué es seguro, qué requiere aprobación, convenciones de memoria
- **SOUL.md:** Personalidad del agente — genuinamente útil, con opiniones, resourceful, trust-based
- **USER.md:** Perfil del humano — nombre, timezone, preferencias
- **MEMORY.md:** Memoria de largo plazo — decisiones, lecciones, contexto que sobrevive reinicios
- **HEARTBEAT.md:** Checklist periódico de tareas

Estos archivos permitieron coherencia durante todo el proyecto sin repetir supuestos o reglas.

---

## 5. Flujo de Trabajo AI-First

### Fase 1: Análisis del Case
- **IA:** Extrajo requerimientos del PDF, identificó entregables 2.1, 2.2, 2.3, 5
- **Humano:** Validó comprensión, ajustó scope

### Fase 2: Planificación
- **IA:** Estructuró plan de implementación con archivos y dependencias
- **Humano:** Validó prioridades, ajustó alcance

### Fase 3: Generación de Datos y Análisis
- **IA:** Generó datasets CSV simulados, calculó métricas competitivas, creó 14 hojas de Excel con 6 gráficos
- **Humano:** Revisó métricas, ajustó supuestos

### Fase 4: Desarrollo de App Web
- **IA:** Código completo Streamlit, CSS, Plotly, integración OpenRouter
- **Humano:** Pruebas de usuario, ajustes de UX

### Fase 5: Documentación
- **IA:** Generó Word, Markdown, formatting
- **Humano:** Revisión final, ajustes de tono

### Fase 6: Verificación y QA
- **IA:** Detectó gaps, validó requisitos
- **Humano:** Aprobación de entregables

---

## 6. Distribución de Trabajo: Humano vs IA

| Tarea | IA (OpenClaw + kimi-k2.6) | Humano |
|-------|---------------------------|--------|
| Análisis del case | Extracción de requerimientos, identificación de gaps | Validación de scope |
| Plan de recolección | Estructura, tablas, justificaciones | Input personal ("como usuario de Rappi..."), validación de criterios |
| Análisis de datos | Dataset, cálculos, tablas pivot, gráficos Excel | Revisión de métricas |
| Top 6 Insights | Redacción completa de findings, impactos y recomendaciones | Validación de prioridades, ajuste de timelines |
| App web | Código Streamlit + CSS + Plotly + OpenRouter | Pruebas UX |
| Documentación | Word + Markdown + formatting | Revisión final, ajustes de tono |
| QA | Detección de gaps, validación de requisitos | Aprobación de entregables |

---

## 7. Stack Tecnológico

| Capa | Tecnología |
|------|-----------|
| Plataforma de agentes | OpenClaw |
| Modelo LLM | kimi-k2.6 (OpenCode) |
| Lenguaje | Python 3.11 |
| Análisis de datos | Pandas, NumPy, OpenPyXL |
| Visualizaciones | Plotly, Excel |
| App web | Streamlit |
| IA real en app | OpenRouter (modelos gratuitos) |
| Contexto persistente | Archivos .md (AGENTS.md, SOUL.md, USER.md, MEMORY.md) |

---

## 8. Conclusión

Este proyecto demostró que **AI-First no es delegación ciega, es orquestación inteligente**. La IA manejó la ejecución técnica, la estructuración de datos y la generación de contenido, mientras el humano proporcionó contexto de negocio, validó dirección estratégica y ajustó prioridades.

El uso de skills como `using-superpowers` garantizó que cada tarea usara la metodología más adecuada. Los archivos `.md` de contexto mantuvieron coherencia. El resultado: un análisis competitivo completo con dashboard, app web interactiva, y documentación ejecutiva — todo en un flujo orquestado por IA pero dirigido por criterio humano.

---

*Rappi Entrepreneur Program | Mayo 2026 | John Stiven Valeriano*
