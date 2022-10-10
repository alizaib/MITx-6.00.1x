# The 6.00 Word Game
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
WORDLIST_FILENAME = "Unit04\\words.txt"

def loadWords():    
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList
def getFrequencyDict(sequence):    
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
def getWordScore(word, n):    
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    wordLength = len(word)
    score *= wordLength

    if wordLength == n:
        score += 50

    return score
def displayHand(hand):    
    print("Current Hand: ", end="")
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")
    print()
def dealHand(n):   
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand
def updateHand(hand, word):    
    handCopy = hand.copy()

    for letter in word:
        if letter in handCopy:
            if handCopy[letter] == 1:
                del handCopy[letter]
            else:
                handCopy[letter] -= 1
    return handCopy
def isValidWord(word, hand, wordList):
    handCopy = hand.copy()

    def isComposedofLettersInHand():
        for letter in word:
            if letter not in handCopy:
                return False
            else:
                handCopy[letter] -= 1
                if handCopy[letter] == 0:
                    del handCopy[letter]
        return True

    return len(word) > 0 and word in wordList and isComposedofLettersInHand()
def calculateHandlen(hand):    
    sum = 0
    for val in hand.values():
        sum += val
    return sum
def playHand(hand, wordList, n):    
    score = 0    
    while hand:
        displayHand(hand)        
        word = input("Enter word, or a '.' to indicate that you are finished: ")        
        if word == '.':            
            break
        else:
            if not isValidWord(word, hand, wordList):
                print("Invalid word, please try again.\n")
            else:
                wordScore = getWordScore(word, n)
                score += wordScore
                print("\"" +word + "\" earned "+ str(wordScore) +" points. Total: " + str(score) + " points\n")
                hand = updateHand(hand, word)

    if not hand:
        print("Run out of letters. Total score: " + str(score) + " points.")
    else:
        print("Goodbye! Total score: " + str(score) + " points.")
def playGame(wordList):
    hand = {}    
    while True:
        print()
        userInput = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if userInput == 'r' and not hand:
            print("You have not played a hand yet. Please play a new hand first!")
            continue

        elif userInput == 'r' or userInput == 'n':
            hand = hand if userInput == 'r' else dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)            
        
        elif userInput == 'e':
            return
        else:
            print("Invalid command.")


if __name__ == '__main__':
    wordList = loadWords()
    #playGame(wordList)
    #playHand({'h':1, 'i':1, 'c':1, 'z':1, 'm':2, 'a':1}, wordList, 7)
    #playHand({'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}, wordList, 7)
    #playHand({'n':1, 'e':1, 't':1, 'a':1, 'r':1, 'i':2}, wordList, 7)
    playGame(wordList)
