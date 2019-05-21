answer_question = {
    'Как дела?' : 'Было терпимо, потом ты написал', 
    'Что делаешь?' : 'Отвечаю на бестолковые вопросы', 
    'Какие планы?' :'Побыстрее это закончить'
    }

def ask_user():
    while True:
        user_say = input('Задайте вопрос  ')
        if user_say in answer_question:
            print(answer_question.get(user_say))
        else:
            print('Я не знаю ответа на этот вопрос')
            print(ask_user())

ask_user() 