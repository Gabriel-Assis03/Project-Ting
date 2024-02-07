import sys
import os


def txt_importer(path_file):
    if not os.path.exists(path_file):
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        return None

    if not path_file.endswith('.txt'):
        sys.stderr.write("Formato inválido\n")
        return None

    with open(path_file, 'r') as file:
        lines = file.read().split('\n')

    return lines
