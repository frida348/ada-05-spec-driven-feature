# AI Usage Log

Este documento registra las interacciones, directrices y herramientas utilizadas por el asistente de IA durante el desarrollo del feature Customer Search en el repositorio `ada-05-spec-driven-feature`.

---

## Información del Asistente

- **Modelo:** Gemini 3.8 Flash (High) / Antigravity Agent
- **Fecha:** 2026-09-24
- **Modo:** Spec-Driven Development / Pair Programming

---

## Resumen de Interacciones

| Turno | Solicitud del Usuario | Acción del Agente | Resultado / Tareas Afectadas |
|---|---|---|---|
| 1 | Solicitud inicial de creación de código según archivos del proyecto. | Análisis de especificaciones, creación inicial de la arquitectura y suite de pruebas. | T-01 a T-06 (implementación inicial) |
| 2 | Instrucción estricta de ejecución previa: leer requerimientos, arquitectura, agentes, e implementar tarea por tarea. | Auditoría de las reglas, confirmación de correspondencia y propuesta de ejecución por fases. | Alineación metodológica estricta |
| 3 | "Realiza tarea por tarea" | Limpieza de archivos previos para reiniciar formalmente desde el estado inicial; ejecución de T-01 (inspección de repositorio y línea base de pruebas). | T-01 completada |
| 4 | "si, continuamos..." (con regla de detección de contradicciones). | Verificación de coherencia entre `REQUIREMENTS.md` y `SPEC.md`, implementación de modelo `Customer` y pruebas asociadas. | T-02 completada |
| 5 | "Si" | Verificación de requisitos, implementación de repositorio desacoplado (`CustomerRepository` e `InMemoryCustomerRepository`) y pruebas de lógica de búsqueda. | T-03 completada |
| 6 | "Procedamos" | Verificación de reglas de validación, implementación de excepciones, validador de texto (`SearchInputValidator`) y servicio (`CustomerSearchService`) con cortocircuito ante datos inválidos. | T-04 completada |
| 7 | "Continuemos" | Verificación de criterios y escenarios, implementación de interfaz (`CustomerSearchInterface`) y suite exhaustiva para TS-01..TS-13 y AC-01..AC-12. | T-05 completada |
| 8 | "sii" | Auditoría final de documentación, verificación de que ningún archivo de especificación fue alterado y reporte formal de finalización. | T-06 completada |
| 9 | Solicitud de matriz de trazabilidad en `docs/traceability.md`. | Generación de la tabla de trazabilidad mapeando requerimientos a escenarios, pruebas y archivos. | `docs/traceability.md` |
| 10 | Solicitud de `results/agent-report.md` y organización del proyecto. | Reorganización en `src/`, generación de `README.md`, `AI_USAGE_LOG.md` y `results/agent-report.md`. | Reporte final y estructura de proyecto |

---

## Directrices de Seguridad y Metodología Aplicadas

1. **No inventar requerimientos:** Todas las reglas de negocio provienen estrictamente de `REQUIREMENTS.md` y `SPEC.md`.
2. **Preguntas abiertas:** Ni Q-01 (recorte de espacios) ni Q-02 (longitud mínima) fueron asumidas o resueltas de manera arbitraria; se siguieron las directrices provisionales de `SPEC.md`.
3. **Inmutabilidad de especificaciones:** Los archivos `REQUIREMENTS.md` y `SPEC.md` no fueron modificados para acomodar código.
4. **Verificación continua:** Se ejecutó `pytest` después de cada tarea para asegurar cero regresiones.
