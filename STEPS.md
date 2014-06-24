# Qrator: Steps to help you get starter

## Requirements

First, install scrapy and scrapyd. Then:


## Execution steps

* If you have deployed scrapyd through services, then go ahead and run:
```
$ scrapyd-deploy 
```

* If you haven't and just run the above command, you'll get an error^^:
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
