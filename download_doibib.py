#!/usr/bin/env python3

import shelve

import requests
import bibtexparser
from tqdm import tqdm


def remove_latex_formatting(text):
    text = text.replace("{", " ")
    text = text.replace("}", " ")
    text = re.sub(r"\\\w+", "", text)
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    return text


def bib_parse(bibtex_string):
    [entry] = bibtexparser.loads(bibtex_string).entries
    entry["title"] = remove_latex_formatting(entry["title"])
    return entry


def remove_empty_lines(iterable):
    return [line for line in iterable if line.strip() != ""]


with open("all_dois.txt") as file:
    dois = set(remove_empty_lines(file.read().splitlines()))

with shelve.open("bibs.shelve") as db:
    dois = dois - set(db.keys())

    for doi in tqdm(dois):
        # TODO use crossref batch API instead?
        doiurl = f"https://doi.org/{doi}"
        response = requests.get(
            doiurl, headers={"Accept": "application/x-bibtex; charset=utf-8"}
        )
        db[doi] = response.content.decode("utf-8").replace("%2F", "/")

    res = {doi: bib_parse(bib) for doi, bib in db.items()}
    json_put("bibs.json", res)