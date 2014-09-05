#!/bin/bash

date >> jobIDs.txt

curl http://localhost:6800/schedule.json -d project=qrator -d spider=HBR >> jobIDs.txt
curl http://localhost:6800/schedule.json -d project=qrator -d spider=nytHome >> jobIDs.txt
curl http://localhost:6800/schedule.json -d project=qrator -d spider=nytInternationalHome >> jobIDs.txt
#curl http://localhost:6800/schedule.json -d project=qrator -d spider=ft >> jobIDs.txt

curl http://localhost:6800/schedule.json -d project=qrator -d spider=hackerNews >> jobIDs.txt
# curl http://localhost:6800/schedule.json -d project=qrator -d spider=techReview
# curl http://localhost:6800/schedule.json -d project=qrator -d spider=bInsider
# curl http://localhost:6800/schedule.json -d project=qrator -d spider=usaToday
# curl http://localhost:6800/schedule.json -d project=qrator -d spider=laTimes
# curl http://localhost:6800/schedule.json -d project=qrator -d spider=theTimes
# curl http://localhost:6800/schedule.json -d project=qrator -d spider=wsj
# curl http://localhost:6800/schedule.json -d project=qrator -d spider=discoverMag
# curl http://localhost:6800/schedule.json -d project=qrator -d spider=arsTechnica

echo "" >> jobIDs.txt
