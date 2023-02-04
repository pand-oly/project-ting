from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file: str, instance: Queue):
    """Aqui irá sua implementação"""
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return None

    importer = txt_importer(path_file)
    result_file_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(importer),
        "linhas_do_arquivo": importer,
    }

    instance.enqueue(result_file_dict)
    return sys.stdout.write(str(result_file_dict))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
