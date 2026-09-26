import random
def guessgame():
  print("Hello welcome to the Randome Guessing game")
  print("I am Afeefa and I wrote the code for this game \nthis is my second time creating something like this so.\nIf you think any changes can be made feel free to tell me.")
  print("Here you have to guess a number between 1 and 100.\nAnd i will tell you if it's right or wrong")
  print("Enter 'Start' to star to game")
  print("Enter 'Exit' to end to game")
  while True:
    ask=input("Do you want to start the game?")
    if ask.lower()=="start" or ask.lower()=="yes":
      nums=range(1,101)
      num=random.choice(nums)
      k=0
      n=input("How many times do you want to try ?")
      try :
          n=int(n)
          print(f"You have {n} try's.")
          while True:
            choice=input("Guess a number between 1 and 100:")
            k=k+1
            print("attempt",k)
            if k==n:
              print('SORRY! You have already tried ',n,' times')
              break
            try:
                choise=int(choice)     
                if choise>num :
                  print("Try a smaller number")
                if choise<num :
                  print("Try a bigger number")
                if choise==num :
                  print("You guessed it right"+'\n' , "CONGRATULATIONS ! YOU WON") 
                  break
            except:
                print("Invalid Input.Please Enter a number.")
                break     
      except:
          print("Enter a valid number")
          continue
    if ask.lower()=="exit" or ask.lower()=="no":
          break
    else :
      print("Please enter a vaalid answer")        
          

guessgame()  