# Importing modules
import random
import re

# Getting random words from the dictionary file. 
def get_random_word():
    with open("Hangman/hangmandict.txt") as dictionary: 
        words = dictionary.readlines()
    random_string = random.choice(words).strip() 
    random_word = random_string.upper()     # Converts the word to all uppercase
    return random_word 


# Easier to replace with underscores + formatting
def add_space(answer):  # Adds a space between letters so "EAT" becomes "E A T"
    space_string = " ".join(answer)
    return space_string

# Comverts letters to underscores. Easeier to read. ___ VS _ _ _ 
def convert_to_underscore(answer):
    convert = answer 
    underscore = re.sub('[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]', "_", convert)
    return underscore

# Joins a list to become a string 
def join_word(word):
    joined = ""
    for i in word:
        joined += i 
    return joined

# Finds indexes of all instances of search in a list.
def find_index(list, search):   # List is the list to search, search is the item to search
    indexes = []
    for idx, value in enumerate(list):
        if value == search:
            indexes.append(idx)
    return indexes
        
# Hangman Diagrams List 
def print_hangman_diagram(hang):
    hangman_diagrams = [
        """

             |
             |
             |
             |
             |
        =========''' 
        """,
        """
         +---+
         |   |
             |
             |
             |
             |
        =========''' 
        """,
        """
         +---+
         |   |
         O   |
             |
             |
             |
        =========''' 
        """,
        """
         +---+
         |   |
         O   |
         |   |
             |
             |
        =========''' 
        """,
        """
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =========''' 
        """,
        """
         +---+
         |   |
         O   |
        /|\  |
             |
             |
        =========''' 
        """,
        """
         +---+
         |   |
         O   |
        /|\  |
        /    |
             |
        =========''' 
        """,
        """
         +---+
         |   |
         O   |
        /|\  |
        / \  |
             |
        =========''' 
        """
    ]
    print(hangman_diagrams[hang])

# Play the game :) 
def play_game():
    game_answer = get_random_word()
    hang = 0  # Hang is the number of errors you made
    correct = 0 # Number of correct answers
    wrong = 0 # Number of wrong answers 
    guesscount = 0 # Number of guesses
    
    spaced_answer = add_space(game_answer) # Spaces the abswer with add_space() function
    spaced_list = list(spaced_answer) # Creates a list from the spaced_answer

    underscores = convert_to_underscore(spaced_answer) # Converts each spaced letter to underscrore 
    underscores_list = list(underscores) # Creates a list of underscores

    used_letters = [] # Initialises a list of used letters. Blank for now
    while True:
        joined_answer = join_word(underscores_list) # Creates a word from the underscore list 

        #If the word is correct, print it and end the while loop
        if joined_answer == spaced_answer and hang < 7:
            print(joined_answer)
            print(" ")
            print("You win!")
            print("Answer: ", game_answer)
            final = "Won"
            break

        # If you use all the tries, you lose and it prints answer
        elif hang == 7:
            print("YOU DIED")
            print_hangman_diagram(hang)
            print("You Lose! The correct answer was", game_answer)
            final = "died"
            break
        
        elif hang < 7:
            print_hangman_diagram(hang) # Print the hangman diagram based on amount of errors
            print(" ")
            print(joined_answer) # Prints the _ and letter combo for guessing.
            print("Used letters:", used_letters) # Prints previously used letters
            print(" ")
            guess = input("Enter Letter: ").upper()
            print(" ")
            print(" ")
            if len(guess) > 1:
                print("Please only use 1 letter")
                continue
            elif len(guess) == 1:
        
                # If the letter is correct, display the letter and replcae the _'s. 
                # Add the letter used to the used letters list
                if guess in spaced_list and guess not in used_letters:
                    hang += 0 
                    correct += 1
                    guesscount += 1
                    used_letters.append(guess)
                    index = find_index(spaced_list, guess)
                    for i in index:
                        underscores_list[i] = guess
                    print("Correct")
                    print("You have", 7 - hang, "errors remaining")

                # If the letter has already been used, do nothing and state it has been used.
                elif guess in used_letters:
                    print("You hvae already used this letter.")
                    print("You have", 7 - hang, "errors remaining")

                # If the letter is not correct, add an error count.
                # Add the letter used to the used letters list
                elif guess not in spaced_list and guess not in used_letters:
                    hang += 1
                    wrong += 1
                    guesscount += 1 
                    used_letters.append(guess)
                    print("Wrong")
                    print("You have", 7 - hang, "errors remaining")
    
    # Option for players to view thier statisitcs
    stats = input("Do you wish to see your stats? [Y/N]: ")
    print(" ")
    if stats == "Y" or stats =="y":
        print("You", final)
        print(" ")
        print("You guessed", guesscount, "times.")
        print("You made", hang, "errors and got", correct, "letters correct")
        print("""
        
        Loading...
        """)
    elif stats == "N" or stats == "n":
        print("Loading...") 
    

    cont_choice = input("Do you wish to continue: [Y/N] ")
    if cont_choice =="N" or cont_choice == "n":
        print("""
            EEEEE   N     N   DDD
            E       N N   N   D   D
            EEEEE   N  N  N   D    D
            E       N   N N   D   D
            EEEEE   N     N   DDDD
        """)
    elif cont_choice == "Y" or cont_choice == "y":
        play_game()

if __name__ == "__main__":
    play_game()