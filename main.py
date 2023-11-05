from response_finder import find_response
from word_processor import process_text

def format_response(response):
  if response is None:
    print("Sorry, I don't understand your question.\n")
  else:
    print('\nOk, here is your code.\n\n', str(response))

while True:
  user_question = input("Send a message: ")

  if user_question.lower() == 'exit':
    print("Shutting down")
    break

  response = find_response(process_text(user_question))
  format_response(response)