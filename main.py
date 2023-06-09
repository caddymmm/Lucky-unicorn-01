show_instructions = ""
while show_instructions.lower() != "xxx":
  # Ask the user if they have played before
  show_instructions = input("Have you played this game before? ").lower ()
  # If they say yes, output 'program continues'
  if show_instructions == "yes":
    show_instructions = "yes"
    print ("program continuses")
  if show_instructions == "y":
    show_instructions = "yes"
    print ("program continuses")
  # If they say no, output 'display instructions'
  elif show_instructions == "no":
    show_instructions = "no"
    print ("Display instructions")
  elif show_instructions == "n":
    show_instructions = "no"
    print ("Display instructions")
  # If they say no, output 'display instructions'
  else: print ("please answer yes / no")