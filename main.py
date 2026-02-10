##############################################################
# Project:        NATO Phonetic Alphabet Speller
# Description:    Converts user input into the NATO Phonetic Alphabet.
#                 Includes robust error handling to catch non-alphabetic
#                 characters using a try-except-else block with recursion
#                 to ensure a valid result is eventually produced.
##############################################################

import pandas

# Create NATO phonetic alphabet dictionary from CSV
# The dictionary comprehension maps 'letter' to its corresponding 'code'
nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dictionary = {row.letter: row.code for index, row in nato_dataframe.iterrows()}

def generate_phonetic_code_words():
    """
    Prompts user for input, validates it, and prints the phonetic list.
    If an invalid character is entered, it catches the KeyError and 
    restarts the function.
    """
    word = input("Enter a word: ").strip().upper()

    try:
        # Attempt to create a list of codes based on each letter in the word
        output_list = [phonetic_dictionary[letter] for letter in word]
    except KeyError:
        # Catch errors if the user enters numbers, spaces, or symbols not in the CSV
        print("Sorry, only letters in the alphabet please.")
        # RECURSION: Start the function over to prompt the user again
        generate_phonetic_code_words()
    else:
        # This block only executes if the list comprehension finished without error
        print(output_list)

# Initial function call to start the program
generate_phonetic_code_words()
