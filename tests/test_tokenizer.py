import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

test_books_dir = os.path.join(parent_dir, 'test_books')

import pytest
from bws5dk.tokenizers import tokenize

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
    
# Initial fail test
@pytest.mark.xfail(reason= "We do not expect 29 words in this sentence")
def test_tokenize_fail():
    # Given the text from The Raven
    # When I pass text to the `tokenize()` function
    # I should get failure error as the length of the list should not be 20
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    tokens = tokenize(text)
    assert isinstance(tokens, list), f"Tokenizer failed on sample text: {text}"
    print(tokens)
    assert len(tokens) == 29, f"Failed as intended. We have {len(tokens)} words, not 29"

# Test The Raven
def test_tokenize_raven():
    raven_path = os.path.join(test_books_dir, 'pg17192.txt')
    with open(raven_path, 'r') as file:
        raven = file.read()
    tokens = tokenize(raven)
    assert isinstance(tokens, list), f"Failed to tokenize The Raven into list"
    print(tokens[0:50])

# Test all English files alone and together with parameterization
@pytest.mark.parametrize("book", [
    'pg17192.txt',
    'pg932.txt',
    'pg1063.txt',
    'pg10031.txt'])


def test_tokenize_all(book):
    book_path = os.path.join(test_books_dir, book)
    with open(book_path,'r') as booky:
        text = booky.read()
        tokens = tokenize(text)
        assert isinstance(tokens, list), f"Tokenizer failed on: {book}"
        print(f"Length of {book} tokeized list: " + str(len(tokens)))
        print(f"Sample of {book} tokens: ")
        print(tokens[0:15])

@pytest.mark.parametrize("book", [
    'pg17192.txt',
    'pg932.txt',
    'pg1063.txt',
    'pg10031.txt'])

def test_tokenize_combined(book):
    temp_file_path = os.path.join(test_books_dir, 'temp.txt')
    with open(temp_file_path, 'a') as temp_file:
        book_path = os.path.join(test_books_dir, book)
        with open(book_path, 'r') as book_file:
            text = book_file.read()
        temp_file.write(text + "\n")
    with open(temp_file_path, 'r') as temp_file:
        concatenated_text = temp_file.read()
    tokens = tokenize(concatenated_text)
    assert isinstance(tokens, list), f"Tokenizer failed on combined texts"
    print(f"Length of combined texts after {book} text added:: " + str(len(tokens)))


def test_delete_concat_text():
    temp_file_path = os.path.join(test_books_dir, 'temp.txt')
    os.remove(temp_file_path)
    assert not os.path.exists(temp_file_path), f"File {temp_file_path} still exists and needs to be removed"


# Test French strings
def test_tokenize_french():
    text = '''_Mais le Corbeau, perché solitairement sur ce buste placide, parla
    ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
    proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
    que je fis à peine davantage que marmotter «D'autres amis déjà ont
    pris leur vol--demain il me laissera comme mes Espérances déjà ont
    pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_'''
    tokens = tokenize(text)
    assert isinstance(tokens, list), f"Tokenizer failed on sample French text"
    print(tokens)
