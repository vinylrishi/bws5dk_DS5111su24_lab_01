import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Had to google this directory code to ensure tokenizers.py was being used

import pytest
from tokenizers import clean_text

# Initial true test
def test_clean_text():
    # Given the text from The Raven
    # When I pass text to the `clean_text()` function
    # I should get new cleaned text that is all lowercase and has no punctuation. This should be in string format.
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    cleaned = clean_text(text)
    assert isinstance(cleaned, str), f"Text Cleaner failed on sample text: {text}"
    assert len(cleaned) <= len(text), f"The cleaned text cannot be longer than the input text"
    print(cleaned)


#Initial fail test
@pytest.mark.xfail(reason= "Cleaner shouldn't do nothing")
def test_clean_text_fail():
    # Given the text from The Raven
    # When I pass text to the `clean_text()` function
    # I should inentionally fail the test as expected
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    cleaned = clean_text(text)
    assert cleaned == "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.", f"We succefully failed, as our output should not be the original text: {text} "
    print('Our cleaned output: ' + cleaned)


# Test The Raven
def test_clean_text_raven():
    with open('test_books/pg17192.txt', 'r') as raven:
        text = raven.read()
    cleaned = clean_text(text)
    assert isinstance(cleaned, str), f"Text Cleaner failed on The Raven"
    print(cleaned[0:500])

# Test all English files alone and together with parameterization
@pytest.mark.parametrize("books", [
    'test_books/pg17192.txt',
    'test_books/pg932.txt',
    'test_books/pg1063.txt',
    'test_books/pg10031.txt'])


def test_clean_text_all(books):
    for book in books:
        with open(book,'r') as booky:
            text = booky.read()
            cleaned = clean_text(text)
            assert isinstance(cleaned, str), f"Text Cleaner failed on: {book}"
            print(f"Length of {book} text: " + str(len(cleaned)))
            print(f"Sample of {book} text: " + cleaned[0:45])


def test_clean_text_combined(books):
    combined_text = ""
    for book in books:
        with open(book,'r') as booky:
            combined_text += " " + booky.read()
    cleaned = clean_text(combined_text)
    assert isinstance(cleaned, str), f"Text Cleaner failed on combined texts"
    print("Length of combined texts: " + str(len(cleaned)))

# Test French strings
def test_clean_text_french():
    text = '''_Mais le Corbeau, perché solitairement sur ce buste placide, parla
    ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
    proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
    que je fis à peine davantage que marmotter «D'autres amis déjà ont
    pris leur vol--demain il me laissera comme mes Espérances déjà ont
    pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_'''
    cleaned = clean_text(text)
    assert isinstance(cleaned, str), f"Text Cleaner failed on sample text: {text}"
    assert len(cleaned) <= len(text), f"The cleaned text cannot be longer than the input text"
    print("Cleaned text: " + cleaned)



