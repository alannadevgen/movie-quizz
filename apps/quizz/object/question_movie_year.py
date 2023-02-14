from object.abstract_question import AbstractQuestion
from object.question_movie import QuestionMovie
import dao


class QuestionMovieYear(QuestionMovie, AbstractQuestion):
    def __init__(self) -> None:
        random_id = dao.get_random_id("movies", "movie_id")
        infos_movie = dao.get_info_movies_id(random_id)
        self.title = infos_movie['title']
        self.year = infos_movie['year']
        self.correct_letter = None
        self.incorrect_answers = []
        self.question_type = "movie year"

    def display_question(self):
        return f"When was the film {self.title} released?\n"

    def get_correct_answer(self):
        return self.year
    
    def get_incorrect_answers(self):
        '''
        Generate random answers for the question
        '''
        return dao.random_bad_answers_int(name_col="year", true_value=self.year)
