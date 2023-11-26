import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

from controllers.data_controller import get_training_data
from helpers.word_processor import process_text

nl_texts, pddl_example = get_training_data()

def init_train():
  nl_texts_processed = np.array([process_text(text) for text in nl_texts])

  tfidf_vectorizer = TfidfVectorizer()
  X = tfidf_vectorizer.fit_transform(nl_texts_processed)
  X_train, X_test, y_train, y_test = train_test_split(X, pddl_example, test_size=0.2, random_state=42)

  model = MultinomialNB()
  model.fit(X_train, y_train)

  predicts = model.predict(X_test)
  accuracy = accuracy_score(y_test, predicts)
  report = classification_report(y_test, predicts)

  print(f"Acurácia: {accuracy}")
  print(f"Classificação Report: {report}")

  return tfidf_vectorizer, model