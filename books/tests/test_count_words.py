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




