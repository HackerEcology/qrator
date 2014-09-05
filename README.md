qrator
======

This project scrapes data from various news feeds.
 
# Steps to help you get started

## Requirements

- Install requirements: ```$ pip install -r requirements.txt```
- scrapy (0.23 preferred) and scrapyd (http://scrapyd.readthedocs.org/en/latest/install.html). 
- Elasticsearch instance running on port 9200
- Ensure 'scrapyd' is running: ```$ sudo service scrapyd start```

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
* ^To avoid this, open two terminals:

  1. In one of them, run :
     ```
     $ scrapyd
     ```

  2. In the second one:
     ```
     $ scrapyd-deploy          
     ```
* scrapyd-deploy works directly because the config is already 
  defined in scrapy.cfg file. Else, one has to run:

  ```
  $ scrapyd-deploy default -p qrator 
  ```
* For various scheduling/crawl commands, check ```scheduler/``` 

## NOTE 

- News sources include major agencies like WSJ, HN, NYTimes and so on..

- http://localhost:6800/ -> Default scrapyd URL

- http://doc.scrapy.org/en/latest/topics/architecture.html Scrapy Architecture

- Refer to TODO.md for current project status.