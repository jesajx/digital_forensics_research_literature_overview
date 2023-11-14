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
* TODO tag quality of paper?
* TODO tag outdatedness of paper?
* TODO dead conferences
* TODO include papers from non-DF-specific journals and conferences? e.g. IEEE Access.
* TODO use citation graphs to find more venues (openalex, crossref, etc.)?
* TODO use keyword search or not?
* TODO include NIST guides?
* TODO IEEE Conference on Communications and Network Security 2017 "network forensic workshop"?
* TODO IEEE International Workshop on Systematic Approaches to Digital Forensic Engineering (SADFE'07)
* TODO Conference on Digital Forensics, Security and Law (ADFSL)
* TODO Journal on Digital Forensics, Security and Law (JDFSL)
* TODO Wiley's WIREs (multidisciplinary forensics)?  https://wires-onlinelibrary-wiley-com.ezp.sub.su.se/journal/25739468
* TODO FBI forensic sciences communications? https://archives.fbi.gov/archives/about-us/lab/forensic-science-communications/fsc/archives

## Sources (for DOIs)
* Digital Investigation (aka "Forensic Science International: Digital Investigation"):
    * TODO date. scopus (query: SRCTITLE({digital investigation})).
* IFIP wg 11.9
    * 2023-08-31. Manually go through each book: https://link.springer.com/conference/digitalforensics
* IEEE Transactions on Information Forensics and Security (TIFS)
    * 2023-08-31. scopus (query: SRCTITLE({Information Forensics and Security})). Grep DOIs containing "TIFS".
* IEEE International Workshop on Information Forensics and Security (WIFS):
    * 2023-08-31. scopus (query: SRCTITLE({Information Forensics and Security})). Grep DOIs containing "WIFS".
* International Conference on Availability, Reliability and Security (ARES)
    * Only subtracks/workshops: WSDF and IoT-SECFOR.
    * 2023-08-31. From ACM library and IEEE Xplore. ARES was published by IEEE until 2016 and since then by ACM. I looked at the "table of contents" of each proceeding to figure out which papers were in what workshop and then copied dois one paper at a time.
* International Symposium on Digital Forensics and Security (ISDFS)
    * 2023-09-03. from IEEE Xplore.
* International Conference on Digital Forensics and Cyber Crime (ICDF2C)
    * 2023-09-03. from Springer Link.
* International Journal of Digital Crime and Forensics (IJDCF)
    * 2023-09-03. from Scopus. (query: SRCTITLE({International Journal of Digital Crime and Forensics})). TODO doublecheck query string
* International Journal of Electronic Security and Digital Forensics (IJESDF)
    * 2023-09-03. from Scopus. (query: SRCTITLE({International Journal of Electronic Security and Digital Forensics})). TODO doublecheck query string

## Note on IEEE Xplore
To download a whole conference from IEEE Xplore, go to that of proceedings (for example [ARES](https://ieeexplore.ieee.org/xpl/conhome/1001707/all-proceedings)) and then check "search within publication" near the search bar at the top of the page. Type any text in the search bar and click search. On the next page, a list of "filters" will show up near the top, so uncheck your search text from that list of filters. Now the only filter should be the conference: `"Parent Publication Number":1001707`. Near the top of the page is a big blue "export"-button.

## Note on Springer Link
Similar trick as with IEEE. Go to a list of proceeding (for example [ICDF2C](https://link-springer-com.ezp.sub.su.se/conference/icdf2c)) and search for any text.
On the next page, delete the `query` parameter from the url. There is a download-button (a gray box with a down-pointing arrow) in the top right of the page.

## Process
1. Download all dois (or links) for a few select (reputable) venues.
1. Open one at a time and skim the title and abstract. If the abstract is
   ambiguous, skim the "conclusion"-section of the paper. If the conclusion is ambigious, skim rest of the paper.
    * for TIFS and WIFS I cheated a little and searched among the paper titles (e.g. for "camera" and "jpeg") and then if the classification seemed obvious for all titles then I mass-labelled the search results.
1. Decide on tags/themes/keywords as we go. Hierarchically classify (i.e. do a
   rough classification first and then classify each subgroup in more detail, fix misclassifications as we go).
