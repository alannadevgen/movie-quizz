from object.abstract_question import AbstractQuestion
import random
import dao

class QuestionActor(AbstractQuestion):
    def __init__(self) -> None:
        random_id = dao.get_random_id("actors", "actor_id")
        infos_actor = dao.get_movies_actor_id(random_id)
        self.actor_name = infos_actor['actor_name']
        self.title = random.sample(infos_actor['titles'], 1)[0]
        self.correct_letter = None
        self.incorrect_answers = []
        self.question_type = "actor"
    
    def display_question(self):
        return f"In which movie did {self.actor_name} play ?\n"

    def get_correct_answer(self):
        return self.title

    def get_incorrect_answers(self):
        '''
        Generate random answers for the question
        '''
        return dao.random_bad_answers(name_col="title", true_value=self.title)
