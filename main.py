import os, time



cont = "y"
while cont == "y":
  print("🌟HIGH SCORE TABLE🌟")
  print()
  init = input("INITIALS: ")
  score = input("SCORE: ")
  print()
  cont = input("y/n ")
  print() 
  print("ADDED")
  
  f = open("high.score", "a")
  f.write(f"{init} {score}\n")
  f.close()
  
  
  time.sleep(1)
  os.system("clear")