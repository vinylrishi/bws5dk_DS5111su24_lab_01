import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Had to google this directory code to ensure tokenizers.py was being used

import pytest
from tokenizers import tokenize

# Initial true test
def test_tokenize():
    # Given the text from The Raven
    # When I pass text to the `tokenize()` function
    # I should get cleaned text that is all lowercase and has no punctuation. Each word of the text is stored in a list that is returned to user.
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    tokens = tokenize(text)
    assert isinstance(tokens, list), f"Tokenizer failed on sample text: {text}"
    print(tokens)
    assert len(tokens) == 25, f"The above sentence should only have 25 words, not {len(tokens)}"
    


