hour = int(input("What hour of the day is it? (use military time)"))
if hour >= 7:
  print("Good morning!")
elif hour >= 12: 
  print("Good afternoon")
else:
  print("Good Night!")
