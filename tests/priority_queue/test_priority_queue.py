import pytest
from ting_file_management.priority_queue import PriorityQueue


@pytest.fixture
def fake_files():
    return [
        {
            "nome_do_arquivo": "arquivo_1.txt",
            "qtd_linhas": 5,
            "linhas_do_arquivo": [...],
        },
        {
            "nome_do_arquivo": "arquivo_2.txt",
            "qtd_linhas": 3,
            "linhas_do_arquivo": [...],
        },
        {
            "nome_do_arquivo": "arquivo_3.txt",
            "qtd_linhas": 4,
            "linhas_do_arquivo": [...],
        },
    ]


def test_basic_priority_queueing(fake_files):
    """Aqui irá sua implementação"""
    queue = PriorityQueue()
    for file in fake_files:
        queue.enqueue(file)

    assert queue.dequeue() == fake_files[1]
    assert queue.search(0) == fake_files[2]
    assert queue.search(1) == fake_files[0]

    with pytest.raises(IndexError):
        queue.search(2)
