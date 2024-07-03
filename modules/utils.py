import os
import sys

def get_resource_path(relative_path):
    """ Obtém o caminho absoluto para o recurso, trabalha para dev e executável PyInstaller """
    try:
        # PyInstaller cria um diretório temporário e armazena o caminho em _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

