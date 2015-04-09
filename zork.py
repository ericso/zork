import sys
import os

import nltk
# nltk.download('all')

from clint.arguments import Args
from clint.textui import prompt, puts, colored


def _yield_input_tokens(user_input):
  """Splits the user input string on spaces and returns a generator for the tokens
  """
  tokens = user_input.split(' ')
  for token in tokens:
    yield token


if __name__ == '__main__':
  # name = prompt.query("What is your name?")
  # puts(colored.blue("Hi {0}.".format(name)))

  movement_set = set([
    'move',
    'walk',
  ])
  looking_set = set([
    'look',
    'gaze',
    'examine',
  ])
  direction_set = set([
    'north',
    'south',
    'east',
    'west',
  ])


  while True:
    user_input = prompt.query(">")
    input_gen = _yield_input_tokens(user_input)

    action = None
    while not action:
      try:
        token = next(input_gen)
      except:
        print("End of input")
        break

      if token in movement_set or token in looking_set:
        action = token

    direction = None
    while not direction:
      try:
        token = next(input_gen)
      except:
        print("End of input")
        break

      if token in direction_set:
        direction = token

    if action and direction:
      print(action)
      print(direction)
