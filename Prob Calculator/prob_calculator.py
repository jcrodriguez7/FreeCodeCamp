import copy
import random

class Hat:
  def __init__(self,**kwargs) -> None:
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, n):
    result = []
    if n > len(self.contents): return self.contents
    for i in range(n):  
      ball = random.choice(self.contents)
      self.contents.remove(ball)
      result.append(ball)
    
    return result


def check(expected_balls,extracted_balls):
  for key, value in expected_balls.items():
    if value > extracted_balls.count(key):
      return False
  return True
  

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  numOfSuccess = 0
  print(hat.contents)
  for i in range(num_experiments):
    newHat = copy.deepcopy(hat)
    extracted_balls = newHat.draw(num_balls_drawn)
    if check(expected_balls,extracted_balls) : numOfSuccess += 1
    
  return numOfSuccess / num_experiments
    
