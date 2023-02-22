from random import randint
from time import sleep
options= ('rock', 'paper', 'scissors')
machine = randint(0, 2)

print('''choose one of the options:
[0] Rock
[1] Paper
[2] Scissors''')
player = int(input('whats your move?  '))
print('JO...')
sleep(1) 
print('CKEN...')
sleep(1)
print('PO!!!')
print('-=' * 12)
print('The machine chose {}'.format(options[machine]))
print('Player chose {}'.format(options[player]))
print ('-=' * 12)

if machine == 0: #machine use rock
   if player == 0:
      print('A TIE')
   elif player == 1:
        print('You win')
   elif player == 2:
        print('You lose')
   else:
    print('invalid move!')

elif machine == 1: #machine use paper
     if player == 0:
         print('You lose') 
     elif player == 1:
         print('A TIE') 
     elif player == 2:
        print('You win')
     else:
        print('invalid move!')

elif machine == 2: #machine use scissors
      if player == 0:
         print('You win')    
      elif player == 1:
        print('You lose')    
      elif player == 2:
        print('A tie') 
      else:
        print('invalid move!')
