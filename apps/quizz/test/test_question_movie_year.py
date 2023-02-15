from unittest import TestCase
from object.question_movie_year import QuestionMovieYear


class TestQuestionMovieYear(TestCase):
    def test_question_movie_year(self):
        # GIVEN
        question = QuestionMovieYear(
            random_id=10241
        )
        # WHEN
        result = question.display_question()
        correct_answer = question.get_correct_answer()
        # THEN
        self.assertIsInstance(question, QuestionMovieYear)
        self.assertEqual(result, "When was the film Dr. Jekyll and Mr. Hyde released?\n")
        self.assertEqual(correct_answer, 1932)
        self.assertEqual(question.question_type, "movie year")