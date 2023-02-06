from ting_file_management.queue import Queue
import re


def exists_word(word: str, instance: Queue):
    """Aqui irá sua implementação"""
    size_instance = len(instance)
    result = list()

    for index in range(size_instance):
        file = instance.search(index)
        ocorrencias = list()

        index_line = 1
        for line in file["linhas_do_arquivo"]:
            # if re.search(word, line):
            if word.lower() in line.lower():
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


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


def fake_files():
    return [
        # {
        #     "nome_do_arquivo": "arquivo_2.txt",
        #     "qtd_linhas": 3,
        #     "linhas_do_arquivo": [...],
        # },
        # {
        #     "nome_do_arquivo": "arquivo_3.txt",
        #     "qtd_linhas": 4,
        #     "linhas_do_arquivo": [...],
        # },
    ]


if __name__ == "__main__":
    p = Queue()
    p.enqueue(
        {
            "nome_do_arquivo": "arquivo_1.txt",
            "qtd_linhas": 3,
            "linhas_do_arquivo": [
                "test a fraze 1",
                "para tentar",
                "fazer o test",
            ],
        }
    )

    r = exists_word("test", p)
    print(r)
