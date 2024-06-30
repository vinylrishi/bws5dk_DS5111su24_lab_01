 # Repo: bws5dk_DS5111su24_lab_01
- gitignore should contain *.txt  
- Makerfile is in the "books" directory :)
  
## Lab Tokenizer  
- Added a token.py file that contains three functions to clean, tokenize, and count the frequency of words from a given string.
- Makefile also checks to make sure python3 and pip are installed (needed to use "sudo" for this because of ubuntu).
- Note: I am having an issue with the token.py file in in that the "logging" package I am trying to use seems to be overwritten by some custom "logging.py" file from anaconda. I am not sure what the repercussions of deleting this file are for other python works, so for now I will not change anything. I ran the token.py code in a jupyter notebook to test it with some sample strings and it works fine for all 3 functions.

## Lab Testing  
- Reorganized files into a "tests: directory so test_books directory could be accessed by testing notebooks and function testing python files.
- Renamed token.py to tokenizers.py because there is an existing token.py installed somewhere in anaconda3.
- There is some directory mapping code at the top of each functiont testing file that I found on google. It helped be resolve issues where the tokenizers.py file could not be found.
- Similarly, the notebook contains some hard coded directory path that needs to be changed for each user depending on where the repo is cloned. This ensured the test books could be accessed in the notebook.
- Note: Removed *.txt from gitignore becuase text files pulled from get_the_books.sh could not be pushed to repo.
  
### Test file and function descriptions
- test_cleantext.py tests pass and fail cases on a small string sample from the Raven using the test_clean_text() and test_clean_text_fail() function, resepectively.
- For assesments on larger texts, we have the test_clean_text_raven() function which cleans text on the entire Raven text (pg17192.txt), as well as the test_clean_text_all() and test_clean_text_combined() functions which cleans text on each book in test_books individually as well as a larger combined string, respectively.
- The test_tokenizer.py and test_count_words.py files have similar test functions to those described above for test_cleantext.py, but for their own functions within tokenizers.py.
- 
### Sample code output for test_cleantext.test_clean_text_all()  
  import test_cleantext
  import test_tokenizer
  import test_count_words
  
  books = ['test_books/pg17192.txt',
      'test_books/pg932.txt',
      'test_books/pg1063.txt',
      'test_books/pg10031.txt']
  
  test_cleantext.test_clean_text_all(books)
  
Output:
  
  Length of test_books/pg17192.txt text: 62378
  Sample of test_books/pg17192.txt text: ﻿the project gutenberg ebook of the raven
     
  Length of test_books/pg932.txt text: 60314
  Sample of test_books/pg932.txt text: ﻿the project gutenberg ebook of the fall of t
  Length of test_books/pg1063.txt text: 31382
  Sample of test_books/pg1063.txt text: ﻿the project gutenberg ebook of the cask of a
  Length of test_books/pg10031.txt text: 380935
  Sample of test_books/pg10031.txt text: ﻿the project gutenberg ebook of the complete 
