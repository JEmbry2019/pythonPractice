# imports the python random module 
import random

# User inputs a choice and it is assigned to the variable command.
command = input('Please enter Rock, Paper, Scissors, Quit to exit:')

# The while loop allows the code below it to run as long as the condition is true.
while command != "Quit":

# The random.choice function selects a string from the choices given and assigns it to the variable computerChoice.
  computerChoice = random.choice(["Rock", "Paper", "Scissor"])

 
# The command variable is converted to upper case, then checked for equality with the string 'ROCK','PAPER', SCISSORS 
# AND the variable computerChoice is checked for equility with the string 'SCISSORS', 'ROCK','PAPER'.
  if((command.upper() == "ROCK" and computerChoice == "Scissors")
    or (command.upper() == "PAPER" and computerChoice == "Rock")
    or (command.upper() == "SCISSORS" and computerChoice == "Paper")
    ):

# If one of the 1st, OR 2nd, OR 3rd condition is met, then the statement is printed.
    print ("Player choice " + command  + " and Computer Choice" + computerChoice + "player wins. ")

# If none of the above conditions are met then the varaible command.upper is checked for equility with computerChoice.
  elif (command.upper == computerChoice)
# If they are equal, then the statement is printed.  
    print ("It's a tie!")
# If they are not equal then the next statement is printed.    
  else:
    print("The computer wins!")

The next line stops the loop and prompts up to play again.
  command = input('Please enter Rock, Paper, Scissors, Quit to exit:')