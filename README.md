# Customer Search Feature (ada-05-spec-driven-feature)

Feature de búsqueda de clientes por nombre y correo electrónico con soporte para coincidencias parciales, insensibilidad a mayúsculas y minúsculas, validación de entradas y comportamiento de solo lectura, desarrollado bajo una metodología dirigida por especificaciones (*Spec-Driven Development*).

---

## Estructura del Proyecto

```
ada-05-spec-driven-feature/
├── README.md              # Documentación general del proyecto
├── REQUIREMENTS.md        # Requerimientos de negocio y funcionales
├── SPEC.md                # Especificación técnica, criterios de aceptación y escenarios
├── ARCHITECTURE.md        # Arquitectura de capas y diseño de interfaces
├── TASKS.md               # Secuencia de tareas de implementación
├── AGENTS.md              # Reglas y directrices para agentes
├── AI_USAGE_LOG.md        # Registro de interacción con el asistente de IA
├── src/                   # Código fuente de producción
│   └── customer_search/
│       ├── __init__.py
│       ├── exceptions.py
│       ├── interface.py
│       ├── models.py
│       ├── repository.py
│       ├── service.py
│       └── validator.py
├── tests/                 # Suite de pruebas automatizadas con pytest
│   ├── __init__.py
│   ├── test_interface.py
│   ├── test_models.py
│   ├── test_repository.py
│   ├── test_service.py
│   ├── test_spec_scenarios.py
│   └── test_validator.py
├── docs/
│   └── traceability.md    # Matriz de trazabilidad de requerimientos
└── results/
    └── agent-report.md    # Reporte de ejecución del agente por tareas
```

---

## Requisitos y Ejecución de Pruebas

### Requisitos
- Python 3.12+
- Pytest

### Ejecución de Pruebas
Para ejecutar la suite completa de pruebas:

```bash
pytest -v
```

Todas las pruebas (41 casos de prueba cubriendo TS-01 a TS-13 y AC-01 a AC-12) deben pasar sin fallos.
