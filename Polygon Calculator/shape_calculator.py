class Rectangle:
  def __init__(self,width,height) -> None:
    self.width = width
    self.height = height

  def __str__(self) -> str:
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self,width):
    self.width = width

  def set_height(self,height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.height > 50 or self.width > 50: return "Too big for picture."

    result = ""
    for row in range(self.height):
      result += "*" * self.width + "\n"

    return result

  def get_amount_inside(self,shape):
    if self.width < shape.width or self.height < shape.height: return 0
    xAxis = self.width // shape.width
    yAxis = self.height // shape.height
    return xAxis * yAxis
  



class Square(Rectangle):

  def __init__(self, side) -> None:
    super().__init__(side,side)
    self.side = side

  def __str__(self) -> str:
    return f"Square(side={self.side})"

  def set_height(self, height):
    super().set_height(height)
    super().set_width(height)
    self.side=height

  def set_width(self, width):
    super().set_height(width)
    super().set_width(width)
    self.side = width

  def set_side(self,side):
    self.side = side
    self.set_height(side)
    self.set_width(side)
