#!/usr/bin/env python3

import json
import re
import pathlib

with open("tags.json") as file:
    tags_from_doi = json.load(file)

with open("all_dois.txt") as file:
    dois = set(file.read().splitlines())

spurious = set(tags_from_doi.keys())-dois

if len(spurious) != 0:
    print("--- BEGIN spurious papers ---")
    for x in spurious:
        print(x)
    print("--- END spurious papers ---")
