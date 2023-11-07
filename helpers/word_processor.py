import spacy

from unidecode import unidecode

nlp = spacy.load("pt_core_news_sm")

def process_text(text):
  doc = nlp(text)

  process_tokens = ' '.join([unidecode(token.lemma_) for token in doc if not token.is_space and not token.is_punct and not token.is_stop]).lower()
  
  return process_tokens