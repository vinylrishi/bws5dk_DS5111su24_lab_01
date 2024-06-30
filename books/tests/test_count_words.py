import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Had to google this directory code to ensure tokenizers.py was being used

import pytest
from tokenizers import count_words

# Initial true test
def test_count_words():
    # Given the text from The Raven
    # When I pass text to the `count_words()` function
    # I should get a dictionary containing the feequency of each word in the text
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    counts = count_words(text)
    assert isinstance(counts, dict), f"Word count failed on sample text: {text}"
    assert counts['the'] == 2, f"The word `the` appears twice in the sentence, not {counts['the']} times"
    print(counts)


# Initial fail test
@pytest.mark.xfail(reason= "The sentence has `the` twice, not once")
def test_count_words_fail():
    # Given the text from The Raven
    # When I pass text to the `count_words()` function
    # I should inentionally fail the test by getting comparing to the wrong count
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    counts = count_words(text)
    assert isinstance(counts, dict), f"Word count failed on sample text: {text}"
    assert counts['the'] == 1, f"We have succefully failed as `the` appears twice, not once in the test sentence"
    print(counts)

# Test The Raven
def test_count_words_raven():
    with open('test_books/pg17192.txt', 'r') as file:
        raven = file.read()
    counts = count_words(raven)
    assert isinstance(counts, dict), f"Word count failed on The Raven"
    print('Count for word `the`: ' + str(counts['the']))

# Test all English files alone and together with parameterization
@pytest.mark.parametrize("books", [
    'test_books/pg17192.txt',
    'test_books/pg932.txt',
    'test_books/pg1063.txt',
    'test_books/pg10031.txt'])


def test_count_words_all(books):
    for book in books:
        with open(book,'r') as booky:
            text = booky.read()
            counts = count_words(text)
            assert isinstance(counts, dict), f"Word count failed on: {book}"
            print('Count for word `the`: ' + str(counts['the']))

def test_count_words_combined(books):
    combined_text = ""
    for book in books:
        with open(book,'r') as booky:
            combined_text += " " + booky.read()
    counts = count_words(combined_text)
    assert isinstance(counts, dict), f"Tokenizer failed on combined texts"
    print('Count for word `the` in combined text: ' + str(counts['the']))

# Test French strings
def test_count_words_french():
    text = '''_Mais le Corbeau, perché solitairement sur ce buste placide, parla
    ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
    proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
    que je fis à peine davantage que marmotter «D'autres amis déjà ont
    pris leur vol--demain il me laissera comme mes Espérances déjà ont
    pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_'''
    counts = count_words(text)
    assert isinstance(counts, dict), f"Word count failed on sample French text"
    assert counts['il'] == 3, f"The word `the` appears three times in the sentence, not {counts['the']} time(s)"
    print(counts)