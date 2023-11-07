from helpers.response_finder import find_response
from helpers.training_model import init_train
from helpers.word_processor import process_text
from helpers.formatter_response import format_response

vectorizer, model = init_train()

while True:
  user_question = input("Envie uma mensagem: ")

  if user_question.lower() == 'sair':
    print("Desligando...")
    break

  response = find_response(process_text(user_question), vectorizer, model)
  format_response(response)