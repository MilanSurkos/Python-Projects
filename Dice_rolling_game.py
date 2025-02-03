import random 

while True:
  choice = input('Roll the dice? (y/n): ').lower()    
  if choice == 'y':
      die1 = random.randint(1, 6)
      die2 = random.randint(1, 6)
      print(f'({die1}, {die2})')
  elif choice == 'n':
      print('Thanks for playing!')
      break
  else:
      print('Invalid choice!')

"""
Ask: roll the dice ? 
If user enters y
  Generate 2 random numbers
  Print them
If users enters n
  Print thank you message
  Terminate
Else
  Print invalid choice

"""