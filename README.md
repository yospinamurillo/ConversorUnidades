# 🔄 Conversor de Unidades — `conversor-fisica-python`

Módulo de código libre para la conversión de unidades físicas (temperatura y distancia), diseñado como herramienta de apoyo para docentes y estudiantes de física. Desarrollado sin dependencias externas.

---

## 📋 Tabla de Contenidos

- [Descripción](#descripción)
- [Requisitos](#requisitos)
- [Instalación y Uso](#instalación-y-uso)
- [Flujo de Configuración](#flujo-de-configuración)
- [Flujo de Ejecución](#flujo-de-ejecución)
- [Ejemplo de Uso](#ejemplo-de-uso)
- [Manejo de Errores](#manejo-de-errores)
- [Personalización](#personalización)
- [Licencia](#licencia)

---

## Descripción

`conversor-fisica-python` es un módulo de consola interactivo que permite convertir valores entre unidades de temperatura (Celsius ↔ Fahrenheit) y distancia (kilómetros ↔ millas). El sistema guía al usuario a través de una interfaz por consola, solicitando la magnitud a convertir, el valor y la unidad destino.

---

## Requisitos

| Requisito   | Versión mínima |
|-------------|----------------|
| Python      | 3.10 o superior |
| Librerías externas | ❌ Ninguna |

---

## Instalación y Uso

**1. Clonar el repositorio:**

```bash
git clone https://github.com/yospinamurillo/ConversorUnidades.git
cd ConversorUnidades
```

**2. Ejecutar el programa:**

```bash
python convertidor_uni.py
```

No se requiere ningún paso de instalación adicional.

---

## Flujo de Configuración

El sistema solicita tres parámetros de forma secuencial en pantalla:

| Paso | Parámetro        | Descripción                                      | Valores válidos          |
|------|------------------|--------------------------------------------------|--------------------------|
| 1    | `tipo_medida`    | Tipo de magnitud a convertir                     | `temp` · `dist`          |
| 2    | `valor_origen`   | Valor numérico que se desea convertir            | Cualquier número         |
| 3    | `unidad_destino` | Unidad a la que se realizará la conversión       | `C` · `F` (temp) / `KM` · `MI` (dist) |

---

## Flujo de Ejecución

### Diagrama de flujo principal

```
┌─────────────────────────────┐
│   Inicio del Programa       │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  Solicitar tipo_medida      │
│  (temp / dist)              │
└──────────────┬──────────────┘
               │
       ┌───────┴───────┐
       │               │
       ▼               ▼
   ┌────────┐    ┌────────┐
   │  TEMP  │    │  DIST  │
   └───┬────┘    └───┬────┘
       │             │
       ▼             ▼
┌────────────────┐ ┌────────────────┐
│ Solicitar valor│ │ Solicitar valor│
│  (números)    │ │  (números)     │
└───┬────────────┘ └────┬───────────┘
    │                   │
    ▼                   ▼
┌────────────────────────────────┐
│  Solicitar unidad_destino      │
│  (C/F para temp, KM/MI dist)   │
└───┬───────────────────────────┬┘
    │                           │
    ▼ Válida                    ▼ Inválida
┌──────────────────┐      ┌───────────────────┐
│  Realizar Cálculo│      │ Error: Unidad no  │
└────┬─────────────┘      │ reconocida        │
     │                    └────────┬──────────┘
     ▼                            │
┌──────────────────┐              │
│ Mostrar Resultado│              │
└────┬─────────────┘              │
     │                            │
     └────────────────┬───────────┘
                      │
                      ▼
          ┌──────────────────────┐
          │   Fin del Programa   │
          └──────────────────────┘
```

### Conversión de Temperatura (Celsius ↔ Fahrenheit)

```
┌──────────────────────────────────┐
│  Conversión de Temperatura       │
└──────────┬───────────────────────┘
           │
    ┌──────┴────────┐
    │               │
    ▼               ▼
  C → F          F → C
    │               │
    ▼               ▼
(C×9/5)+32    (F-32)×5/9
    │               │
    └───────┬───────┘
            ▼
      Mostrar Resultado
```

### Conversión de Distancia (KM ↔ MI)

```
┌──────────────────────────────────┐
│  Conversión de Distancia         │
└──────────┬───────────────────────┘
           │
    ┌──────┴────────┐
    │               │
    ▼               ▼
  KM → MI        MI → KM
    │               │
    ▼               ▼
  KM × 0.621    MI / 0.621
    │               │
    └───────┬───────┘
            ▼
      Mostrar Resultado
```

---

## Ejemplo de Uso

### Conversión de 100 °C a Fahrenheit:

```
tipo_medida    → temp
valor_origen   → 100
unidad_destino → F
```

**Salida:**

```
Resultado: 100.00 °C equivalen a 212.00 °F.
```

### Conversión de 10 km a millas:

```
tipo_medida    → dist
valor_origen   → 10
unidad_destino → MI
```

**Salida:**

```
Resultado: 10.00 KM equivalen a 6.21 MI.
```

---

## Manejo de Errores

Si se ingresa una unidad no reconocida, el sistema interrumpe la ejecución y muestra el siguiente mensaje:

```
[ALERTA] Unidad no reconocida. Usa solo C, F, KM o MI.
```

Esto previene cálculos incorrectos y orienta al usuario a ingresar un valor válido.

**Casos manejados:**

| Caso | Comportamiento |
|------|---|
| Unidad no válida | Se muestra alerta y se interrumpe la ejecución |
| Valor no numérico | Sistema solicita reintentar la entrada |
| Tipo de medida inválido | Se solicita ingresar `temp` o `dist` |

---

## Personalización

Al inicio del archivo `convertidor_uni.py` se encuentra la variable:

```python
DECIMALES_MOSTRADOS = 2
```

Los docentes pueden modificar este valor directamente en el código para obtener mayor precisión en cálculos de laboratorio. Por ejemplo, para mostrar 4 decimales:

```python
DECIMALES_MOSTRADOS = 4
```

**Ejemplos de impacto:**

```python
# Con DECIMALES_MOSTRADOS = 2
Resultado: 100.00 °C equivalen a 212.00 °F.

# Con DECIMALES_MOSTRADOS = 4
Resultado: 100.0000 °C equivalen a 212.0000 °F.
```

---

## Licencia

Este proyecto está distribuido bajo la licencia **MIT**. Consulta el archivo `LICENSE` para más información.
