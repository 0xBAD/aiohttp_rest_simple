from queue import Queue


class Task(Queue):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Task()
        return cls.__instance
