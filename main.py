import spacy

nlp = spacy.load("en_core_web_sm")

def preprocess_question(text):
  doc = nlp(text)
  stopwords = spacy.lang.en.stop_words.STOP_WORDS
  processed_question = ' '.join([token.text for token in doc if token.text.lower() not in stopwords])
  return processed_question

def find_response(processed_question):
  question_to_response = {
    "want define domain simple switch": "(define: (domain switch)\n (:requirements :strips)\n\n (:predicates (switch_is_on)\n     (switch_is_off))\n\n  (:action switch_on\n  :precondition (switch_is_off)\n   :effect (and (switch_is_on))\n     (not (switch_is_off))\n)\n\n  (:action switch_off\n  :precondition (switch_is_on)\n :effect (and (switch_is_off))\n     (not (switch_is_on))\n)\n)\n",
    "implement domain simple switch": "(define: (domain switch)\n (:requirements :strips)\n\n (:predicates (switch_is_on)\n     (switch_is_off))\n\n  (:action switch_on\n  :precondition (switch_is_off)\n   :effect (and (switch_is_on))\n     (not (switch_is_off))\n)\n\n  (:action switch_off\n  :precondition (switch_is_on)\n :effect (and (switch_is_off))\n     (not (switch_is_on))\n)\n)\n",
  }
  return question_to_response.get(processed_question, "Sorry, I don't understand you question.\n")

def format_response(response):
  if(response.lower().find("Sorry")):
    print(response)
  else:
    print('Ok, here is your code.\n\n', str(response))

while True:
  user_question = input("Send a message: ")

  if user_question.lower() == 'exit':
    print("Shutting down")
    break

  response = find_response(preprocess_question(user_question))
  format_response(response)