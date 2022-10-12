from ast import Lambda
import string
def load_words(file_name):    
    print('Loading word list from file...')    
    in_file = open(file_name, 'r')    
    line = in_file.readline()
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

def is_word(word_list, word):
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    f = open("Unit05\\story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'Unit05\\words.txt'

class Message(object):    
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        new_dict = {}
        
        for l in string.ascii_lowercase:
            index = (string.ascii_lowercase.index(l) + shift) % 26

            new_dict[l] = string.ascii_lowercase[index]
            new_dict[l.capitalize()] = string.ascii_uppercase[index]

        return new_dict

    def apply_shift(self, shift):
        new_dict = self.build_shift_dict(shift)
        output = ''
        for l in self.get_message_text():
            if l in new_dict:
                output += new_dict[l]
            else:
                output += l
        return output

class PlaintextMessage(Message):
    def __init__(self, text, shift):        
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)

    def get_shift(self):
        return self.shift

    def get_encrypting_dict(self):
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        return self.message_text_encrypted

    def change_shift(self, shift):
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        Message.__init__(self, text)

    def decrypt_message(self):
        def get_words_count(str):
            words = str.split(' ')

            count = 0
            for word in words:
                if is_word(self.get_valid_words(), word):
                    count += 1

            return count        

        l = []
        for s in range(-1, -27, -1):
            str = self.apply_shift(s)
            word_count = get_words_count(str)
            l.append((26+s, str, word_count))

        l.sort(key = lambda x:x[2], reverse=True)

        result = (l[0][0], l[0][1])

        return result




story = get_story_string()
ciphertext = CiphertextMessage(story)    
print('Actual Output:', ciphertext.decrypt_message())
    
