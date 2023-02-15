from object.abstract_question import AbstractQuestion
import dao


class QuestionMovieCountry(AbstractQuestion):
    def __init__(self, random_id = None) -> None:
        if random_id is None:
            random_id = dao.get_random_id("movies", "movie_id")
        infos_movie = dao.get_info_movies_id(random_id)
        self.title = infos_movie['title']
        self.country = infos_movie['countries'][0]
        self.countries = infos_movie['countries']
        self.correct_letter = None
        self.incorrect_answers = []
        self.question_type = "movie country"

    def display_question(self):
        '''
            Returns the question as it should be displayed in the quizz.
        '''
        return f"What is the country of origin of the film {self.title}?\n"

    def get_correct_answer(self):
        '''
            Returns the correct answer.
        '''
        return self.country
    
    def get_incorrect_answers(self):
        '''
        Generate random answers for the question.
        '''
        return dao.random_bad_answers_countries(list_countries=self.countries)
