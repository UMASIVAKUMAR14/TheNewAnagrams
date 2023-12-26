import random
words = []

def lettersPicked():
  vowels = ["a", "e", "i", "o", "u"]
  consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
  chosen = ""
  for i in range(2):
    r = random.randint(0,len(vowels)-1)
    chosen+= vowels[r] + " "
    vowels.remove(vowels[r])
  for j in range(5):
    r = random.randint(0,len(consonants)-1)
    chosen+= consonants[r] + " "
    consonants.remove(consonants[r])  
  vowels = ["a", "e", "i", "o", "u"]
  consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
  return chosen

  
def main():
  if (input("Would you like to read the instructions?(yes/no)") == "yes"):
    instructions()
  print()
  alpha = lettersPicked()
  print("Your letters are " + alpha)
  print()
  
  score = 0
  for s in range(5):
    word = input("Word: ")
    while (checkWord(word, alpha) == False):
      print("The word must have a length greater than 2, cannot be previously used, and can only use the above letters.")
      word = input("Word: ")
    print("Your word is worth ", scoreWord(word), " points.")
    score+= scoreWord(word)
    if (scoreWord(word) > 20):
      print("Wow, great word!")
    print()
  print("Your score is ", score)

  if (input("Would you like to play again?(yes/no)") == "yes"):
    main()
  else:
    print("Thank you for playing!")
  

def instructions():
  print()
  print("Welcome to the new anagrams! You will recieve 7 letters. 2 will be vowels, 5 will be consonants. You will be able to give 5 words using the letters, and the letters can be repeated how many ever times you would like to use them. Words cannot be repeated. Use integrity when deciding what is a word! The longer the words, the more points you will receive. The more points, the better! Have fun my friend!")
  


def checkWord(doubt, beta):
  if (len(doubt) < 3):
    return False
  for q in range(len(doubt)):
    if (beta.find(doubt[q]) < 0):
      return False
  for p in words:
    if (doubt == p):
      return False
  words.append(doubt)
  return True


def scoreWord(quest):
  if (len(quest) == 3):
    return(2)
  elif (len(quest) == 4):
    return(5)
  elif (len(quest) == 5):
    return(15)
  elif (len(quest) == 6):
    return(25)
  elif (len(quest) >= 7):
    return(50)


main()