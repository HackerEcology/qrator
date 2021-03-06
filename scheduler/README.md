* For dumping data crawled into ES instance:
  - Run ```$ ./es_mappings/upload_mapping.sh```
  - Run ```$ python scheduler.py```
  - (bug: currently this script doesn't stop unless you press ctrl+c)

* For installing cron job on ```cronscheduler.sh```, to run at 11 pm everyday:  
  1. copy cronscheduler.sh to home dir (~/); then:
  2. run ```$ crontab -e```, and append  ```*  23 *  *  *     ~/cronscheduler.sh```
  3. exit and check job through ```$ crontab -l```
  4. After one sample run after 11 pm, check contents of ```~/jobIDs.txt``` (automatically created).
  - NOTE: This doesn't dump data to ES. Only fills up contents of http://localhost:6800/items/qrator/

* For installing cron job on ```cronscheduler_new.sh```, to run at 11 pm everyday:  
  1. copy cronscheduler_new.sh to home dir (~/); then:
  2. run ```$ crontab -e```, and append  ```*  23 *  *  *     ~/cronscheduler_new.sh```
  3. exit and check job through ```$ crontab -l```
  4. After one sample run after 11 pm, check contents of Elasticsearch index 'qrator',
  5. After the sample run, check contents of files named with item_*.json in home directory.
  6. Time of last job is saved to ~/last_job.txt
  - Note: run ```$ ./es_mappings/upload_mapping.sh``` once before scheduling this.
  
* for deploying a sample job, run ```$ ./cmd_curl.sh```

* for cronscheduler_new.sh to work, create a symbolic link to the qrator source code:

  ```ln -s /media/F/workspace/A_PERSONAL_projects/HackerEcology/qrator/ ~/.```