from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.queue = list()
        self.__length = 0

    def __len__(self):
        """Aqui irá sua implementação"""
        return self.__length

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.queue.append(value)
        self.__length += 1
        return 0

    def dequeue(self):
        """Aqui irá sua implementação"""
        if self.__length == 0:
            return None

        item_deleted = self.queue.pop(0)
        self.__length -= 1

        return item_deleted

    def search(self, index):
        """Aqui irá sua implementação"""
        if 0 > index or index >= self.__length:
            raise IndexError

        return self.queue.__getitem__(index)
