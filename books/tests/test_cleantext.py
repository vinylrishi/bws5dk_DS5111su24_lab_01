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


