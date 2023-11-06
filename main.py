from response_finder import find_response
from training_model import init_train
from word_processor import process_text

def format_response(response):
  if response is None:
    print("Desculpe, eu não entendi a sua pergunta.\n")
  else:
    print('\nOk, aqui está o seu código.\n\n', str(response))

vectorizer, model = init_train()

while True:
  user_question = input("Envie uma mensagem: ")
  # user_question = "Eu quero implementar um domínio determinístico simples de um switch com predicados switch_is_off e switch_is_on e com ações switch_on e switch_off"

  if user_question.lower() == 'sair':
    print("Desligando...")
    break

  find_response(process_text(user_question), vectorizer, model)