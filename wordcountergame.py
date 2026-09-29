import time
print("---------Welcome to the Word and Character and Lines Counter--------")
print("In this you can count the number of words or characters in a file or text ...")
print("Write 'exit' to end this program.")
print("Write 'back' to go to the previous page.")
while True: 
  start=input("Write 'start' to start and 'end' to exit ::")
  if (start.lower().strip()=="start"):
    while True:
      que=input("What do you want to count ' Character or words or line'? ")
      if (que.lower().strip()=="words") or (que.lower().strip()=="word"):
        while True:
          ask=input("file or textor exit?")
          if (ask.lower().strip()=="text") :
            text=input("Please enter the text :")
            name=input('in which txt file do you want too save this as texxt you can tell anexistinf file name but withouut .txt::')
            name=name.strip().lower()
            words=text.split()
            time.sleep(0.5)
            print("Total number of words are:",len(words))
          elif (ask.lower().strip()=="file") :
            file=input("Enter your file name :")
            with open(f"{file}.txt","r") as f:
              data=f.read()
              dataword=data.split()
              time.sleep(0.5)
              print("Total number of words are:",len(dataword))
          elif (ask.lower().strip()=="back"):
            break
          else:
            print("Please give a valid answer!!")  
      elif (que.lower().strip()=="lines") or (que.lower().strip()=="line"):
        while True :
          file=input("Enter your file name :")
          if (file.lower().strip()=="back")  :
            break    
          else:
            try:
              with open(f"{file}.txt","r") as f:
                data=f.readlines()
                i=0
                for eachline in data:
                  i+=1
                time.sleep(0.5)  
                print("Total number of lines are :",i)
            except:
              
              print("Enter a valid file name this file deos not exist")    
      elif (que.lower().strip()=="character") or  (que.lower().strip()=="characters"):
        while True:        
          ask=input("file or text or exit?")
          if (ask.lower().strip()=="text") :
            text=input("Please enter the text :")
            textchar=text.replace(" ","")
            time.sleep(0.5)
            print("Total number of characters are:",len(textchar))
          elif (ask.lower().strip()=="file") :
            file=input("Enter your file name :")
            try:
              with open(f"{file}.txt","r") as f:
                data=f.read()
                datachar=data.replace(" ","")
                time.sleep(0.5)
                print("Total number of characters are:",len(datachar))
            except:
                print("Enter a valid file name this file deos not exist")       
          elif (ask.lower().strip()=="back"):
                    break
          else:
                    print("Please give a valid answer!!")
      elif (que.lower().strip()=="back")  :
        break      
      else:
        print("Please give a valid answer!!")
  elif  (start.lower().strip()=="end"):
    break  
  else:
     print("Please enter a valid answer!!!!!!!!!!") 