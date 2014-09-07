#!/bin/sh
curl -XDELETE 'http://localhost:9200/qrator/'
curl -XPUT 'http://localhost:9200/qrator/'
#curl -XDELETE 'http://localhost:9200/qrator/nytHome'
#curl -XDELETE 'http://localhost:9200/qrator/nytInternationalHome'
curl -XPUT 'http://localhost:9200/qrator/nytHome/_mapping' -d @es_mappings/nytHome_mapping.json
curl -XPUT 'http://localhost:9200/qrator/nytInternationalHome/_mapping' -d @es_mappings/nytInternationalHome_mapping.json
