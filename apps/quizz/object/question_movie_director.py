from object.abstract_question import AbstractQuestion
import dao


class QuestionMovieDirector(AbstractQuestion):
    def __init__(self) -> None:
        random_id = dao.get_random_id("movies", "movie_id")
        infos_movie = dao.get_info_movies_id(random_id)
        self.title = infos_movie['title']
        self.director = infos_movie['directors'][0]
        self.directors = infos_movie['directors']
        self.correct_letter = None
        self.incorrect_answers = []
        self.question_type = "movie director"

    def display_question(self):
        '''
            Returns the question as it should be displayed in the quizz.
        '''
        return f"Who directed the film {self.title}?\n"

    def get_correct_answer(self):
        '''
            Returns the correct answer.
        '''
        return self.director
    
    def get_incorrect_answers(self):
        '''
        Generate random answers for the question.
        '''
        return dao.random_bad_answers_directors(list_directors=self.directors)
