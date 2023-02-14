from abc import ABC, abstractmethod
import random


class AbstractQuestion(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def display_question(self):
        pass

    @abstractmethod
    def get_correct_answer(self):
        pass

    def get_correct_letter(self):
        return self.correct_letter

    @abstractmethod
    def get_incorrect_answers(self):
        pass

    def get_all_answers(self):
        answers = self.get_incorrect_answers()
        answers.append(self.get_correct_answer())
        random.shuffle(answers)
        return answers

    def display_full_question(self):
        letters = ['A', 'B', 'C', 'D']
        question = self.display_question()
        answers = self.get_all_answers()
        print(answers)

        index = answers.index(self.get_correct_answer())
        self.correct_letter = letters[index]

        return question + f"\nA {answers[0]}\nB {answers[1]}\nC {answers[2]}\nD {answers[3]}\n"
