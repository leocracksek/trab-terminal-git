"""Herramienta de terminal para consultar un CSV sintético. Python 3.8+."""
import argparse
import csv
from pathlib import Path


def cargar_objetos(ruta):
    """Lee el CSV y convierte cada cantidad de texto a entero."""
    objetos = []
    with Path(ruta).open(encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        if lector.fieldnames != ["nombre", "categoria", "cantidad"]:
            raise ValueError("Cabecera esperada: nombre,categoria,cantidad")
        for fila in lector:
            if None in fila or any(v is None or not v.strip() for v in fila.values()):
                raise ValueError("Hay una fila incompleta o con columnas de más")
            cantidad = int(fila["cantidad"])
            if cantidad < 0:
                raise ValueError("Las cantidades no pueden ser negativas")
            objetos.append({"nombre": fila["nombre"].strip(),
                            "categoria": fila["categoria"].strip(),
                            "cantidad": cantidad})
    return objetos


def unidades_por_categoria(objetos):
    """Acumula unidades por categoría; no cuenta filas."""
    totales = {}
    for objeto in objetos:
        categoria = objeto["categoria"]
        totales[categoria] = totales.get(categoria, 0) + objeto["cantidad"]
    return totales


def buscar_objeto(objetos, nombre):
    """Busca un nombre exacto sin distinguir mayúsculas de minúsculas."""
    for objeto in objetos:
        if objeto["nombre"].casefold() == nombre.casefold():
            return objeto
    return None


def main():
    # 1. Definir y leer las opciones de la línea de comandos.
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--accion", choices=["resumen", "buscar"], default="resumen")
    parser.add_argument("--nombre", help="Nombre exacto para buscar")
    parser.add_argument("--archivo", type=Path,
                        default=Path(__file__).with_name("datos.csv"))
    args = parser.parse_args()
    if args.accion == "buscar" and not args.nombre:
        parser.error("La acción buscar necesita --nombre")

    # 2. Cargar la entrada y ejecutar la función que corresponda.
    try:
        objetos = cargar_objetos(args.archivo)
        if args.accion == "resumen":
            print("Referencias:", len(objetos))
            for categoria, unidades in unidades_por_categoria(objetos).items():
                print(categoria + ": " + str(unidades))
        elif args.accion == "buscar":
            encontrado = buscar_objeto(objetos, args.nombre)
            print(encontrado if encontrado is not None else "No encontrado")
    except (OSError, ValueError) as error:
        parser.exit(2, "Revisa la entrada: " + str(error) + "\n")


# Este bloque llama a main cuando ejecutamos el archivo, no cuando lo importamos.
if __name__ == "__main__":
    main()
