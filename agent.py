from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import SVC

from word_processor import process_text

example_domain = "(define: (domain switch)\n (:requirements :strips)\n\n (:predicates (switch_is_on)\n     (switch_is_off))\n\n  (:action switch_on\n  :precondition (switch_is_off)\n   :effect (and (switch_is_on))\n     (not (switch_is_off))\n)\n\n  (:action switch_off\n  :precondition (switch_is_on)\n :effect (and (switch_is_off))\n     (not (switch_is_on))\n)\n)\n"

training_data = {
  "Eu quero um exemplo de domínio simples de um switch": example_domain,
  "Implemente um exemplo simples de domínio de um switch": example_domain,
  "Como implementar um exemplo de domínio simples de um switch": example_domain,
  "Eu quero implementar um exemplo de domínio simples de um switch": example_domain,
  "Defina um domínio simples de um switch": example_domain
}

questions, intents = zip(*training_data.items())
questions = [process_text(question) for question in questions]

vectorizer = TfidfTransformer()
questions_tfidf = vectorizer.fit_transform(questions)

model = SVC(kernel='linear', C=1, probability=True)
model.fit(questions_tfidf, intents)

class Agent:
  def returnModel():
    print(questions)