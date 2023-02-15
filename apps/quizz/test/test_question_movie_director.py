from unittest import TestCase
from object.question_movie_director import QuestionMovieDirector


class TestQuestionMovieDirector(TestCase):
    def test_question_movie_director(self):
        # GIVEN
        question = QuestionMovieDirector(
            random_id=10241
        )
        # WHEN
        result = question.display_question()
        correct_answer = question.get_correct_answer()
        # THEN
        self.assertIsInstance(question, QuestionMovieDirector)
        self.assertEqual(result, "Who directed the film Dr. Jekyll and Mr. Hyde?\n")
        self.assertEqual(correct_answer, 'Rouben Mamoulian')
        self.assertEqual(question.question_type, "movie director")