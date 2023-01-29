from unittest import TestCase
from quizz.object.question_movie_year import QuestionMovieYear


class TestQuestionMovieYear(TestCase):
    def test_question_movie_year(self):
        # GIVEN
        question = QuestionMovieYear(
            movie_id=10623,
            title='Blade Runner',
            year=1982,
            genre='Fantasy',
            duration=124,
            avg_vote=8.9,
            critics_vote=9.02,
            public_vote=9.0,
            total_votes=843
        )
        # WHEN
        result = question.display_question()
        correct_answer = question.get_correct_answer()
        # THEN
        self.assertIsInstance(question, QuestionMovieYear)
        self.assertIsEqual(result, "When was Blade Runner released?")
        self.assertIsEqual(correct_answer, 1982)