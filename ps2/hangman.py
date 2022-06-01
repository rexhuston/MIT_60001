# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
from operator import truediv
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()





def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    retval = False

    for i in secret_word:
      if i not in letters_guessed:
        retval = False
        break
      else:
        retval = True

    return retval



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass

    retval = ""

    #loop through letters in secret word
    #if letter in secret word, add letter to the return word
    #else add _ to the return word
    for i in secret_word:
      if i not in letters_guessed:
        retval += "_"
      else:
        retval += i

    return retval



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    retval = ""
    for i in string.ascii_lowercase:
      if i not in letters_guessed:
        retval += i

    return retval


    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass

    print ("Welcome to the game Hangman!")
    print ("I am thinking of a word that has",len(secret_word),"letters")
    #guess tracker, default to 6
    guesses = 6
    letters_guessed = ""
    letter = ""

    #warnings tracker, defaults to 3
    #user gets 3 invalid input warnings
    warnings = 3

    #hits, track number of good guesses
    hits = 0

    #init i
    i = 0

    while i < guesses:
      print("You have", guesses-i, "guesses left")
      print("Available letters:", get_available_letters(letters_guessed))

      letter = input("Please guess a letter: ")

      if letter in string.ascii_letters and letter not in letters_guessed:
        #valid guess
        letters_guessed += letter

        if letter in secret_word:
          print("Good guess:", get_guessed_word(secret_word, letters_guessed))
          hits+=1
        else:
          print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
          i+=1

        if is_word_guessed(secret_word, letters_guessed):
          print("Congratulations you have won!")
          print("Your total score is:", (guesses-i)*hits)
          break
      elif letter in letters_guessed:
        #warning -- already guessed that letter
        warnings-=1

        if warnings<0:
          print("Oops! You have already guessed that letter:"
              , "you have no warnings left so you lose one guess")
          i+=1
          break
        else:
          print("Oops! You have already guessed that letter:"
              , "you have ", warnings, "warnings left:"
              ,get_guessed_word(secret_word, letters_guessed))
      else:
        #warning -- invalid letter
        warnings-=1

        if warnings<0:
          print("Oops! That is not a valid letter:"
              , "you have no warnings left so you lose one guess")
          i+=1
          break
        else:
          print("Oops! That is not a valid letter:"
              , "you have ", warnings, "warnings left:"
              ,get_guessed_word(secret_word, letters_guessed))
      
      print("------------------------")

    if i>=guesses:
      print("Sorry you ran out of guesses, the word was", secret_word,".")
        




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    revealed = ""
    for l in my_word:
      if l not in revealed:
        revealed+=l
    
    match = False

    if len(my_word)!=len(other_word):
      match = False
    else:
      for i in range(len(my_word)):
        if my_word[i]==other_word[i]:
          match=True
        elif my_word[i]=="_" and other_word[i] not in revealed:
          match=True
        else:
          match=False
          break
    return match





def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matches = ""
    for word in wordlist:
      if match_with_gaps(my_word, word):
        matches+=(" "+word)

    if matches=="":
      print("No matches found")
    else:
      print(matches.strip())



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass

    print ("Welcome to the game Hangman!")
    print ("I am thinking of a word that has",len(secret_word),"letters")
    #guess tracker, default to 6
    guesses = 6
    letters_guessed = ""
    letter = ""

    #warnings tracker, defaults to 3
    #user gets 3 invalid input warnings
    warnings = 3

    #hits, track number of good guesses
    hits = 0


    #init i
    i = 0

    while i < guesses:
      print("You have", guesses-i, "guesses left")
      print("Available letters:", get_available_letters(letters_guessed))

      letter = input("Please guess a letter: ")

      if letter == "*":
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
      elif letter in string.ascii_letters and letter not in letters_guessed:
        #valid guess
        letters_guessed += letter

        if letter in secret_word:
          print("Good guess:", get_guessed_word(secret_word, letters_guessed))
          hits+=1
        else:
          print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
          i+=1

        if is_word_guessed(secret_word, letters_guessed):
          print("Congratulations you have won!")
          print("Your total score is:", (guesses-i)*hits)
          break
      elif letter in letters_guessed:
        #warning -- already guessed that letter
        warnings-=1

        if warnings<0:
          print("Oops! You have already guessed that letter:"
              , "you have no warnings left so you lose one guess")
          i+=1
          break
        else:
          print("Oops! You have already guessed that letter:"
              , "you have ", warnings, "warnings left:"
              ,get_guessed_word(secret_word, letters_guessed))
      else:
        #warning -- invalid letter
        warnings-=1

        if warnings<0:
          print("Oops! That is not a valid letter:"
              , "you have no warnings left so you lose one guess")
          i+=1
          break
        else:
          print("Oops! That is not a valid letter:"
              , "you have ", warnings, "warnings left:"
              ,get_guessed_word(secret_word, letters_guessed))
      
      print("------------------------")

    if i>=guesses:
      print("Sorry you ran out of guesses, the word was", secret_word,".")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)
    #print (match_with_gaps('a__le', 'apple'))

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
