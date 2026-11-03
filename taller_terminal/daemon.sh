#!/usr/bin/env bash
dir_path="$(pwd)"
scripts="$dir_path/scripts"
resultados="$dir_path/resultados"

mkdir -p "$resultados"
python "$scripts/herramienta.py" --help
python "$scripts/herramienta.py" --accion resumen > "$resultados/resumen.txt"
python "$scripts/herramienta.py" --accion buscar --nombre "cable USB"
