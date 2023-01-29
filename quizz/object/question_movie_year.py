from quizz.object.abstract_question import AbstractQuestion
from quizz.object.question_movie import QuestionMovie


class QuestionMovieYear(QuestionMovie, AbstractQuestion):
    def __init__(
            self,
            movie_id,
            title
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
