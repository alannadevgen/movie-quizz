from object.abstract_question import AbstractQuestion


class QuestionMovie(AbstractQuestion):
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
        super().__init__()
        self.movie_id = movie_id
        self.title = title
        self.year = year
        self.genre = genre
        self.duration = duration
        self.avg_vote = avg_vote
        self.critics_vote = critics_vote
        self.public_vote = public_vote,
        self.total_votes = total_votes

    def display_question(self):
        pass

    def get_correct_answer(self):
        pass