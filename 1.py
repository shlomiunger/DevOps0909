print("LEAP YEAR CHECKER.")

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not a leap year.")
  else:
    print("Leap year.")
else:
  print("Not a leap year.\n")
input("Now you might not be so impressed with this... wait till you see the behind-the-scenes\n")
