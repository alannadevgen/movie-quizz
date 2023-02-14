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
    
    def display_question(self):
        return f"In which movie did {self.actor_name} play ?"

    def get_correct_answer(self):
        return self.title