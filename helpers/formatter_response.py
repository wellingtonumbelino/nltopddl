def format_response(response):
  if response is None:
    print("Desculpe, eu não entendi a sua pergunta.\n")
  elif "Huuum" in response:
    print('\n', response, '\n')
  else:
    print('\nOk, aqui está o seu código.\n\n', str(response), '\n')