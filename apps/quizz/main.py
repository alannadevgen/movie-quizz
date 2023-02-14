from object.question_actor import QuestionActor

nb_questions = input('How many questions do you want ?')

for _ in range(int(nb_questions)):
    question_actor = QuestionActor()
    res = input(question_actor.display_question())

    answer = question_actor.get_correct_answer()

    if res.lower() !=  answer.lower():
        print(answer)
    else:
        print('Correct !')