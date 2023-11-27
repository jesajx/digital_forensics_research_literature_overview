
.PHONY: all clean test

all: all_dois.txt

clean:

test:
	./check_completeness.py
	./check_duplicate_tags.sh
	./check_spurious.py

all_dois.txt: $(wildcard dois/*.txt)
	cat $^ | grep -v '^$$' > "$@"
