# Biología Matemática I — Miniproyecto 1 (ejercicios 1, 2 y 6)

Proyecto LaTeX. `main.tex` ensambla el documento y `preambulo.tex` concentra
paquetes, formato y macros. Cada ejercicio vive en su propio archivo dentro de
`ejercicios/`, así que reordenarlos es mover una línea de `main.tex`.

## Compilar

```bash
make          # genera main.pdf en esta carpeta
make watch    # recompila sola cada vez que guardas
make clean    # borra out/, conserva el PDF
make purge    # borra también el PDF
```

El **PDF queda aquí, en la raíz**, junto con `main.synctex.gz` (para que el
editor salte del PDF al fuente). Todo lo que genera LaTeX —`.aux`, `.log`,
`.toc`, `.bbl`, `.bcf`, `.fls`— vive en `out/`, que se puede borrar entera sin
perder nada.

Si agregas una figura sin tocar ningún `.tex`, latexmk cree que no hay nada que
recompilar: usa `make force`.

## Estructura

```
main.tex            ensambla el documento; aquí se activa o desactiva cada ejercicio
preambulo.tex       paquetes, formato, entornos y macros
ejercicios/         un archivo por ejercicio, con el número del enunciado (01-, 02-, 06-)
figuras/            las gráficas que piden los tres ejercicios
bibliografia.bib    referencias del ejercicio 2 (APA 7)
out/                salida de LaTeX; desechable
```

## Notas

- **`\pendiente{...}`** marca en rojo lo que falta escribir. Al terminar,
  descomenta en `preambulo.tex` la línea `\renewcommand{\pendiente}[1]{}` y
  desaparecen todas sin tener que borrarlas una por una.
- **Referencias cruzadas**: `\Cref{...}` escribe solo «Tabla 1»,
  «Ejercicio 2». Si sale «??», falta el `\crefname` de ese
  entorno en el preámbulo.
- **Escribir sólo una parte**: mientras trabajas en un ejercicio, comenta los `\input` de los demás en `main.tex`
  y la compilación se acorta.

## Overleaf

El proyecto compila igual aquí y en Overleaf; puedes escribir en local y usar
Overleaf para ver el resultado o revisarlo con alguien más.

```bash
make zip      # deja overleaf.zip con los fuentes, listo para subir
```

En Overleaf: **New Project → Upload Project** y arrastra el zip. Trae `main.tex`
en la raíz, así que detecta solo el documento principal. En **Menu** confirma
*Compiler* = **pdfLaTeX** y *TeX Live version* = **2023 o posterior**.

Overleaf **no usa el `Makefile`**: compila con su propia configuración, así que
allá no existe `out/` y los auxiliares los administra él. Por eso `latexmkrc`
—el único archivo de build que Overleaf sí lee— no fija directorios de salida.

Si el proyecto ya existe en Overleaf, no subas el zip encima: agrega archivos
pero no borra los viejos.
