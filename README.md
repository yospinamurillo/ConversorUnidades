[README.md](https://github.com/user-attachments/files/28039095/README.md)
# ConversorUnidades
Conversor de unidades simple
# 🔄 Conversor de Unidades — `conversor-fisica-python`

Módulo de código libre para la conversión de unidades físicas (temperatura y distancia), diseñado como herramienta de apoyo para docentes y estudiantes de física. Desarrollado sin dependencias externas.

---

## 📋 Tabla de Contenidos

- [Descripción](#descripción)
- [Requisitos](#requisitos)
- [Instalación y Uso](#instalación-y-uso)
- [Flujo de Configuración](#flujo-de-configuración)
- [Ejemplo de Uso](#ejemplo-de-uso)
- [Manejo de Errores](#manejo-de-errores)
- [Personalización](#personalización)
- [Licencia](#licencia)

---

## Descripción

`conversor-fisica-python` es un módulo de consola interactivo que permite convertir valores entre unidades de temperatura (Celsius ↔ Fahrenheit) y distancia (kilómetros ↔ millas). El sistema guía al usuario paso a paso mediante preguntas en pantalla, sin requerir ninguna librería externa.

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
git clone https://github.com/xxxxx/conversor-fisica-python.git
cd conversor-fisica-python
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

## Ejemplo de Uso

Conversión de 100 °C a Fahrenheit:

```
tipo_medida    → temp
valor_origen   → 100
unidad_destino → F
```

**Salida:**

```
Resultado: 100.00 °C equivalen a 212.00 °F.
```

---

## Manejo de Errores

Si se ingresa una unidad no reconocida, el sistema interrumpe la ejecución y muestra el siguiente mensaje:

```
[ALERTA] Unidad no reconocida. Usa solo C, F, KM o MI.
```

Esto previene cálculos incorrectos y orienta al usuario a ingresar un valor válido.

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

---

## Licencia

Este proyecto está distribuido bajo la licencia **MIT**. Consulta el archivo `LICENSE` para más información.
