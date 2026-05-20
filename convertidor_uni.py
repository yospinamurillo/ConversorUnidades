# ============================================================
#  Conversor de Unidades — conversor-fisica-python
#  Licencia: MIT
# ============================================================

DECIMALES_MOSTRADOS = 2  # Cambia a 4 para mayor precisión en laboratorio


def convertir_temperatura(valor, unidad_destino):
    if unidad_destino == "F":
        return (valor * 9 / 5) + 32, "°C", "°F"
    elif unidad_destino == "C":
        return (valor - 32) * 5 / 9, "°F", "°C"
    else:
        return None, None, None


def convertir_distancia(valor, unidad_destino):
    if unidad_destino == "KM":
        return valor * 1.60934, "MI", "KM"
    elif unidad_destino == "MI":
        return valor / 1.60934, "KM", "MI"
    else:
        return None, None, None


def main():
    print("=" * 50)
    print("   CONVERSOR DE UNIDADES — Física")
    print("=" * 50)

    tipo_medida = input("\nPaso 1 — tipo_medida (temp / dist): ").strip().lower()

    if tipo_medida not in ("temp", "dist"):
        print("[ALERTA] Tipo de medida no reconocido. Usa solo 'temp' o 'dist'.")
        return

    try:
        valor_origen = float(input("Paso 2 — valor_origen: ").strip())
    except ValueError:
        print("[ALERTA] El valor debe ser un número.")
        return

    unidad_destino = input("Paso 3 — unidad_destino (C/F para temp | KM/MI para dist): ").strip().upper()

    if tipo_medida == "temp":
        resultado, unidad_origen, unidad_final = convertir_temperatura(valor_origen, unidad_destino)
    else:
        resultado, unidad_origen, unidad_final = convertir_distancia(valor_origen, unidad_destino)

    if resultado is None:
        print("[ALERTA] Unidad no reconocida. Usa solo C, F, KM o MI.")
        return

    print(f"\nResultado: {valor_origen:.{DECIMALES_MOSTRADOS}f} {unidad_origen} equivalen a {resultado:.{DECIMALES_MOSTRADOS}f} {unidad_final}.")


if __name__ == "__main__":
    main()
