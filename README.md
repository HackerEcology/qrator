qrator
======

This project scrapes data from various news feeds.
 
# Steps to help you get started

## Requirements

First, install scrapy and scrapyd (Ref: http://scrapyd.readthedocs.org/en/latest/install.html). 

Ensure that service 'scrapyd' is running (sudo service scrapyd start). Then:


## Execution steps

* If you haven't deployed the project yet, then go to project root and run:
```
$ scrapyd-deploy 
```

* If you aren't running scrapyd as a service, and just ran the above command, you'll get an error^^:
```
Deploying to project "qrator" in http://localhost:6800/addversion.json
Deploy failed: <urlopen error [Errno 111] Connection refused>
```
^^To avoid this, open two terminals:

1. In one of them, run :
```
$ scrapyd
```

2. In the second one:
          
```
$ scrapyd-deploy          
```

## NOTE 
- scrapyd-deploy works directly because the config is already 
  defined in scrapy.cfg file. Else, one has to run:

  ```
  $ scrapyd-deploy default -p qrator 
  ```

- News sources include major agencies like WSJ, HN, NYTimes and so on..

- Refer to ```cmd_curl.sh``` for sample commands. Run this first 
  and go to http://localhost:6800/items/qrator/

- sample crawl command: ```$ scrapy crawl HBR```

- http://localhost:6800/ -> Default URL

- http://doc.scrapy.org/en/latest/topics/architecture.html Scrapy Architecture