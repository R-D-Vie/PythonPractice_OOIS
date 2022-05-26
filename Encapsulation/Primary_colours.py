class PrimaryColor:
  """Primary colors are red, blue, and yellow"""
  def __init__(self):
    self._color = "red"

  @property
  def color(self):
    """Getter that returns the _color instance variable"""
    return self._color

  @color.setter
  def color(self, new_color):
    primary_colors = ["red", "blue", "yellow"]
    if new_color not in primary_colors:
        raise ValueError("New color must be a primary color")
    self._color = new_color
    