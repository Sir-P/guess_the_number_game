# import libraries
import random
class GuessGame:
  def __init__(self, level=1) -> None:
    """This is a guessing game in which the computer generate a random number and require you to guess the correct number if thethe number if too high or low. the computer gives you a hints"""
    self.level = level
    def game_level():
      print('Welcome to Guess the Number Game !!!')
      print('Enter desire level of difficulty.\n\neasy, medium or hard')
      lev = input('Level: ')
      #level = 1
      if lev.lower()== 'easy':
        level = self.level
      elif lev.lower() == 'medium':
        level = self.level + 1
      elif lev.lower() == 'hard':
        level = self.level + 2
      else:
        level = self.level
      return level
    self.level = game_level()
     
  def start(self):
    cur = self.level
    while cur:
      print(f'Level : {cur}')
      print('\n\nEnter yes to Start and no to Quit')
      inp = input('Start: ' )
      while inp:
        if inp == 'yes' or inp == 'no':
          break
        else:
          print("Enter a Valid String Literal i.e Yes of No")
          inp = input('Start: ' ).lower()
          continue
      if inp.lower() == 'yes':
        if cur == 1:
          cur=self.easy()
        elif cur == 2:
          cur=self.medium()
        else:
          self.hard()
      else:
        break

  def easy(self):
    guess_number = random.randrange(0,10)
    trial = 3
    while trial:
      trial -= 1
      guess = eval(input('guess a number between 0 and 10 : '))
      guess_dict ={
      'high': f'Number is too high, you have {trial} trial left, \nTry again !',
      'low': f'Number is too low, you have {trial} trial left, \nTry again !,',
      'win': f'Correct the answer is {guess_number}, \nYou win',
      'lost': f'Sorry the answer is {guess_number}, \nYou lost, Game Over !',
    }
      if guess == guess_number:
        print(guess_dict['win'],'\n\nWelcome to the next level: \nMedium')
        cur = 2
        return cur
      elif guess > guess_number:
        print(guess_dict['high'])
      else:
        print(guess_dict['low'])
      if trial == 0:
        print(guess_dict['lost'], '\n\nPlay agein !!!')
        cur = 1
        return cur

  def medium(self):
    guess_number = random.randrange(0,100)
    trial = 5
    while trial:
      trial -= 1
      guess = eval(input('guess a number between 0 and 100 : '))
      guess_dict ={
      'high': f'Number is too high, you have {trial} trial left, \nTry again !',
      'low': f'Number is too low, you have {trial} trial left, \nTry again !,',
      'win': f'Correct the answer is {guess_number}, \nYou win',
      'lost': f'Sorry the answer is {guess_number}, \nYou lost, Game Over !',
    }
      if guess == guess_number:
        print(guess_dict['win'],'\n\nWelcome to the next level: \nHard')
        cur = 3
        return cur
      elif guess > guess_number:
        print(guess_dict['high'])
      else:
        print(guess_dict['low'])
      if trial == 0:
        print(guess_dict['lost'])
        print(guess_dict['lost'], '\n\nPlay agein !!!')
        cur = 2
        return cur

  def hard(self):
    guess_number = random.randrange(0,1000)
    trial = 7
    while trial:
      trial -= 1
      guess = eval(input('guess a number between 0 and 1000: '))
      guess_dict ={
      'high': f'Number is too high, you have {trial} trial left, \nTry again !',
      'low': f'Number is too low, you have {trial} trial left, \nTry again !,',
      'win': f'Correct the answer is {guess_number}, \nYou win',
      'lost': f'Sorry the answer is {guess_number}, \nYou lost, Game Over !',
    }
      if guess == guess_number:
        print(guess_dict['win'], '\n\nYou are the World Champion !!!')
        print('Play again')
        break
      elif guess > guess_number:
        print(guess_dict['high'])
      else:
        print(guess_dict['low'])
      if trial == 0:
        print(guess_dict['lost'], '\n\nPlay agein !!! \nHard')
        cur = 3
        return cur

if __name__=="__main__":
  new_game = GuessGame()
  new_game.start()