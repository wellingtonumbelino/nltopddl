import numpy as np

def find_response(text, vectorizer, model):
  np_text = np.array([text])
  vec_text = vectorizer.transform(np_text)
  predict_pddl = model.predict(vec_text)

  return predict_pddl[0]