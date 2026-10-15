# make        -> compila $(MAIN).pdf en la raíz; los auxiliares van a out/
# make watch  -> recompila sola al guardar (latexmk -pvc)
# make force  -> recompila aunque latexmk crea que no hay nada que hacer
# make zip    -> empaqueta los fuentes para subirlos a Overleaf
# make clean  -> borra out/ y el synctex; conserva el PDF
# make purge  -> borra también el PDF
#
# El proyecto está pensado para compilar igual en local y en Overleaf.  Overleaf
# NO usa este Makefile: compila con su propia configuración, así que allá no
# existe out/ y los auxiliares los administra él.  Por eso latexmkrc no fija
# directorios de salida: es el único archivo de build que Overleaf sí lee.
#
# El PDF y el .synctex.gz quedan en la raíz a propósito: para abrir el documento
# sin buscarlo y para que el editor pueda saltar del PDF al fuente.  Todo lo
# demás (.aux, .log, .toc, .bbl, .bcf, .fls...) vive en out/, que no se versiona.
#
# Dos cosas hacen que esto funcione, y las dos son necesarias:
#
#  1. "-auxdir=out -outdir=."  reparte la salida: auxiliares a out/, PDF y
#     synctex a la raíz.
#  2. El mkdir de abajo.  \include escribe un .aux por archivo incluido dentro
#     de out/, y pdflatex NO crea esos subdirectorios: sin ellos aborta con
#     "I can't write on file `capitulos/01-x.aux'" y luego "Emergency stop".
#     Los subdirectorios se deducen de dónde hay .tex, así que no hay que tocar
#     esta línea al agregar carpetas.

MAIN  = main
OUT   = out
ZIP   = overleaf.zip
FLAGS = -pdf -synctex=1 -auxdir=$(OUT) -outdir=. -interaction=nonstopmode

OUTDIRS = $(OUT) $(addprefix $(OUT)/,$(sort $(dir $(wildcard */*.tex))))

all:
	@mkdir -p $(OUTDIRS)
	latexmk $(FLAGS) -halt-on-error $(MAIN).tex

watch:
	@mkdir -p $(OUTDIRS)
	latexmk -pvc $(FLAGS) $(MAIN).tex

# Hace falta cuando agregas una figura sin tocar ningún .tex: latexmk decide si
# recompila mirando los fuentes, y un archivo nuevo no cambia ninguno.
force:
	@mkdir -p $(OUTDIRS)
	latexmk -g $(FLAGS) -halt-on-error $(MAIN).tex

# Empaqueta para «New Project -> Upload Project» de Overleaf: sólo fuentes, con
# main.tex en la raíz del zip y sin carpeta contenedora, que es como Overleaf
# detecta solo el documento principal.  Deja fuera out/, el PDF, el synctex, el
# historial de git y la basura que agrega macOS.
zip:
	@rm -f $(ZIP)
	@zip -r -q $(ZIP) . \
	  -x '$(OUT)/*' '.git/*' '*.DS_Store' '__MACOSX/*' \
	     '$(MAIN).pdf' '$(MAIN).synctex.gz' '*.zip'
	@echo "$(ZIP) listo para subir a Overleaf"

# Como todo lo auxiliar vive en out/, limpiar es borrar un directorio.
clean:
	rm -rf $(OUT) $(MAIN).synctex.gz

purge: clean
	rm -f $(MAIN).pdf

.PHONY: all watch force zip clean purge
