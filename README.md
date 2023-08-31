# (Work in progress) An overview of the Digital Forensics research literature

Systematic Literature Review of academic papers in Digital Forensics to give
an overview of various subareas in the field.

## TODO

* clean up old tags
* generate pretty graphs (and post them in this readme)
* review "contribution areas" tags for misclassifications.
* Write a "contribution" summary for every paper.
* Rename some tags and write explanations (since the semantics of some tags
  is non obvious and tend to drift through the process).
* More papers
* TODO include theses, books, standards and tools?

## Sources (for DOIs)
* Digital Investigation:
    * TODO date. scopus (query: SRCTITLE({digital investigation})).
* IFIP wg 11.9
    * 2023-08-31. Manually go through each book: https://link.springer.com/conference/digitalforensics
* IEEE Transactions on Information Forensics and Security (TIFS)
    * 2023-08-31. scopus (query: SRCTITLE({Information Forensics and Security})). Grep DOIs containing "TIFS".
* IEEE International Workshop on Information Forensics and Security (WIFS):
    * 2023-08-31. scopus (query: SRCTITLE({Information Forensics and Security})). Grep DOIs containing "WIFS".


more TODO:
* TODO DFRWS (I suspect not everything is published as special issues of Digital Investigation, especially older papers).
* ARES WSDF and ARES IoT-SECFOR. download dois from IEEE and ACM.
    * ieee: go to ares on ieee xplore
      (https://ieeexplore.ieee.org/xpl/conhome/1001707/all-proceedings), then check "search within publication" near the search bar at the top of the page. type any text in the search bar. On the next page the filters used will show up near the top, so uncheck the one for your searchbar text. Now the only filter should be: `"Parent Publication Number":1001707`. Near the top of the page is a big blue "export"-button.
    * on ieee, also visit each conference one by one to see the table of contents (https://ieeexplore-ieee-org.ezp.sub.su.se/xpl/conhome/5437532/proceeding?isnumber=5437988&sortType=vol-only-seq&pageNumber=1). WSDF started in 2008 (judging from the archives on ares-conference.eu)
    * acm: visit each conference one by one to scroll down and select the groups of papers in wsdf and IoT-SECFOR, and then export citations. IoT-SECFOR started in 2018.
* TODO ARES IoT-SECFOR
* TODO dead conferences
* TODO include papers from non-DF-specific journals and conferences? e.g. IEEE Access.
* TODO use citation graphs to find more venues (openalex, crossref, etc.)?
* TODO use keyword search or not?

## Process
1. Download all dois (or links) for a few select (reputable) venues.
1. Open one at a time and skim the title and abstract. If the abstract is
   ambiguous, skim the "conclusion"-section of the paper. If the conclusion is ambigious, skim rest of the paper.
1. Decide on tags/themes/keywords as we go. Hierarchically classify (i.e. do a
   rough classification first and then classify each subgroup in more detail, fix misclassifications as we go).
1. ???
1. profit.


