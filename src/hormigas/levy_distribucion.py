"""Ejercicio 6, Parte 2: distribución de longitudes de paso de un vuelo de Lévy.

    P(l) = (mu - 1) * l^(-mu),   l >= 1,  1 < mu <= 3

El factor (mu - 1) normaliza la densidad (su integral de 1 a infinito vale 1).
Es la misma distribución que muestrea levy-step-size en ants_levy.nlogox:
    l = u^(-1/(mu - 1)),  u uniforme en (0, 1]

Genera figuras/levy_distribucion.pdf con P(l) para tres valores de mu.

Uso:  python levy_distribucion.py
"""
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

MUS = [1.1, 2.0, 3.0]
COLORES = ["C0", "C1", "C2"]
FIGURAS = Path(__file__).resolve().parents[2] / "figuras"


def densidad(l, mu):
    return (mu - 1) * l ** (-mu)


def main():
    fig, ax = plt.subplots(figsize=(7, 4))

    l = np.linspace(1, 10, 500)
    for mu, color in zip(MUS, COLORES):
        ax.plot(l, densidad(l, mu), color=color, lw=2, label=rf"$\mu={mu:g}$")

    ax.set_xlim(1, 10)
    ax.set_ylim(0, 2.1)
    ax.set_xlabel("longitud de paso $l$")
    ax.set_ylabel("$P(l)$")
    ax.legend()
    ax.grid(alpha=0.3)

    fig.tight_layout()
    FIGURAS.mkdir(exist_ok=True)
    salida = FIGURAS / "levy_distribucion.pdf"
    fig.savefig(salida)
    print("guardada", salida)

    # Para el texto: qué tan seguido sale un paso largo con cada mu
    for mu in MUS:
        print(f"mu={mu:g}:  P(l > 10) = {10 ** (1 - mu):.3g},  "
              f"P(l > 100) = {100 ** (1 - mu):.3g}")


if __name__ == "__main__":
    main()
