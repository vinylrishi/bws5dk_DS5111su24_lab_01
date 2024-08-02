"""This is the text tokenizer function. I am required to put this docstring for linting tests."""
import string
import logging
from collections import Counter

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def clean_text(txt):
    """This function should make all text 
    lowercase and remove punctuation"""
    assert isinstance(txt,str), "String inputs only"

    log.info('Removing punctuation and case sensitivity')
    trans = str.maketrans('', '', string.punctuation)
    new_text = txt.lower().translate(trans)

    log.info('Text cleaned')

    assert isinstance(new_text, str), "String ouputs only"
    return new_text


def tokenize(txt):
    """This function should call the clean_text then 
    tokenize all words in the cleaned text into a list"""
    assert isinstance(txt,str), "String inputs only"

    log.info("Text getting cleaned")
    cleaned_text = clean_text(txt)
    log.info("Text has been cleaned")

    log.info("Tokenizing words into list")
    token_list = cleaned_text.split()
    log.info("Text has been tokenzied")

    assert isinstance(token_list,list), "Output should be a list"
    return token_list

def count_words(txt):
    """This function should take the list of tokenized words 
    and count the frequency of each word into a dictionary"""
    assert isinstance(txt,str), "String inputs only"
    log.info("Clean and tokenize input text")
    token_list = tokenize(txt)

    assert isinstance(token_list, list), "Tokenizer failed to create a list"
    log.info("Text is cleaned and words are in a list")

    log.info("Counting word fequencies...")
    counts = Counter(token_list)
    log.info("Done counting")

    assert isinstance(counts, dict), "Dictionary was not created"

    return counts
