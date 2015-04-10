import sys
import os

import nltk
# nltk.download('all')

from clint.arguments import Args
from clint.textui import prompt, puts, colored

from world import GameNode
from characters import Player


GAME_ROOT_NODE = None
GAME_PLAYER = None


def _build_game_world():
  """Creates random GameNodes and connects them
  """
  new_node = GameNode(text="You awake in a field. It's dark out...")
  new_node.north = GameNode(text="Walking north, you see a forest in distance.")
  new_node.south = GameNode(text="You head south. There is a large wall blocking your path. The wall runs for miles in either direction. It is high and there's no obvious way to climb over it.")
  new_node.east = GameNode(text="You come upon a house. It's an eerie house.")
  new_node.west = GameNode(text="You reach a wide gushing river. The water is freezing.")

  return new_node

def _create_player(name, curr_pos):
  """Generates a Player object for the user to move around
  """
  return Player(name=name, curr_pos=curr_pos)


def _yield_input_tokens(user_input):
  """Splits the user input string on spaces and returns a generator for the tokens
  """
  tokens = user_input.split(' ')
  for token in tokens:
    yield token

def _get_user_action():
  """Prompt user for text input, returns parsed action and direction

  Returns: tuple of <action>, <direction>
  <action> is either 'move' or 'look'
  <direction> is one of the compass directions (north, south, east, west)
  """
  user_input = prompt.query(">")
  input_gen = _yield_input_tokens(user_input)

  action = None
  while not action:
    try:
      token = next(input_gen)
    except:
      print("End of input")
      break

    if token in movement_set:
      action = 'move'
    elif token in looking_set:
      action = 'look'

  direction = None
  while not direction:
    try:
      token = next(input_gen)
    except:
      print("End of input")
      break

    if token in direction_set:
      direction = token

  return (action, direction)

if __name__ == '__main__':
  # name = prompt.query("What is your name?")
  # puts(colored.blue("Hi {0}.".format(name)))

  movement_set = set([
    'move',
    'walk',
    'go',
    'proceed',
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

  # Create the game world
  GAME_ROOT_NODE = _build_game_world()

  # Create the game player
  GAME_PLAYER = _create_player(name="Unnamed", curr_pos=GAME_ROOT_NODE)

  # Game start
  print(GAME_PLAYER.curr_pos.text)

  # Main game loop
  while True:
    action, direction = _get_user_action()
    print(action, direction)

    if action == 'move' and direction in direction_set:
      GAME_PLAYER.move(direction)

      print(GAME_PLAYER.curr_pos)
      print(GAME_PLAYER.curr_pos.text)

