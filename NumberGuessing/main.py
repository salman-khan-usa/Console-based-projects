import random

user_score = 0
comp_score = 0

while(user_score < 3 and comp_score < 3):
  computer = random.randint(1,30)
  user = int(input('Guess the Number(1-30):'))


  if(user == computer):
    user_score += 1
    print(f'🎉Congo, You won,Your number{user} matches the computer number{computer}.')

  else:
    comp_score += 1
    print(f'⚠️ wrong guess! The computer chose {computer}.')

if user_score == 3:
  print('🏆Congo,You won the Game.')

else:
  print('Sorry bruda ,computer won.')
