#!/usr/bin/env python3

import sys
import json
import re
import pathlib
import argparse


parser = argparse.ArgumentParser(prog='remaining.py')
parser.add_argument('--print-doi')
parser.add_argument('venue', nargs='?')

args = parser.parse_args()

with open("tags.json") as file:
    tags_from_doi = json.load(file)

if args.venue is None:
    with open("all_dois.txt") as file:
        dois = set(file.read().splitlines())
else:
    dois_dir = pathlib.Path('dois')
    path = dois_dir / f'{args.venue}.txt'
    with path.open() as file:
        dois = set(file.read().splitlines())

dois -= {""} # remove empty line

for doi, tags in tags_from_doi.items():
    new_tags = set()

    for k in tags:
        k = k.lower()
        new_tags.add(k)

        m = re.match(r"^([^:]*):\s*(.*)", k)
        if m:
            lhs = m.group(1)
            rhs = m.group(2)
            new_tags.add(lhs)
            if lhs == "contributionarea":
                new_tags.add(rhs)

    tags_from_doi[doi] = new_tags


done = {
    doi
    for doi, tags in tags_from_doi.items()
    if ("contributionarea" in tags or "not research" in tags or "not forensics" in tags) and doi in dois
}

for doi in dois:
    if doi not in done:
        if args.print_doi:
            print(doi)
        else:
            url = doi
            if "://" not in url: # "doi" var might actually be URL for some venues, so check first.
                url = f'https://doi.org/{doi}'
            print(url)
