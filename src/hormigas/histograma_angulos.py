"""Ejercicio 6, Parte 1: histograma de los ángulos de giro de wiggle.

Lee el plot exportado de NetLogo (datos/angulos_original.csv) y lo compara con
la distribución teórica del giro neto de wiggle:

    giro = (random 40) - (random 40),   con a, b uniformes en {0, ..., 39}

Para un giro k hay 40 - |k| parejas (a, b) con a - b = k, de 40^2 = 1600
posibles, así que
    P(k) = (40 - |k|) / 1600,   k = -39, ..., 39   (triangular, pico en 0).

Genera figuras/histograma_angulos.pdf.

Uso:  python histograma_angulos.py
"""
import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

AQUI = Path(__file__).resolve().parent
DATOS = AQUI / "datos" / "angulos_original.csv"
FIGURAS = AQUI.parents[1] / "figuras"


def leer_plot_netlogo(ruta):
    """Regresa (x, y) de los puntos del pen en un CSV de export-plot."""
    with open(ruta, newline="", encoding="utf-8") as f:
        filas = list(csv.reader(f))
    # Los puntos empiezan después del encabezado "x","y","color","pen down?"
    inicio = next(i for i, fila in enumerate(filas) if fila[:2] == ["x", "y"]) + 1
    puntos = [fila for fila in filas[inicio:] if fila]
    x = np.array([float(fila[0]) for fila in puntos])
    y = np.array([float(fila[1]) for fila in puntos])
    return x, y


def main():
    k, conteos = leer_plot_netlogo(DATOS)
    total = conteos.sum()
    teorica = total * (40 - np.abs(k)) / 1600

    media = (k * conteos).sum() / total
    desv = np.sqrt(((k - media) ** 2 * conteos).sum() / total)
    # Varianza de una uniforme en {0..39} es (40^2 - 1)/12; la resta suma dos
    desv_teo = np.sqrt(2 * (40**2 - 1) / 12)

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(k, conteos, width=1, color="C0", alpha=0.7, label="simulación (NetLogo)")
    ax.plot(k, teorica, color="C3", lw=2,
            label=r"teórica: $N\,(40-|k|)/1600$")
    ax.set_xlim(-41, 41)
    ax.set_xlabel("ángulo de giro $k$ (grados)")
    ax.set_ylabel("frecuencia")
    ax.legend(loc="upper right")
    ax.grid(alpha=0.3)

    fig.tight_layout()
    FIGURAS.mkdir(exist_ok=True)
    salida = FIGURAS / "histograma_angulos.pdf"
    fig.savefig(salida)
    print("guardada", salida)
    print(f"giros registrados: {total:.0f}")
    print(f"media: {media:.3f}  (teórica 0)")
    print(f"desviación estándar: {desv:.2f}  (teórica {desv_teo:.2f})")


if __name__ == "__main__":
    main()
