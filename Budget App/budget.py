class Category:

  def __init__(self, categoryName) -> None:
    self.categoryName=categoryName
    self.ledger = []
    self.currentBalance = 0

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
    self.currentBalance += amount
        
  def withdraw(self, amount, description=""):
    if self.check_funds(amount) : 
      self.ledger.append({"amount": -amount, "description": description})
      self.currentBalance -= amount
      return True
    return False
    
  def get_balance(self):
    return self.currentBalance

  def transfer(self,amount,destination):
    if self.check_funds(amount):
      self.withdraw(amount,"Transfer to "+destination.categoryName)
      destination.deposit(amount,"Transfer from "+self.categoryName)
      return True
    return False
    

  def check_funds(self,amount):
    
    return amount <= self.currentBalance

  def __str__(self):
    result = ""
    #Adding first line, with Category Name centered in '*'
    numberOfAst = (30 - len(self.categoryName)) // 2
    result += "*" * numberOfAst + self.categoryName + "*" * (30-numberOfAst-len(self.categoryName)) + "\n"

    #Adding ledger items line by line
    for line in self.ledger:
      formattedDesc = line["description"]
      if len(formattedDesc) > 23 :
        formattedDesc = formattedDesc[:23]
      else: formattedDesc += " " * (23 - len(formattedDesc))

      
      formattedAmount = str(format(line["amount"], ".2f"))
      
      result += formattedDesc + " " *(7-len(formattedAmount)) + formattedAmount + "\n"
      
    result += "Total: " + str(self.currentBalance)
    
    return result





def create_spend_chart(categories):

  result = "Percentage spent by category\n"
  maxWidth = 4 + 4 + (len(categories)-1)*3
  
  withdrawByCat = {}
  totalMoved = 0
  for category in categories:
    categoryWithdraw = 0
    for movement in category.ledger:
      if movement["amount"] < 0: categoryWithdraw += movement["amount"]

    withdrawByCat[category.categoryName] = abs(categoryWithdraw)
    
    totalMoved += abs(categoryWithdraw)

 
  for category in withdrawByCat.keys():
    withdrawByCat[category] = ((withdrawByCat[category]/totalMoved*100) // 10) *10

  ejeX = 100
  
  #Drawing axis with values
  while(ejeX>=0):
    line = " " * (3-len(str(ejeX))) + str(ejeX) + "| "
    for cat in withdrawByCat.keys():
      if withdrawByCat[cat] >= ejeX:
        line += "o  "
      else: line += "   "
    result += line + "\n"
    ejeX -= 10  

  #Drawing lines under axis  
  line = "    " + "-" * (maxWidth - 4)
  result += line + "\n"

   #Drawing leyend
  categoryNames = []
  maxDepth = 0
  for c in categories:
    categoryNames.append(c.categoryName)
    maxDepth = max(maxDepth,len(c.categoryName))

  
  index = 0
  for row in range(maxDepth):
    line = "     "
    for c in categoryNames:
      if row < len(c):
        line += c[row] + "  "
      else: line += "   "

    
    result += line 
    if row +1 < maxDepth : result += "\n"
 

  return result