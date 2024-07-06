import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

test_books_dir = os.path.join(parent_dir, 'test_books')

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
    raven_path = os.path.join(test_books_dir, 'pg17192.txt')
    with open(raven_path, 'r') as raven:
        text = raven.read()
    cleaned = clean_text(text)
    assert isinstance(cleaned, str), f"Text Cleaner failed on The Raven"
    print(cleaned[0:500])

# Test all English files alone and together with parameterization
@pytest.mark.parametrize("book", [
    'pg17192.txt',
    'pg932.txt',
    'pg1063.txt',
    'pg10031.txt'])


def test_clean_text_all(book):
    book_path = os.path.join(test_books_dir, book)
    with open(book_path,'r') as booky:
        text = booky.read()
        cleaned = clean_text(text)
        assert isinstance(cleaned, str), f"Text Cleaner failed on: {book}"
        print(f"Length of {book} text: " + str(len(cleaned)))
        print(f"Sample of {book} text: " + cleaned[0:45])


def test_clean_text_combined(book):
    temp_file_path = os.path.join(test_books_dir, 'temp.txt')
    with open(temp_file_path, 'a') as temp_file:
        book_path = os.path.join(test_books_dir, book)
        with open(book_path, 'r') as book_file:
            text = book_file.read()
        temp_file.write(text + "\n")
    with open(temp_file_path, 'r') as temp_file:
        concatenated_text = temp_file.read()
    cleaned = clean_text(concatenated_text)
    assert isinstance(cleaned, str), "Text cleaner failed on combined texts"
    print(f"Length of combined text after {book} text added: " + str(len(cleaned)))

def test_delete_concat_text():
    temp_file_path = os.path.join(test_books_dir, 'temp.txt')
    os.remove(temp_file_path)
    assert not os.path.exists(temp_file_path), f"File {temp_file_path} still exists and needs to be removed"


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



