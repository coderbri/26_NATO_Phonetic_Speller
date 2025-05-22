# 26 NATO Phonetic Speller

## Overview

This project allows users to enter a word (e.g., their name), and returns a list of phonetic code words. It's inspired by the common struggle of spelling out names clearly over the phone. Instead of improvising words, users are provided with standardized NATO phonetics like "Alpha", "Bravo", "Charlie", etc.

## Concepts Implemented

- **Dictionary Comprehension**: To convert CSV data into a dictionary.
- **List Comprehension**: To generate a list of phonetic words from user input.
- **Reading CSV with Pandas**: To load and parse the NATO phonetic alphabet.

## Features / Project Logic

- Loads a CSV file containing NATO phonetic codes.
- Creates a dictionary mapping letters to their corresponding phonetic code.
- Accepts user input and converts it to uppercase.
- Outputs the phonetic spelling using list comprehension.

## How to Run

1. Ensure you have `pandas` installed:
   ```bash
   pip install pandas
    ```

2. Make sure `nato_phonetic_alphabet.csv` is in the same directory as the script.

3. Run the script:
    ```py
    python main.py
    ```

4. Input a word when prompted and view the phonetic spelling.
    ```py
    Enter a word: jane doe
    ['Juliet', 'Alfa', 'November', 'Echo', 'Delta', 'Oscar', 'Echo']
    ```

## Acknowledgements

Inspired by real-world communication needs for clear spelling over phone or radio, this project is implemented as part of a Python learning journey through Dr. Angela Yu's 100 Days of Code: Python Pro Bootcamp.