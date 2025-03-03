import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

test_books_dir = os.path.join(parent_dir, 'test_books')

import pytest
from bws5dk.tokenizers import clean_text, tokenize, count_words

# Note, in creating tokenizer function, clean_text was aleady integrated. Likewise, count_words function already integrates tokenize. Nonetheless, we will create these integration funcitons.

# Initial true test
@pytest.mark.integration
def test_integration_pass():
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    cleaned = clean_text(text)
    counts = count_words(text)
    assert isinstance(cleaned, str), f"Text Cleaner failed on sample text: {text}"
    assert len(cleaned) <= len(text), f"The cleaned text cannot be longer than the input text"
    assert isinstance(counts, dict), f"Word count failed on sample text: {text}"
    assert counts['the'] == 2, f"The word `the` appears twice in the sentence, not {counts['the']} times"
    print(cleaned)
    print(counts)


# Initial fail test
@pytest.mark.integration
@pytest.mark.xfail(reason= "Cleaner shouldn't do nothing")
def test_integration_fail():
    # Given the text from The Raven
    # When I pass text to the `clean_text()` function
    # I should inentionally fail the test as expected
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    cleaned = clean_text(text)
    counts = count_words(text)
    assert isinstance(cleaned, str), f"Text Cleaner failed on sample text: {text}"
    assert len(cleaned) <= len(text), f"The cleaned text cannot be longer than the input text"
    assert isinstance(counts, dict), f"Word count failed on sample text: {text}"
    assert counts['the'] == 5, f"The word `the` appears twice in the sentence, not {counts['the']} times"
    print(cleaned)
    print(counts)


# Test The Raven integration
@pytest.mark.integration
def test_integration_raven():
    raven_path = os.path.join(test_books_dir, 'pg17192.txt')
    with open(raven_path, 'r') as file:
        raven = file.read()
    cleaned = clean_text(raven)
    counts = count_words(cleaned)
    assert isinstance(counts, dict), f"Word count failed on The Raven"
    print('Count for word `the`: ' + str(counts['the']))






