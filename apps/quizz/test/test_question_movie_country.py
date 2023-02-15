from unittest import TestCase
from object.question_movie_country import QuestionMovieCountry


class TestQuestionMovieCountry(TestCase):
    def test_question_movie_country(self):
        # GIVEN
        question = QuestionMovieCountry(
            random_id=10241
        )
        # WHEN
        result = question.display_question()
        correct_answer = question.get_correct_answer()
        # THEN
        self.assertIsInstance(question, QuestionMovieCountry)
        self.assertEqual(result, "What is the country of origin of the film Dr. Jekyll and Mr. Hyde?\n")
        self.assertEqual(correct_answer, 'United States')
        self.assertEqual(question.question_type, "movie country")