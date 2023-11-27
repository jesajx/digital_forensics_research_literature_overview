#!/usr/bin/env python3

import json
import re
import pathlib

with open("tags.json") as file:
    tags_from_doi = json.load(file)

with open("all_dois.txt") as file:
    dois = set(file.read().splitlines())

dois_by_venue = dict()
for path in pathlib.Path(".").glob("dois/*.txt"):
    venue = path.stem
    with path.open() as file:
        dois_by_venue[venue] = set(file.read().splitlines())
        dois_by_venue[venue] -= {""} # remove empty line

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

num_tot = len(dois)
num_done = len(done)
num_left = num_tot - num_done
done_percentage = num_done / num_tot * 100

print('### rough classification progress ###')
print(f'{num_done}/{num_tot} ({done_percentage:.2f}%) num_left={num_left}')

for venue in dois_by_venue:
    venue_num_tot = len(dois_by_venue[venue])
    venue_num_done = sum(1 for doi in dois_by_venue[venue] if doi in done)
    venue_num_left = venue_num_tot - venue_num_done
    venue_done_percentage = venue_num_done / venue_num_tot * 100
    print(f'{venue}:')
    print(f'  {venue_num_done}/{venue_num_tot} ({venue_done_percentage:.2f}%) num_left={venue_num_left}')

