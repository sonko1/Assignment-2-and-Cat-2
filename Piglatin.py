# A program that will take a word and output its pig latin version :
#if the word starts with a consoltant or a group of consoltant, moves all letters before the forst vowel to the end then adds "ay"
#if the word starts with a vowel , simply adds "way" to the end of the word

ay = 'ay'
way = 'way'
consonant = ('B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','Y','V','X','Z')
vowel = ('A','E','I','O','U')

user_word = input('Enter a word to translate to Pig Latin: ')
# getting first letter and making sure its a string and setting it to uppercase
first_letter = user_word[0]
first_letter = str(first_letter)
first_letter=first_letter.upper()
if first_letter in consonant:
    print(first_letter,'is a consonant')
    length_of_word = len(user_word)
    remove_first_letter = user_word[1:length_of_word]
    pig_latin=remove_first_letter+first_letter+ay
    print('The word in Pig Latin is:',pig_latin)
elif first_letter in vowel:
    print(first_letter,'is a vowel')
    pig_latin=user_word+way
    print('The word in Pig Latin is:',pig_latin)
else:
    print('I dont know what',first_letter,'is')