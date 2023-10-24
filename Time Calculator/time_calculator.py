def add_time(start, duration, startingDay = ""):

  
    
  hourTime = start.split()
  startHour = int(hourTime[0].split(":")[0])
  startMin = int(hourTime[0].split(":")[1])
  PM = hourTime[1] == "PM"

  if PM : startHour += 12
  PM = False
  

  splittedDuration = duration.split(":")
  
  durHour = int(splittedDuration[0])
  durMinutes = int(splittedDuration[1])
  
  finalMinute = (durMinutes+startMin) % 60
  hoursAdded = (durMinutes+startMin) // 60

  finalHour = (durHour+startHour+hoursAdded) % 24
  addedDays = (durHour+startHour+hoursAdded) // 24

  

  if finalMinute < 10 : finalMinute = "0" + str(finalMinute)

  if finalHour >= 12:
    PM = True
    
  if finalHour > 12: 
    finalHour -= 12

  if not PM and finalHour == 0: finalHour=12
  

  if PM: new_time = str(finalHour) + ":" + str(finalMinute) + " PM"
  else: new_time = str(finalHour) + ":" + str(finalMinute) + " AM" 

  if startingDay != "":
    weekDay = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" , "Sunday"]
    newWeekDay = weekDay[(weekDay.index(startingDay.capitalize()) + addedDays) % 7]

    new_time +=   ", " + newWeekDay


  if addedDays == 1 : new_time += " (next day)"
  elif addedDays >1 :  new_time += " ({n} days later)".format(n=addedDays)
  
  return new_time