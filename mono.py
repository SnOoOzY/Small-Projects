import os 
from colorama import init
from colorama import Back

#display

def display_title():
    
    os.system('clear')

print("""
 ****     ****   *******   ****     **   *******  
/**/**   **/**  **/////** /**/**   /**  **/////** 
/**//** ** /** **     //**/**//**  /** **     //**
/** //***  /**/**      /**/** //** /**/**      /**
/**  //*   /**/**      /**/**  //**/**/**      /**
/**   /    /**//**     ** /**   //****//**     ** 
/**        /** //*******  /**    //*** //*******  
//         //   ///////   //      ///   ///////   """)
print("""
//////////////////////////////////////////////////""")


def user_choice():

  print("\n[1] Enter Chat")
  print("[2] Set Username")
  print("[3] Settings")
  print("[q] Quit")

  return input("> ")

def chat():
  print("Welcome to the chatroom! (Nothing worked on yet.)")
  input("> ")

def username():
  print("\nHere is your current username; \n")
  for new_username in usernames:
    print(new_username.title)
  
  new_username = input("Set your username: ")
  usernames.append(new_username)
  print("\nYour new username will be displayed as: %s!\n"% new_username.title) # Only printing the address of the objects value, fix.

def settings():
  print("\nHere are the list of settings: ")
  print("""\n
  [s1] Set background colour 
  [s2] Set text colour
  [qs] Quit settings""")

  return input("> ")

def backcol():
  print("\nTo change the colour of your console background, type bg (colour). The colours available are; red, blue, yellow, green, peach and default.")
  colin =  input("> ")
  newcol.append(colin)



# Functions

usernames = []

choice = ''

colin = []

newcol = []

display_title()

while choice != 'q':


  choice = user_choice()

  colchoice = colin()

  display_title()
  if choice == '1':
    chat()
  elif choice == '2':
    username()
  elif choice == '3':
    settings()
  elif colchoice() == 'bg red':
    print(Back.RED, "Background colour set to red.")
  elif colchoice() == 'bg blue':
    print(Back.BLUE, "Background colour set to blue.")
  elif colchoice() == 'bg yellow':
    print(Back.YELLOW, "Background colour set to yellow.")
  elif colchoice() == 'bg green':
    print(Back.GREEN, "Background colour set to green.")
  elif colchoice() == 'bg peach':
    print(Back.LIGHTRED_EX, "Background colour set to peach.")
  elif colchoice() == 'bg default':
    print(Back.BLACK, "Background colour set to default (black).")
  elif choice() == 's1':
    backcol()
  else:
    print("\n I don't understand that prompt, please try again.")