from database.connect_db import return_all_nl_examples, return_pddl_example, close_connection

def get_training_data():
  nl_text_examples = []
  pddl_examples = []
  for element in return_all_nl_examples():
    nl_text_examples.append(element['nl_text'])
    pddl_examples.append(return_pddl_example(element['pddl_id']))

  close_connection()
  return nl_text_examples, pddl_examples