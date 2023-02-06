from ting_file_management.queue import Queue
from typing import List


def abs_search_word(word: str, instance: Queue, with_line=False):
    size_instance = len(instance)
    result = list()

    for index in range(size_instance):
        file = instance.search(index)
        ocorrencias = list()

        index_line = 1
        for line in file["linhas_do_arquivo"]:
            if word.lower() in line.lower():
                if with_line:
                    ocorrencias.append({"linha": index_line, "conteudo": line})
                else:
                    ocorrencias.append({"linha": index_line})

            index_line += 1

        if ocorrencias:
            result.append(
                {
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": ocorrencias,
                    "palavra": word,
                }
            )

    return result


def exists_word(word: str, instance: Queue):
    """Aqui irá sua implementação"""
    return abs_search_word(word, instance)


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    return abs_search_word(word, instance, with_line=True)
