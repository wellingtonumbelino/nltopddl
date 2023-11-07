def format_response(response):
  if response is None:
    print("Desculpe, eu não entendi a sua pergunta.\n")
  else:
    print('\nOk, aqui está o seu código.\n\n', str(response))