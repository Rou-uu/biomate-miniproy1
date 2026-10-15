# Configuración mínima y portable de latexmk.
$pdf_mode   = 1;   # pdfLaTeX
$bibtex_use = 2;   # ejecuta biber/bibtex y limpia sus auxiliares

# A propósito NO se fijan aquí $aux_dir ni $out_dir.  Overleaf lee este archivo
# y compila con su propio directorio de salida; fijarlos aquí puede romperle la
# compilación.  El reparto raíz/out lo hace el Makefile, que Overleaf no usa.
