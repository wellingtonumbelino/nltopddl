from word_processor import process_text

def find_response(processed_question):
  intentions = [
    "Eu quero um exemplo de domínio simples de um switch",
    "Implemente um exemplo simples de domínio de um switch",
    "Como implementar um exemplo de domínio simples de um switch",
    "Eu quero implementar um exemplo de domínio simples de um switch",
    "Defina um domínio simples de um switch"
  ]

  for intention in intentions:
    if (process_text(intention) in processed_question.lower()):
      return "(define: (domain switch)\n (:requirements :strips)\n\n (:predicates (switch_is_on)\n     (switch_is_off))\n\n  (:action switch_on\n  :precondition (switch_is_off)\n   :effect (and (switch_is_on))\n     (not (switch_is_off))\n)\n\n  (:action switch_off\n  :precondition (switch_is_on)\n :effect (and (switch_is_off))\n     (not (switch_is_on))\n)\n)\n"