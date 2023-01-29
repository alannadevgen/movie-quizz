from abc import ABC, abstractmethod


class AbstractQuestion(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def display_question(self):
        pass
