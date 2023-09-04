
.PHONY: all clean test

all: all_dois.txt

clean:

test:
	./check_completeness.py
	./check_duplicate_tags.sh

all_dois.txt: $(wildcard dois/*.txt)
	cat $^ | grep -v '^$$' > "$@"
