GAME_ROOT_NODE = None
GAME_PLAYER = None

MOVEMENT_SET = set([
  'move',
  'walk',
  'go',
  'proceed',
])

LOOKING_SET = set([
  'look',
  'gaze',
  'examine',
])

DIRECTION_SET = set([
  'north',
  'south',
  'east',
  'west',
])

DIRECTION_OPPOSITES = {
  'north': 'south',
  'south': 'north',
  'east': 'west',
  'west': 'east',
}
