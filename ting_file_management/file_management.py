import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if path_file.endswith(".txt"):
        try:
            with open(path_file, "r", newline="\n") as file:
                lines = file.read().split("\n")
                return lines
        except FileNotFoundError:
            return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

    return sys.stderr.write("Formato inválido")
