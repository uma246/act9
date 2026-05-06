# 🌡️ Temperature Monitor - Control de Temperatura Industrial

Sistema simple y robusto para monitoreo de temperatura en equipos industriales.

## Descripción

Aplicación que evalúa lecturas de temperatura y determina si el equipo está en condición normal u alarma.

**Umbral de alarma:** 80°C

## Características

- ✅ Lectura de temperatura desde usuario
- ✅ Detección de alarmas cuando T > 80°C
- ✅ Validación de errores de sensor (temperaturas negativas)
- ✅ Pruebas automáticas con pytest
- ✅ Manejo robusto de errores

## Requisitos

- Python 3.7+
- pytest (para ejecutar pruebas)

## Instalación

```bash
git clone <repo-url>
cd temperature-monitor
pip install pytest
```

## Uso

```bash
python main.py
```

Ejemplo:
```
Ingrese temperatura (°C): 85
⚠️ ALARMA: Temperatura alta detectada
```

## Pruebas

Ejecutar todas las pruebas:
```bash
pytest tests/
```

Ejecutar con detalle:
```bash
pytest tests/ -v
```

## Estructura del Proyecto

```
temperature-monitor/
├── main.py              # Aplicación principal
├── temperature.py       # Lógica de control de temperatura
├── tests/
│   └── test_temperature.py  # Suite de pruebas
├── README.md            # Este archivo
└── .gitignore          # Configuración de Git
```

## Validaciones Implementadas

| Caso | Resultado |
|------|-----------|
| T > 80°C | ⚠️ ALARMA |
| T ≤ 80°C | ✅ OK |
| T < 0 | ❌ Error de sensor |
| Input no numérico | ❌ Error de entrada |

## Changelog

### v1.0.0
- Implementación inicial de control de temperatura
- Validación de sensor
- Manejo de errores de usuario
