from helpers.response_finder import find_response
from helpers.training_model import init_train
from helpers.word_processor import process_text

vectorizer, model = init_train()

def format_response(response):
  if response is None:
    print("Desculpe, eu não entendi a sua pergunta.\n")
  else:
    print('\nOk, aqui está o seu código.\n\n', str(response))

while True:
  user_question = input("Envie uma mensagem: ")

  if user_question.lower() == 'sair':
    print("Desligando...")
    break

  response = find_response(process_text(user_question), vectorizer, model)
  format_response(response)