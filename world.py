
class GameNode:
  """Represents a position in the game world
  """

  def __init__(self, text=None, north=None, south=None, east=None, west=None):
    """
    Args:
      text: str - Text that is displayed to player upon entering position
      north: GameNode - Pointer to the position north
      south: GameNode - Pointer to the position south
      east: GameNode - Pointer to the position east
      west: GameNode - Pointer to the position west
    """
    self.text = text
    self.north = north
    self.south = south
    self.east = east
    self.west = west
