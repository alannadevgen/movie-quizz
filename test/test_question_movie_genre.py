from unittest import TestCase
from quizz.object.question_movie_genre import QuestionMovieGenre


class TestQuestionMovieYear(TestCase):
    def test_question_movie_genre(self):
        # GIVEN
        question = QuestionMovieGenre(
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
        self.assertIsInstance(question, QuestionMovieGenre)
        self.assertEqual(result, "What is the main genre of the film Blade Runner?")
        self.assertEqual(correct_answer, 'Fantasy')
        self.assertEqual(question.question_type, "movie genre")