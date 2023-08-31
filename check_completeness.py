#!/usr/bin/env python3

import json
import re

with open("tags.json") as file:
    tags_from_doi = json.load(file)

with open("all_dois.txt") as file:
    dois = set(file.read().splitlines())


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
    if ("contributionarea" in tags or "not research" in tags) and doi in dois
}

num_tot = len(dois)
num_done = len(done)
num_left = num_tot - num_done
done_percentage = num_done / num_tot * 100

print(f"{num_done}/{num_tot} ({done_percentage:.2f}%) num_left={num_left}")

for doi in tags_from_doi:
    if doi not in done:
        print(doi)
