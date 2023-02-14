from object.question_actor import QuestionActor
from object.question_movie_genre import QuestionMovieGenre
from object.question_movie_year import QuestionMovieYear
import random


class QuestionFactory():
    @staticmethod
    def instanciate_question():
        all_types = ["actor", "movie genre", "movie year"]
        question_type = random.choice(all_types)

        if question_type == "actor":
            question = QuestionActor()
        elif question_type == "movie genre":
            question = QuestionMovieGenre()
        elif question_type == "movie year":
            question = QuestionMovieYear()
        
        return question