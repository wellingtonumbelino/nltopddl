import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

from word_processor import process_text

nl_texts = [
  "Eu quero implementar um domínio determinístico simples de um switch com predicados switch_is_off e switch_is_on e com ações switch_on e switch_off",
  "Implemente um domínio determinístico simples de um switch com predicados switch_is_off e switch_is_on e com ações switch_on e switch_off",
  "Como implementar um domínio determinístico simples de um switch com predicados switch_is_off e switch_is_on e com ações switch_on e switch_off"
]

example =  "(define: (domain switch)\n (:requirements :strips)\n\n (:predicates (switch_is_on)\n     (switch_is_off))\n\n  (:action switch_on\n  :precondition (switch_is_off)\n   :effect (and (switch_is_on))\n     (not (switch_is_off))\n)\n\n  (:action switch_off\n  :precondition (switch_is_on)\n :effect (and (switch_is_off))\n     (not (switch_is_on))\n)\n)\n"

pddl_example = [
  example,
  example,
  example
]

def init_train():
  nl_texts_processed = np.array([process_text(text) for text in nl_texts])

  tfidf_vectorizer = TfidfVectorizer()
  X = tfidf_vectorizer.fit_transform(nl_texts_processed)
  X_train, X_test, y_train, y_test = train_test_split(X, pddl_example, test_size=0.2, random_state=42)

  model = MultinomialNB()
  model.fit(X_train, y_train)

  return tfidf_vectorizer, model

  # predicts = model.predict(X_test)
  # accuracy = accuracy_score(y_test, predicts)
  # report = classification_report(y_test, predicts)