
.PHONY: all clean test

# Note: for convience we still git commit this file despite it being generated.
ALL_DOIS_TXT := all_dois.txt

all: $(ALL_DOIS_TXT)

clean:

test: all

$(ALL_DOIS_TXT): $(wildcard dois/*.txt)
	cat $^ | grep -v '^$$' > "$@"
