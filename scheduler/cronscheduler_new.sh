#!/bin/bash

# follow instructions in scheduler/README.md for this file.

cd ~/qrator/
rm ~/item_hbr.json; scrapy crawl HBR  -o ~/item_hbr.json -t json
rm ~/item_nythome.json; scrapy crawl nytHome  -o ~/item_nythome.json -t json
rm ~/item_nytinthome.json; scrapy crawl nytInternationalHome  -o ~/item_nytinthome.json -t json
#scrapy crawl mitTheTech -o ~/item_mitthetech.json -t json
rm ~/item_hackernews.json; scrapy crawl hackerNews -o ~/item_hackernews.json -t json
#rm ~/item_craig.json; scrapy crawl craig -o ~/item_craig.json -t json
rm ~/item_techcrunch.json; scrapy crawl TechCrunch -o ~/item_techcrunch.json -t json
rm ~/item_discovermag.json; scrapy crawl DiscoverMag -o ~/item_discovermag.json -t json
#scrapy crawl ft

echo "Data overwritten to ~/item_*.json (if they existed)" 
date >> ~/last_job.txt
echo "time saved to ~/last_job.txt"
