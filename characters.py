
class Player:
  """Represents a player character in the game world
  """

  def __init__(self, name, curr_pos=None):
    """
    Args:
      text: str - The name of the player
      curr_pos: GameNode - Pointer to the player's current position
    """
    self.name = name
    self.curr_pos = curr_pos

  def move(self, direction):
    """Moves a player in the direction indicated

    Args:
      direction: str - The direction the player will move to
    """
    # TODO(eric) figure out some sort of event system

    if self.curr_pos == None:
      print("Player is off the map!")
    elif getattr(self.curr_pos, direction) == None:
      print("Invalid direction")
    else:
      if direction == 'north':
        self.curr_pos = self.curr_pos.north
      elif direction == 'south':
        self.curr_pos = self.curr_pos.south
      elif direction == 'east':
        self.curr_pos = self.curr_pos.east
      elif direction == 'west':
        self.curr_pos = self.curr_pos.west
