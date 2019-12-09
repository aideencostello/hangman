#  _______
#  |     |
#  |     O
#  |    -|-
#  |    / \
# _|___ 

 
import sys

chosen=[]
word=[]
player=["1", "2"]

alphabet=[]
for i in "abcdefghijklmnopqrstuvwxyz":
   alphabet.append(i)

#################################################################
### startup and flow

def main():
   print("")
   printPhrase(getHangman(10), "\n")
   print("")
   player[0] = input_custom("Enter player 1's name: ")
   player[1] = input_custom("Enter player 2's name: ")
   print("")
   start()

def restart():
   print("\nNew Game\n")
   player.reverse()
   chosen.clear()
   word.clear()
   start()

def start():
   print("Player " + player[0] + "'s turn")
   userInputWord()
   printAll(False)
   guessCycle()
   
def guessCycle():
   userInputLetter();
   printAll();
   
   if checkWin():
      print("\nCongratulations, you guessed the word!")
      restart()
   elif checkLoss():
      print("\nUh oh, you died! The word was ", end="")
      printPhrase(word)
      restart()
   else: 
      guessCycle()

#################################################################
### user inputs

def input_custom(msg):
   res = input(msg)
   if (res in "exit") and ("exit" in res):
      exit()
   return res

def userInputWord(prefix=""):
   input_string = prefix + "Player " + player[0] + ", please enter a word:"
   res = input_custom(input_string).lower()
   clearLine(1)
   print(" " * (len(input_string) + len(res)))
   clearLine(1)
   wordGood, errorMsg = checkInputWord(res)
   if wordGood:
      inputWord(res)
   else:
      userInputWord(errorMsg + "! ")

def userInputLetter():
   guessLetter( input_custom("Player " + player[1] + ", please enter a letter:"))
   clearLine(1)

def guessLetter(letter):
   # player 2 guesses a letter 
   chosen.append(letter)

def inputWord(word_input):
   # player 1 chooses a word to be guessed
   for i in word_input:
      word.append(i)

def clearLine(n):
   sys.stdout.write("\033[F"*n)
   #print("clearing " + str(n))

#################################################################
### check states

def checkInputWord(input):
   for letter in input:
      if not letter in alphabet:
         return False, "Letter not in the alphabet"
   if 3>len(input):
      return False, "Word too short"
   return True, ""

def getErrors():
   # function to count the number of errors made so far
   res = 0
   for letter in chosen:
      if not letter in word:
         res += 1
   return res
   
def checkWin():
   count = 0
   distinctWord = []
   for letter in word:
      if not letter in distinctWord:
         distinctWord.append(letter)
         if letter in chosen:
            count +=1
   return count==len(distinctWord)

def checkLoss():
   count = 0
   for letter in chosen:
      if not letter in word:
         count += 1
   return count>9
   
#################################################################
### print

def printPhrase(input, line_end=""):
   for letter in input:
      print(letter, end=line_end)
   print("")

def printAll(initFlag=True):
   if initFlag:
      clearLine(11)
   printPhrase(getHangman(getErrors()), "\n")
   print(" ", end="")
   printPhrase(getWord())
   print("")
   printPhrase(getAlphabet())
   print("")

#################################################################
### printable objects 

def getWord():
   res = []
   for letter in word:
      if letter in chosen:
         res.append(letter)
      else:
         res.append("_")
   return res

def getAlphabet():
   # get the alphabet string, excluding any letters that have been chosen
   res = []
   for letter in alphabet:
      if letter in chosen:
         res.append("-")
      else:
         res.append(letter)
   return res

def getHangman(number):
   # function to get the hangman state based on input number
   # number indicates how many mistakes the guesser has made (max 10)

   # the series of characters that make up the hangman, one for each step
   symbols="_|_|O|--/\\"

   # turn on/off different pieces of the hangman, based on the input number
   symbolList = []
   for i in range(len(symbols)):
      if number>i:
         symbolList.append(symbols[i])
      else:
         symbolList.append(" ")

   # the base line by itself has a space and looks silly
   if number==1:
      middle_base="_"
   else:
      middle_base=symbolList[1]

   # define the block of characters to display the hangman
   hangmanSymbol = []
   hangmanSymbol.append( "  " + (symbolList[2] * 7) + " " )
   hangmanSymbol.append( "  " + symbolList[1] + (" "*5) + symbolList[3] + " " )
   hangmanSymbol.append( "  " + symbolList[1] + (" "*5) + symbolList[4] + " " )
   hangmanSymbol.append( "  " + symbolList[1] + (" "*4) + symbolList[6] + symbolList[5] + symbolList[7] )
   hangmanSymbol.append( "  " + symbolList[1] + (" "*4) + symbolList[8] + " " + symbolList[9] )
   hangmanSymbol.append( " " + symbolList[0] + middle_base + ( symbolList[0] * 3 ) + (" "*4) )
   
   return hangmanSymbol

#################################################################

main()
