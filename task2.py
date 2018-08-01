import random

words = [word.rstrip('\n') for word in open('words.txt')]
randomPhrase = " ".join([words[random.randrange(0, len(words))] for i in range(4)])

randomPhrase

#reverse both the order of the 4 words and the order of the letters in each word

reversePhrase = randomPhrase[::-1]
print(reversePhrase)
