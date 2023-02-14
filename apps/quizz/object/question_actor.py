from object.abstract_question import AbstractQuestion
import random
import dao

class QuestionActor(AbstractQuestion):
    def __init__(self) -> None:
        random_id = dao.get_random_id("actors", "id")
        infos_actor = dao.get_movies_actor_id(random_id)
        actor_name = infos_actor['actor_name']
        title = random.sample(infos_actor['titles'], 1)[0]
        self.actor_name = actor_name
        self.title = title
        self.correct_letter = None
    
    def display_question(self):
        letters = ['A', 'B', 'C', 'D']
        
        question = f"In which movie did {self.actor_name} play ?\n"
        answers = dao.random_bad_answers("title", self.title)
        answers.append(self.title)
        random.shuffle(answers)

        index = answers.index(self.title)
        self.correct_letter = letters[index]

        complete_question = question + f"A {answers[0]}\nB {answers[1]}\nC {answers[2]}\nD {answers[3]}\n"
        
        return complete_question

    def get_correct_answer(self):
        return self.correct_letter