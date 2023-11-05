def find_response(processed_question):
  intentions = [
    "want simple domain example switch",
    "implement simple switch domain example",
    "implement simple domain example switch",
    "want implement simple domain example switch",
    "define simple domain switch"
  ]

  for intention in intentions:
    if (intention in processed_question.lower()):
      return "(define: (domain switch)\n (:requirements :strips)\n\n (:predicates (switch_is_on)\n     (switch_is_off))\n\n  (:action switch_on\n  :precondition (switch_is_off)\n   :effect (and (switch_is_on))\n     (not (switch_is_off))\n)\n\n  (:action switch_off\n  :precondition (switch_is_on)\n :effect (and (switch_is_off))\n     (not (switch_is_on))\n)\n)\n"