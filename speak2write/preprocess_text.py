import string
import re

class preprocess_text:
    """Given a sentence, this clas is used to apply some preprocessing functions before going to further steps."""


    def __init__(self):
        pass

    @staticmethod
    def decontract(sentence):
        sentence = re.sub(r"won\'t", "will not", sentence)
        sentence = re.sub(r"can\'t", "can not", sentence)

        # general
        sentence = re.sub(r"n\'t", " not", sentence)
        sentence = re.sub(r"\'re", " are", sentence)
        sentence = re.sub(r"\'s", " is", sentence)
        sentence = re.sub(r"\'d", " would", sentence)
        sentence = re.sub(r"\'ll", " will", sentence)
        sentence = re.sub(r"\'t", " not", sentence)
        sentence = re.sub(r"\'ve", " have", sentence)
        sentence = re.sub(r"\'m", " am", sentence)
        return sentence


    @staticmethod
    def remove_punct(sentence):
        remove = string.punctuation
        remove = remove.replace("$", "") # don't remove hyphens
        remove = remove.replace("&", "") # don't remove hyphens
        remove = remove.replace("%", "") # don't remove hyphens

        pattern = r"[{}]".format(remove) # create the pattern

        sentence = re.sub(pattern, "", sentence) 
        return sentence

    @staticmethod
    def remove_whitespace(sentence):
        return sentence.strip()
    
    @staticmethod
    def prepro(sentence):
        sentence=preprocess_text.decontract(sentence)
        sentence=preprocess_text.remove_punct(sentence)
        sentence=preprocess_text.remove_whitespace(sentence)

        return sentence
