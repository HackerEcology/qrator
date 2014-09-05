#!/bin/sh

curl http://localhost:6800/listspiders.json?project=qrator
curl http://localhost:6800/schedule.json -d project=qrator -d spider=HBR
curl http://localhost:6800/listjobs.json?project=qrator
