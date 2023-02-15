from unittest import TestCase
from object.question_actor import QuestionActor


class TestQuestionMovieCountry(TestCase):
    def test_question_movie_actor(self):
        # GIVEN
        question = QuestionActor(
            random_id=3057
        )
        # WHEN
        result = question.display_question()
        correct_answer = question.get_correct_answer()
        # THEN
        self.assertIsInstance(question, QuestionActor)
        self.assertEqual(result, "In which movie did Maureen O'Hara play?\n")
        self.assertEqual(correct_answer, 'Miracle on 34th Street')
        self.assertEqual(question.question_type, "actor")