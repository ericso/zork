import sys
import os

import nltk
# nltk.download('all')

from clint.arguments import Args
from clint.textui import prompt, puts, colored

from world import GameNode
from characters import Player
from const import (
  GAME_ROOT_NODE,
  GAME_PLAYER,
  MOVEMENT_SET,
  LOOKING_SET,
  DIRECTION_SET,
  DIRECTION_OPPOSITES,
)


def _build_game_world():
  """Creates random GameNodes and connects them
  """
  new_node = GameNode(text="You awake in a field. It's dark out...")

  _connect_game_node(new_node, GameNode(text="Walking north, you see a forest in distance."), 'north')
  _connect_game_node(new_node, GameNode(text="You head south. There is a large wall blocking your path. The wall runs for miles in either direction. It is high and there's no obvious way to climb over it."), 'south')
  _connect_game_node(new_node, GameNode(text="You come upon a house. It's an eerie house."), 'east')
  _connect_game_node(new_node, GameNode(text="You reach a wide gushing river. The water is freezing."), 'west')

  return new_node

def _connect_game_node(node1, node2, direction):
  """Adds node2 to node1.direction

  Args:
    node1: GameNode - source node
    node2: GameNode - destination node
    direction: str - the direction (north, south, east, west) from node1 to node2
  """
  if getattr(node1, direction) == None:
    setattr(node1, direction, node2)
    setattr(node2, DIRECTION_OPPOSITES[direction], node1)
  else:
    print("%s node already has a connection in the %s direction" % (node1, direction))


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
    except StopIteration as err:
      print(err)
      break

    if token in MOVEMENT_SET:
      action = 'move'
    elif token in LOOKING_SET:
      action = 'look'

  direction = None
  while not direction:
    try:
      token = next(input_gen)
    except:
      print("End of input")
      break

    if token in DIRECTION_SET:
      direction = token

  return (action, direction)

if __name__ == '__main__':
  # name = prompt.query("What is your name?")
  # puts(colored.blue("Hi {0}.".format(name)))

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

    if action == 'move' and direction in DIRECTION_SET:
      GAME_PLAYER.move(direction)

      print(GAME_PLAYER.curr_pos)
      print(GAME_PLAYER.curr_pos.text)

