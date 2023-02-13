from object.abstract_question import AbstractQuestion
from object.question_movie import QuestionMovie


class QuestionMovieGenre(QuestionMovie, AbstractQuestion):
    def __init__(
            self,
            movie_id,
            title,
            year,
            genre,
            duration,
            avg_vote,
            critics_vote,
            public_vote,
            total_votes
        ) -> None:
        super().__init__(
            movie_id,
            title,
            year,
            genre,
            duration,
            avg_vote,
            critics_vote,
            public_vote,
            total_votes
        )
        self.question_type = "movie genre"

    def display_question(self):
        return f"What is the main genre of the film {self.title}?"

    def get_correct_answer(self):
        return self.genre
