#!/bin/bash

date >> jobIDs.txt

curl http://localhost:6800/schedule.json -d project=default -d spider=HBR >> jobIDs.txt
curl http://localhost:6800/schedule.json -d project=default -d spider=nytHome >> jobIDs.txt
curl http://localhost:6800/schedule.json -d project=default -d spider=nytInternationalHome >> jobIDs.txt
curl http://localhost:6800/schedule.json -d project=default -d spider=ft >> jobIDs.txt

# curl http://localhost:6800/schedule.json -d project=default -d spider=hackerNews
# curl http://localhost:6800/schedule.json -d project=default -d spider=techReview
# curl http://localhost:6800/schedule.json -d project=default -d spider=bInsider
# curl http://localhost:6800/schedule.json -d project=default -d spider=usaToday
# curl http://localhost:6800/schedule.json -d project=default -d spider=laTimes
# curl http://localhost:6800/schedule.json -d project=default -d spider=theTimes
# curl http://localhost:6800/schedule.json -d project=default -d spider=wsj
# curl http://localhost:6800/schedule.json -d project=default -d spider=discoverMag
# curl http://localhost:6800/schedule.json -d project=default -d spider=arsTechnica

echo "" >> jobIDs.txt