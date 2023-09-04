#!/bin/bash

grep '^"10\.' tags.json | sort | uniq -c | grep -v ' 1 '
num_duplicates=$(grep '^"10\.' tags.json | sort | uniq -c | grep -v ' 1 ' | wc -l)
echo "num_duplicates=$num_duplicates"
(( $num_duplicates == 0 ))
