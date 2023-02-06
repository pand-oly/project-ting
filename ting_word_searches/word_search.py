from ting_file_management.queue import Queue


def search_exist_word(lines, word, occurrences, with_line):
    index_line = 1
    for line in lines:
        if word.lower() in line.lower():
            if with_line:
                occurrences.append({"linha": index_line, "conteudo": line})
            else:
                occurrences.append({"linha": index_line})

        index_line += 1


def abs_search_word(word: str, instance: Queue, with_line=False):
    size_instance = len(instance)
    result = list()

    for index in range(size_instance):
        file = instance.search(index)
        ocorrencias = list()

        lines = file["linhas_do_arquivo"]

        search_exist_word(lines, word, ocorrencias, with_line)

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
