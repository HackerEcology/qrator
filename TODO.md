- [x] upload module (export direct-to-DB)
- [x] including docs
- [ ] data-redundancy checks
- [x] include a proper python scheduler script
  - [ ] fix manual reactor stop action after all spiders crawled. (i.e., Ctrl+C)
- [ ] fix ft spider parsing all the pages since 2007: currently commented out in newscrawlers.py
- [ ] fix techcrunch spider: all categories appended everytime to each entry.

***

- [ ] SPIDERS:
  - [x] nyt
  - [x] nyt Int. Home
  - [x] Craig # not needed anymore
  - [x] Hacker News
  - [x] financial times 
    - [ ] fix results
  - [x] hacker news
  - [x] Discover Mag
  - [x] TechCrunch
  - [ ] mit technologyreview
  - [ ] business insider
  - [ ] phys.org

  - [ ] mit-tech
    - [x] skeleton
    - [ ] define methods to parse rss links from techReview recursively
    - [ ] fix results. [all category links appear in each category]    

  - [ ] HBR
    - [x] skeleton
    - [x] fix errors
    - [ ] fix Selector vs HtmlXPathSelector issue

***
- [x] packaging and testing.
- [ ] ES mappings:
  - [x] nytHome and nytInternationalHome
  - [ ] HBR
  - [ ] FT
  - [ ] HackerNews
- [ ] HTML Filter pipelines:
  - [x] nytHome and nytInternationalHome
  - [x] TechCrunch