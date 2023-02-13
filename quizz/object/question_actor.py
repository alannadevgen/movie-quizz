from quizz.object.abstract_question import AbstractQuestion


class QuestionActor(AbstractQuestion):
    def __init__(self, actor_id) -> None:
        super().__init__()
    
    def display_question(self):
        return super().display_question()

    def get_correct_answer(self):
        return super().get_correct_answer()