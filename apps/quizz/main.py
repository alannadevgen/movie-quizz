from object.question_factory import QuestionFactory


nb_questions = input('How many questions do you want ? ')

nb_correct_answers = 0
for num_question in range(int(nb_questions)):
    print(f'\n---------- Question {num_question+1} -----------')
    question_factory = QuestionFactory()
    question = question_factory.instanciate_question()
    res_letter = input(question.display_full_question())

    correct_letter = question.get_correct_letter()
    answer = question.get_correct_answer()
    
    if res_letter.lower() != correct_letter.lower():
        print(f'False :(\nThe correct answer is {answer}\n')
    else:
        nb_correct_answers += 1
        print('Correct!\n')
print(f'You got {nb_correct_answers} correct anwser(s)!\n')