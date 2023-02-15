from unittest import TestCase
from object.question_movie_genre import QuestionMovieGenre


class TestQuestionMovieYear(TestCase):
    def test_question_movie_genre(self):
        # GIVEN
        question = QuestionMovieGenre()
        question.title='Blade Runner'
        question.year=1982
        question.genre='Fantasy'
        # WHEN
        result = question.display_question()
        correct_answer = question.get_correct_answer()
        # THEN
        self.assertIsInstance(question, QuestionMovieGenre)
        self.assertEqual(result, "What is the main genre of the film Blade Runner?\n")
        self.assertEqual(correct_answer, 'Fantasy')
        self.assertEqual(question.question_type, "movie genre")