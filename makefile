default: 
	@cat makefile

get_texts:
	@bash get_the_books.sh

# Add Raven specific jobs
pg17192.txt:
	wget https://www.gutenberg.org/cache/epub/17192/pg17192.txt

raven_line_count: pg17192.txt
	cat pg17192.txt | wc -l

raven_word_count: pg17192.txt
	cat pg17192.txt | wc -w

raven_counts: pg17192.txt
	@echo "'raven' count:"
	cat pg17192.txt | grep raven | wc -l
	@echo "'Raven' count:"
	cat pg17192.txt | grep Raven | wc -l
	@echo "All case count:"
	cat pg17192.txt | grep -E "(raven|Raven)" | wc -l

# Jobs for all downloads combined

total_lines: pg17192.txt
	cat *.txt | wc -l

total_words: pg17192.txt
	cat *.txt | wc -w


output_all_jobs: raven_line_count raven_word_count raven_counts total_lines total_words 	

check_py_requirements: 
	python3 -m venv env; sudo pip install --upgrade pip; sudo pip install -r requirements.txt

env:
	python3 -m venv env; . env/bin/activate; sudo pip install --upgrade pip; sudo pip install -r requirements.txt

test:
	pytest -vvx tests

