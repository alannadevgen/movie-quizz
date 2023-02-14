from object.question_actor import QuestionActor

nb_questions = input('How many questions do you want ?')

for _ in range(int(nb_questions)):
    question_actor = QuestionActor()
    res_letter = input(question_actor.display_question())

    answer = question_actor.get_correct_answer()

    if res_letter.lower() != answer.lower():
        print(f'False :(\n The correct answer is {answer}')
    else:
        print('Correct !')