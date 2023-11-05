import spacy
import re

nlp = spacy.load("pt_core_news_sm")

def process_text(text):
  doc = nlp(text)

  stopwords = spacy.lang.pt.stop_words.STOP_WORDS
  processed_question = [token.text for token in doc if token.text.lower() not in stopwords]

  # pattern = r'[^a-zA-Z0-9\s]'
  # processed_question = [re.sub(pattern, '', token) for token in processed_question]

  return ' '.join(processed_question)