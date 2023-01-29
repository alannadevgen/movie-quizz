from quizz.object.abstract_question import AbstractQuestion
from quizz.object.question_movie import QuestionMovie


class QuestionMovieYear(QuestionMovie, AbstractQuestion):
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
        self.question_type = "movie year"

    def display_question(self):
        return f"When did the film {self.title} come out?"

    def get_correct_answer(self):
        return self.year
