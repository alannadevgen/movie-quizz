from unittest import TestCase
from object.question_movie_genre import QuestionMovieGenre


class TestQuestionMovieGenre(TestCase):
    def test_question_movie_genre(self):
        # GIVEN
        question = QuestionMovieGenre(
            random_id=10241
        )
        # WHEN
        result = question.display_question()
        correct_answer = question.get_correct_answer()
        # THEN
        self.assertIsInstance(question, QuestionMovieGenre)
        self.assertEqual(result, "What is the main genre of the film Dr. Jekyll and Mr. Hyde?\n")
        self.assertEqual(correct_answer, 'Horror')
        self.assertEqual(question.question_type, "movie genre")