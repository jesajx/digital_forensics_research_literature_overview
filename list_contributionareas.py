#!/usr/bin/env python3

import json
import re
import collections

#import string_grouper # TODO maybe look for typos

with open("tags.json") as file:
    tags_from_doi = json.load(file)

areas = collections.Counter()
for doi, tags in tags_from_doi.items():
    new_tags = set()

    for k in tags:
        k = k.lower()
        m = re.match(r"contributionarea\s*:(.*)", k)
        if m:
            a = m.group(1)
            a = a.strip()
            areas[a] += 1

areas = sorted(((c,a) for a,c in areas.items()))
for c,a in areas:
    print(c, a)
