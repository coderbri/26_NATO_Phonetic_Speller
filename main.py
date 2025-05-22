import pandas

# * Create NATO phonetic alphabet dictionary from CSV
nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dictionary = {row.letter:row.code for index, row in nato_dataframe.iterrows()}

# * Convert user input into list of phonetic code words
word = input("Enter a word: ").strip().upper()
phonetic_code_words = [phonetic_dictionary[letter] for letter in word if letter in phonetic_dictionary]
print(phonetic_code_words)
