#!/bin/bash

grep '^"10\.' tags.json | sort | uniq -c | grep -v ' 1 '
