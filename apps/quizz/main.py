from object.question_movie_genre import QuestionMovieGenre

nb_questions = input('How many questions do you want ? ')

nb_correct_answers = 0
for num_question in range(int(nb_questions)):
    print(f'\n----- Question {num_question+1} ------')
    question = QuestionMovieGenre()
    res_letter = input(question.display_full_question())

    correct_letter = question.get_correct_letter()
    answer = question.get_correct_answer()
    
    if res_letter.lower() != correct_letter.lower():
        print(f'False :(\nThe correct answer is {answer}\n')
    else:
        nb_correct_answers += 1
        print('Correct!\n')
print(f'You got {nb_correct_answers} correct anwsers!\n')