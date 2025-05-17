import re

# settings
dict_location = '/usr/share/dict/web2'
dict_word_seperator = '\n'

# getting the dict's words
with open(dict_location) as f:
    dict_words = f.read().split(dict_word_seperator)

# asking the person using this to give all matches so far
word_pattern = input('''What is the current known pattern for your word?

Please format the pattern like this
If you don't know that letter, type '_'.
Otherwise, type the letter.
Note that you do not need to seperate things by spaces, but you can. \n''') # this is the list of all the correct letters

word_pattern_re = word_pattern.replace(' ', '').replace('_', '.')

# now we're getting the best guess
# here we're specifically just getting info about the word from what the user said
word_length = word_pattern.replace(' ', '').__len__()

def get_matching_words(pattern: str):
    matching_words = []
    # here we're going through all the words in the dictionary
    for word in dict_words:
        # checking if the word matches the word pattern regular expression
        if re.fullmatch(pattern, word):
            matching_words.append(word)

    return matching_words

# now we're getting all words that match that pattern
matching_words = get_matching_words(word_pattern_re)

# now we're counting all the letters in each possible word
# then we use that to get the best letter to guess

def get_most_common_letter(words: list[str], bad_letters: str) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # here we're turning all the words into one string
    concated_string = ''.join(words).lower()

    # now we're actually couting all the letters
    most_common_letter = ''
    most_common_letter_count = 0
    for letter in alphabet:
        if not bad_letters.__contains__(letter) and concated_string.count(letter) >= most_common_letter_count:
            most_common_letter = letter
            most_common_letter_count = concated_string.count(letter)

    return most_common_letter
letters_not_in = ''
while True:
    new_letter_guessing = get_most_common_letter(matching_words, ''.join([word_pattern_re.replace('.', ''), letters_not_in]))
    print(f'The best letter to guess is {new_letter_guessing}')
    new_pattern = input('''Please enter the new pattern.
If that letter was the only letters left, quit python, or type "Robert '); DROP TABLE Students;".
If that letter isn't there, type '):<'.\n''')
    # checking if we should quit python
    if new_pattern == 'Robert \'); DROP TABLE Students;':
        raise Exception('Sanitize your data inputs!')
    if new_pattern == '):<':
        letters_not_in += new_letter_guessing
    else:
        # getting the new regex to get more words
        word_pattern_re = new_pattern.replace(' ', '').replace('_', '.')
    # updating the new list of possible words
    matching_words = get_matching_words(word_pattern_re)
