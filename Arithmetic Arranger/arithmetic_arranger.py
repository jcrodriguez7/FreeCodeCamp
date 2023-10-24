def arithmetic_arranger(problems,showResult=False):
  line1 = ""
  line2 = ""
  line3 = ""
  line4 = ""
  #Check if there are more than 5 problems
  if len(problems) > 5: return "Error: Too many problems.";
    
  for problem in problems:
    problemItems = problem.split()

    #Check if operator is + or -
    if problemItems[1] not in ['+','-']: 
      return "Error: Operator must be '+' or '-'."
    #Check if numbers has more than 4 digits
    if len(problemItems[0]) > 4 or len(problemItems[2]) > 4: 
      return "Error: Numbers cannot be more than four digits."
    #Check if numbers has only digits
    if not problemItems[0].isdigit() or not problemItems[2].isdigit(): 
      return "Error: Numbers must only contain digits."
  
    if problemItems[1] == '+':
      resultNumber = int(problemItems[0]) + int(problemItems[2])
    else:
      resultNumber = int(problemItems[0]) - int(problemItems[2])

    maxDigits = 2 + max(len(problemItems[0]), len(problemItems[2]))

    #Create the line1
    for i in range(maxDigits-len(problemItems[0])):
      line1 += " "
    line1 += problemItems[0] + "    "

    #Create the line2
    line2 += problemItems[1]
    for i in range(maxDigits-len(problemItems[2])-1):
      line2 += " "
    line2 += problemItems[2] + "    "

    #Create the line3
    for i in range (maxDigits):
      line3 += "-"
    line3 += "    "

    
    #Create line4
    for i in range(maxDigits - len(str(resultNumber))):
      line4 += " "
    print(resultNumber)
    line4 += str(resultNumber)  
    line4 += "    "
    
  line1 = line1.rstrip()
  line2 = line2.rstrip()
  line3 = line3.rstrip()

  result = line1 + "\n" + line2 + "\n" + line3

  #If the call ask to show the result:
  if(showResult):
    line4 = line4.rstrip()
    result += "\n" + line4
  
  
  return result
      
    

