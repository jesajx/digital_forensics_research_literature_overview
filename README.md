# (Work in progress) An overview/survey of the Digital Forensics research literature

Systematic Literature Review of academic papers in Digital Forensics to give
an overview of various subareas in the field.

## TODO
* maybe use full doi-urls instead of just DOIs? some conferences do not have dois (and we therefore need to use other urls for those), so having both be urls makes things more consistent.
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
* TODO multidisciplinary venues?
    * "forensic science international" https://www-sciencedirect-com.ezp.sub.su.se/journal/forensic-science-international/vol/346/suppl/C
    * "forensic science international: Synergy" https://www-sciencedirect-com.ezp.sub.su.se/journal/forensic-science-international-synergy
* TODO FBI forensic sciences communications? https://archives.fbi.gov/archives/about-us/lab/forensic-science-communications/fsc/archives
* TODO check for DFRWS papers that are not on DI
* TODO include korean DF journals?
* TODo International Association of Forensic Sciences (IAFS)?

## Sources (for DOIs/URLs)
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
* "Forensic Science International: Reports" (FSIR)
    * 2023-11-14. from sciencedirect.com (go through every issue by hand and filter out articles in the Digital Forensics-section as shown on the website).
        * TODO consider maybe also including articles from the the "General Forensics" and "Negative Result" sections.
* WIREs
    * 2023-11-14. from wiley.com (go through every issue by hand and filter out digital forensics related articles, and philosophical/general articles).
* JDFSL
    * 2023-11-14. Just wget commons.erau.edu/jdfsl and then do some grep and sed magic.
* ADFSL
    * 2023-11-14. Just wget commons.erau.edu/adfsl and then do some grep and sed magic.

## Note on IEEE Xplore
To download a whole conference from IEEE Xplore, go to that of proceedings (for example [ARES](https://ieeexplore.ieee.org/xpl/conhome/1001707/all-proceedings)) and then check "search within publication" near the search bar at the top of the page. Type any text in the search bar and click search. On the next page, a list of "filters" will show up near the top, so uncheck your search text from that list of filters. Now the only filter should be the conference: `"Parent Publication Number":1001707`. Near the top of the page is a big blue "export"-button.

## Note on ADFSL and JDFSL  (erau.edu)
Just use recursive wget.
    * JDFSL html pages have a `<meta> tag with `name=bepress_citation_doi` that contains either the DOI or a full DOI url.
    * ADFSL does not have DOIs, so just the url.

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
